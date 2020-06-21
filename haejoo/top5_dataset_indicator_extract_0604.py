import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import pandas as DataFrame

from tqdm import tqdm
import datetime, time
from datetime import date, timedelta

from apyori import apriori
from mlxtend.frequent_patterns import apriori, association_rules 


def main():
    stock_list = pd.read_excel('./combine_data_ratio.xlsx')
    indicator_data = pd.read_excel('./indicator_sheet_date.xlsx', sheet_name = None)
    top5_dataset = extract_top5_dataset(stock_list, indicator_data)

    writer = pd.ExcelWriter("top5_dataset_indicator.xlsx")
    top5_dataset.to_excel(writer, sheet_name='TOP5')
    writer.save()
    

def extract_top5_dataset(stock_list, indicator_data):
    top5_dataset = pd.DataFrame()
    day_list = make_day_list()
    
    for day in tqdm(day_list):
        try:
            top5 = stock_list[str(day)][1:6]
            day_data = indicator_data[str(day)]
            top5_indicator = extract_top5_indicator(day, top5, day_data)
            top5_dataset = top5_dataset.append(top5_indicator, ignore_index=True)
        except:
            continue
     
    return top5_dataset

def extract_top5_indicator(day, top5, day_data):
    top5_indicator = pd.DataFrame()
    # indicator_data = pd.read_excel(indicator_url, sheet_name = day)
    for stock in top5:
        top5_indicator = top5_indicator.append(day_data[day_data['회사명'] == stock], ignore_index=True)

    return top5_indicator
    



def make_day_list():
    day_list = []
    sdate = datetime.date(2017, 1, 1)
    edate = datetime.date(2020, 6, 4) 
    delta = edate - sdate

    for i in range(delta.days + 1):
        # print(sdate + timedelta(days=i))
        day_list.append(sdate + timedelta(days=i))

    return day_list
    
if __name__=="__main__":
    main()
from pykrx import stock
import numpy as np
import openpyxl as op
import pandas as pd

tickers = stock.get_market_ticker_list() # collect stock num
stock_num = np.array(tickers)

def add_zero(num):
    num = str(num)
    num = "0"*(6-len(num))+num
    return num
    print(num)



wf= op.Workbook()
wb2 = wf.active
wb2['A1']="종목 번호";wb2['B1']="종목 명"

for i in tickers:
    df = stock.get_market_ohlcv_by_date("20160101","20200406","049850")
    df = stock.get_market_ohlcv_by_date("20160101","20200406","060310")
    print(i)
    input()
    date_ = df.index
    end_costs = df.values
    date_idx = list()
    end_cost_values = list()
    #time index
    for i in date_:
        date_idx_tmp = str(i)
        date_idx.append(date_idx_tmp.split(" ")[0])
    #end_index
    for i in end_costs:
        #stock.get_market_ticker_name("종목번호")
        print(stock.get_market_ticker_name(add_zero(i[3])))
        input()
        end_cost_values.append(i[3])
 


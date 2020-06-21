import warnings
warnings.filterwarnings("ignore")

import talib as ta
from sklearn.preprocessing import MinMaxScaler

import numpy as np
import pandas as pd
import pandas as DataFrame

from tqdm import tqdm
import datetime, time

def main():
    stock_list = pd.read_excel('./stock_list_with_name_num_re.xlsx')
    stock_list.code = stock_list.code.map('{:06}'.format)

    # writer1 = pd.ExcelWriter("stock_data_indicator_new.xlsx")
    writer2 = pd.ExcelWriter("stock_data_indicator_normalize_new2.xlsx")
    writer3 = pd.ExcelWriter("stock_data_indicator_level_new2.xlsx")

    for i in tqdm(range(len(stock_list))):
        data =  pd.DataFrame()
        stock_code = stock_list.loc[i]['code']
        stock_name = stock_list.loc[i]['name']
        url = get_url(stock_name, stock_code)

        data = get_stock_data(url)
        indicator_data = get_indicator(data)
        normalized_data = normalize_indicator(indicator_data, data)
        leveling_data = leveling_indicator(normalized_data, data)

        indicator_data = indicator_data[data.index.year >= 2017]
        normalized_data = normalized_data[normalized_data.index.year >= 2017]
        leveling_data = leveling_data[leveling_data.index.year >= 2017]

        # indicator_data.to_excel(writer1, sheet_name=stock_name)
        normalized_data.to_excel(writer2, sheet_name=stock_name)
        leveling_data.to_excel(writer3, sheet_name=stock_name)

    # writer1.save()
    writer2.save()
    writer3.save()

def get_url(name, code): 
    url = 'http://finance.naver.com/item/sise_day.nhn?code={}'.format(code)

    return url 


def get_stock_data(url):
    df = pd.DataFrame() 

    for page in range(1, 100): 
        pg_url = '{url}&page={page}'.format(url=url, page=page) 
        df = df.append(pd.read_html(pg_url, header=0)[0], ignore_index=True) 
    
    df = df.dropna()
    df = type_change(df)

    return df

def type_change(df):
    df = df.rename(columns= {'날짜': 'date', '종가': 'close', '전일비': 'diff', 
                             '시가': 'open', '고가': 'high', '저가': 'low', '거래량': 'volume'})

    df[['close', 'diff', 'open', 'high', 'low', 'volume']] = df[['close', 'diff', 'open', 'high', 'low', 'volume']].astype(int) 
    df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d")

    df = df.sort_values(by=['date'], ascending=True)
    df = df.set_index("date")

    return df

def get_indicator(data):
    indicator_data = pd.DataFrame() 
    indicator_data = indicator_data.append(data)
    indicator_data['Fluctuation'] = np.log(data['close']/data['close'].shift(1))
    indicator_data['MA20'] = data['close'].rolling(window=20).mean()
    indicator_data['MA60'] = data['close'].rolling(window=60).mean()
    indicator_data['MA120'] = data['close'].rolling(window=120).mean()
    indicator_data['MA20P'] = data['close']/data['close'].rolling(window=20).mean()
    indicator_data['MA60P'] = data['close']/data['close'].rolling(window=60).mean()
    indicator_data['MA120P'] = data['close']/data['close'].rolling(window=120).mean()
    indicator_data['ATR'] = ta.ATR(np.array(data['high'].astype(float)), np.array(data['low'].astype(float)), np.array(data['close'].astype(float)), 30)
    indicator_data['slowk'], indicator_data['slowd'] = ta.STOCH(np.array(data['high'].astype(float)), np.array(data['low'].astype(float)), np.array(data['close'].astype(float)), fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
    indicator_data['RSI'] = ta.RSI(np.array(data['close'].astype(float)))
    indicator_data['ADX'] = ta.ADX(np.array(data['high'].astype(float)), np.array(data['low'].astype(float)), np.array(data['close'].astype(float)))
    indicator_data['macd'], indicator_data['macdsignal'], indicator_data['macdhist'] = ta.MACD(np.array(data['close'].astype(float)), fastperiod=12, slowperiod=26, signalperiod=9)
    indicator_data['aroondown'], indicator_data['aroonup'] = ta.AROON(np.array(data['high'].astype(float)), np.array(data['low'].astype(float)))
    indicator_data['MOM'] = ta.MOM(np.array(data['close'].astype(float)), timeperiod=120) / data['close'].shift(120) * 100
    indicator_data['VAR'] = ta.VAR(np.array(data['close'].astype(float)))
    indicator_data['WILLR'] = ta.WILLR(np.array(data['high'].astype(float)), np.array(data['low'].astype(float)), np.array(data['close'].astype(float)), timeperiod=14)

    return indicator_data

def normalize_indicator(indicator_data, data):
    mms_data = pd.DataFrame() 
    mms_data = mms_data.append(data)
    mms_data['MMS_MA20P'] = indicator_data['MA20P'].rolling(window=20).apply(lambda x : MMS(x) * 100)
    mms_data['MMS_MA60P'] = indicator_data['MA60P'].rolling(window=20).apply(lambda x : MMS(x) * 100)
    mms_data['MMS_MA120P'] = indicator_data['MA120P'].rolling(window=20).apply(lambda x : MMS(x) * 100)
    mms_data['MMS_ATR'] = indicator_data['ATR'].rolling(window=20).apply(lambda x : MMS(x) * 100)
    mms_data['MMS_slowk'] = indicator_data['slowk'].rolling(window=20).apply(lambda x : MMS(x) * 100)
    mms_data['MMS_slowd'] = indicator_data['slowd'].rolling(window=20).apply(lambda x : MMS(x) * 100)
    mms_data['MMS_MOM'] = indicator_data['MOM'].rolling(window=20).apply(lambda x : MMS(x) * 100)
    mms_data['MMS_RSI'] = indicator_data['RSI'].rolling(window=20).apply(lambda x : MMS(x) * 100)
    mms_data['MMS_ADX'] = indicator_data['ADX'].rolling(window=20).apply(lambda x : MMS(x) * 100)
    mms_data['MMS_macd'] = indicator_data['macd'].rolling(window=20).apply(lambda x : MMS(x) * 100)
    mms_data['MMS_macdsignal'] = indicator_data['macdsignal'].rolling(window=20).apply(lambda x : MMS(x) * 100)
    mms_data['MMS_macdhist'] = indicator_data['macdhist'].rolling(window=20).apply(lambda x : MMS(x) * 100)
    mms_data['MMS_aroondown'] = indicator_data['aroondown'].rolling(window=20).apply(lambda x : MMS(x) * 100)
    mms_data['MMS_aroonup'] = indicator_data['aroonup'].rolling(window=20).apply(lambda x : MMS(x) * 100)
    mms_data['MMS_VAR'] = indicator_data['VAR'].rolling(window=20).apply(lambda x : MMS(x) * 100)
    mms_data['MMS_WILLR'] = indicator_data['WILLR'].rolling(window=20).apply(lambda x : MMS(x) * 100)

    return mms_data

def leveling_indicator(normalized_data, data):
    level_data = pd.DataFrame()
    level_data = level_data.append(data)
    category = list(range(0,101,25))
    level_data['level_MA20P'] = level(normalized_data['MMS_MA20P'], 'MA20P', category)
    level_data['level_MA60P'] = level(normalized_data['MMS_MA60P'], 'MA60P', category)
    level_data['level_MA120P'] = level(normalized_data['MMS_MA120P'], 'MA120P', category)
    level_data['level_ATR'] = level(normalized_data['MMS_ATR'], 'ATR', category)
    level_data['level_slowk'] = level(normalized_data['MMS_slowk'], 'slowk', category)
    level_data['level_slowd'] = level(normalized_data['MMS_slowd'], 'slowd', category)
    level_data['level_MOM'] = level(normalized_data['MMS_MOM'], 'MOM', category)
    level_data['level_RSI'] = level(normalized_data['MMS_RSI'], 'RSI', category)
    level_data['level_ADX'] = level(normalized_data['MMS_ADX'], 'ADX', category)
    level_data['level_macd'] = level(normalized_data['MMS_macd'], 'macd', category)
    level_data['level_macdsignal'] = level(normalized_data['MMS_macdsignal'], 'macdsignal', category)
    level_data['level_macdhist'] = level(normalized_data['MMS_macdhist'], 'macdhist', category)
    level_data['level_aroondown'] = level(normalized_data['MMS_aroondown'], 'aroondown', category)
    level_data['level_aroonup'] = level(normalized_data['MMS_aroonup'], 'aroonup', category)
    level_data['level_VAR'] = level(normalized_data['MMS_VAR'], 'VAR', category)
    level_data['level_WILLR'] = level(normalized_data['MMS_WILLR'], 'WILLR', category)

    return level_data


def MMS(data):
    data = np.array(data)
    scaler = MinMaxScaler()
    scaler.fit(np.reshape(data, (-1,1)))
    return scaler.transform(np.reshape(data[-1], (-1,1)))

def level(data, indicator, category):
    data = np.array(data)
    bin_labels = ['{}_{}'.format(indicator,i) for i,_ in enumerate(category)]
    data = pd.cut(data, category, right=False, labels=bin_labels[:-1])

    return np.array(data)


if __name__=="__main__":
    main()
from pykrx import stock
import numpy as np
import pandas as pd
import time
 
tickers = stock.get_market_ticker_list() # collect stock num
stock_num = np.array(tickers)
 
for i in tickers:
    df = stock.get_market_ohlcv_by_date("20160101","20200406",i)
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
        print(i[3])
        end_cost_values.append(i[3])
 
    time.sleep(100)
 

from sklearn.datasets import load_iris
import numpy as np
import pandas as pd
import json
from pykrx import stock
import numpy as np
import os
import openpyxl as op
import pandas as pd


data = load_iris()
y = data.target
X = data.data[:, 2:]
feature_names = data.feature_names[2:]

from sklearn.tree import DecisionTreeClassifier

tree1 = DecisionTreeClassifier(criterion='entropy', max_depth=1,  random_state=0).fit(X, y)

"""
https://jfun.tistory.com/41
"""

company_list=list()
def stock_name_list():
    wb = op.Workbook()
    wb = op.load_workbook("./data/modify_data.xlsx")
    sheet1 = wb["Sheet1"]
    for idx, val in enumerate(sheet1):
        if idx == 0:
            continue
        company_list.append([val[0].value, val[1].value])
        # (종목명,종목번호)
    wb.close()
    return company_list
company_list = stock_name_list()
print(company_list)
data_ = dict()
cnt = 0
print(len(company_list))
for i in company_list:
    try:
        tmp = pd.read_excel("./data/indicator/stock_data_indicator.xlsx",sheet_name=i[0])
    except Exception as e:
        print(e)
        continue
    #2017-01-03만
    print(i[0])
    print(tmp.iloc[1])
    data_[i[0]] = tmp.iloc[1]









path = './data/indicator.csv'
cnt =0

V = pd.DataFrame(data_)
V=V.T
V










#
# path = './data/indicator.csv'
# cnt =0
#
# V = pd.DataFrame()
# for k,v in data_.items():
#     # print(v)
#     # print(type(v))
#     # df = v
#     # # tmp=dict()
#     # # tmp['기업']=k
#     # # tmp = pd.DataFrame(tmp)
#     # # df.append(tmp)
#     # v = pd.DataFrame(v)
#     print(type(v))
#     #V = pd.DataFrame(v,index=[k])
#     V = pd.DataFrame(v)
#
# V=V.T
# V=V.rename(index={1 : "CJ"})
#
#



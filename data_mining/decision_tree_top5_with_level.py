from pykrx import stock
import numpy as np
import openpyxl as op
import pandas as pd
import os
import pickle
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import export_graphviz
import graphviz
import pydotplus

menu_list=['회사명', 'date', 'close', 'diff', 'open', 'high', 'low', 'volume', 'level_MA20P', 'level_MA60P', 'level_MA120P', 'level_ATR', 'level_slowk', 'level_slowd', 'level_MOM', 'level_RSI', 'level_ADX', 'level_macd', 'level_macdsignal', 'level_macdhist', 'level_aroondown', 'level_aroonup', 'level_VAR', 'level_WILLR','up']


path_indicator= "../data/indicator/with_level_indicator"
if os.path.exists(path_indicator):
    file = open(path_indicator, "rb")
    indicator = pickle.load(file)


for idx,date_ in enumerate(indicator.keys()):
    print(idx, " : ",date_)
    if idx ==0:
        df = pd.DataFrame.from_dict(indicator[date_],orient='index',columns=menu_list)
        continue
    tmp = pd.DataFrame.from_dict(indicator[date_],orient='index',columns=menu_list)
    df = pd.concat([df,tmp])
df_ = df.dropna(axis=0) #없는 값 제거
train_pre = df_[menu_list[8:-1]]
pd.options.mode.chained_assignment = None#열 전체 값 바꾸는 것 허용

#LEVEL 되어있는 것을 바꿈. enum 느낌으로
for idx,val in enumerate(menu_list):
    if idx == len(menu_list)-1:
        break
    if idx>7:
        try :
            le = LabelEncoder()
            result = le.fit_transform(train_pre[val])
            train_pre[val] = result
        except Exception as e:
            print(e)


x_train, x_test, y_train, y_test = train_test_split(train_pre, df_['up'], test_size=0.1, random_state=13)
tree_clf = DecisionTreeClassifier(max_depth=8, random_state=13)

#input("TIME : ")

tree_clf.fit(x_train, y_train)

tree_clf.fit(x_train, y_train)
print(tree_clf.max_depth)
print('TRAIN Score: {}'.format(tree_clf.score(x_train, y_train)))
print('TEST Score: {}'.format(tree_clf.score(x_test, y_test)))





print(menu_list[8:-1])
#input("TIME 2 : ")
export_graphviz(tree_clf, out_file="level_indicator_DT.dot",feature_names=menu_list[8:-1],class_names=["TOp5","XXX"], filled=True, impurity=False)


import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
with open('./level_indicator_DT.dot') as file_reader:
    dot_data = file_reader.read()
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_png("with_level.png")

"""
DT 그림 설명 : https://injo.tistory.com/15
"""


"""

#시각화 부분
from sklearn.metrics import  accuracy_score
y_pred = tree_clf.predict(x_test)
print("Accuracy : %.5f" %accuracy_score(y_test,y_pred))


export_graphviz(tree_clf, out_file="indicator_DT.dot",
                feature_names=menu_list[7:-1],
                class_names=train_pre.index, filled=True, impurity=False)

with open("indicator_DT.dot") as f :
    dot_graph = f.read()
dot = graphviz.Source(dot_graph) # dot_graph의 source 저장
dot.render(filename='tree.png') # png로 저장


"""










# 일단 2017-01-02 만을 본다
#
# for i in df2:
#     print(i)
# for i in df2['2017-01-02']:
#     print(i)
# for date_,indicator_ in indicator.items():
#     for cp_name, cp_indicator in indicator_.items():
#         print(cp_name," : ",cp_indicator)
#         input("TIME")


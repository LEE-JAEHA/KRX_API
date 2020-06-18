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
as_menu_list = ['level_MA20P','level_MA60P','level_RSI','level_VAR','level_macdhist']
# top5 list 가져오기
# file = open("../data/indicator/level_top5","rb")
# top5 = pickle.load(file)
path_indicator= "../data/indicator/with_level_indicator"
if os.path.exists(path_indicator):
    file = open(path_indicator, "rb")
    indicator = pickle.load(file)

if os.path.exists("./pd_with_association_indicator.csv"):
    print("READ CSV")
    # df_ = pd.read_csv("./pd.csv")
    df_ = pd.read_csv("./pd_with_association_indicator.csv")
else:
    for idx,date_ in enumerate(indicator.keys()):
        print(idx, " : ",date_)
        if idx ==0:
            df = pd.DataFrame.from_dict(indicator[date_],orient='index',columns=menu_list)
            # df = pd.DataFrame.from_dict(indicator[date_], orient='index', columns=as_menu_list)
            continue
        tmp = pd.DataFrame.from_dict(indicator[date_],orient='index',columns=menu_list)
        # tmp = pd.DataFrame.from_dict(indicator[date_], orient='index', columns=as_menu_list)
        df = pd.concat([df,tmp])
    df_ = df.dropna(axis=0) #없는 값 제거

    import pandas as pd
    df_.to_csv("./pd_with_association_indicator.csv",encoding="UTF-8-sig")



train_pre = df_[menu_list[8:]]
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

# del train_pre["TOP5"]
# print(type(tmp))
# print(tmp.iloc[100:])
# tmp2 = tmp.iloc[100:]
# print("LENGTH 2 : ", len(tmp2))
# tmp3 = train_pre.iloc[0:len(train_pre)-100]
# print("LENGTH 3 : ", len(tmp3))
# input("TME " )



# up_list = train_pre["up"]
# up_list = up_list.iloc[len(train_pre)-1000:] #마지막 10일 up 지표

#up_list 에는 0.25 up에 대한 데이터가 들어가 있음
with open('./0.25up_list','rb') as f:
    up_list = pickle.load(f)

del train_pre['up']
len_ = len(up_list) # 200406까지 데이터만 쓰겠다.

x_valid = train_pre.iloc[len_-1000 : len_]
y_valid = up_list[len_-1000 :len_ ]

train_pre = train_pre.iloc[0:len_-1000] # 마지막 10일 전까지 보조 지표
up_list_tmp = up_list[0:len_-1000]


x_train, x_test, y_train, y_test = train_test_split(train_pre,up_list_tmp, test_size=0.1, random_state=13)

# from sklearn.ensemble import RandomForestClassifier
# from sklearn import metrics
# forest = RandomForestClassifier(n_estimators=100)
# forest.fit(x_train, y_train)
# y_pred = forest.predict(x_test)
# print(y_pred)
# print(list(y_test))
# # 정확도 확인
# print('정확도 :', metrics.accuracy_score(y_test, y_pred))


tree_clf = DecisionTreeClassifier(criterion='entropy',max_depth=10, random_state=13)

#input("TIME : ")

tree_clf.fit(x_train, y_train)
print(tree_clf.max_depth)


print('TRAIN Score: {}'.format(tree_clf.score(x_train, y_train)))
print('TEST Score: {}'.format(tree_clf.score(x_test, y_test)))


# 실제 데이터를 이용하여 predict 해보기
from sklearn.metrics import accuracy_score
y_pred = tree_clf.predict(x_valid)


uu = 0
dd =0
up_up =0
up_down = 0
down_down =0
down_up = 0
for i,v in enumerate(y_valid):
    if v == True : # 실제 오른 경우
        uu+=1
        if v == y_pred[i] :#실제 올랐는데 올랐다고 판단
            up_up+=1
        if v != y_pred[i]:#실제 올랐는데 내렸다고 판단
            up_down+=1
    if v== False: #실제 떨어졌는데
        dd += 1
        if v == y_pred[i]:  # 실제 내렸는데 내렸다고 판단
            down_down += 1
        if v != y_pred[i]:  # 실제 내렸는데 올랐다고 판단
            down_up += 1
print("*"*30)
print("실제 오른 것 개수 : ",uu)
print("실제 올랐는데 올랐다고 판단 : ",up_up)
print("실제 올랐는데 내렸다고 판단 : ",up_down)
print("*"*30)
print('실제 내린 것 개수 : ',dd)
print("실제 내렸는데 내렸다고 판단 :",down_down)
print("실제 내렸는데 올랐다고 판단 :",down_up )
print("*"*30)
chk=0




print(menu_list[8:-1])
#input("TIME 2 : ")
export_graphviz(tree_clf, out_file="level_indicator_DT.dot",feature_names=menu_list[8:-1],class_names=["Top5","XXX"], filled=True, impurity=False)


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


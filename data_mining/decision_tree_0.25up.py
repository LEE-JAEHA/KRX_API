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

menu_list = ['close', 'diff', 'open', 'high', 'low', 'volume', 'MMS_MA20P', 'MMS_MA60P', 'MMS_MA120P', 'MMS_ATR', 'MMS_slowk', 'MMS_slowd', 'MMS_MOM', 'MMS_RSI', 'MMS_ADX', 'MMS_macd', 'MMS_macdsignal', 'MMS_macdhist', 'MMS_aroondown', 'MMS_aroonup', 'MMS_VAR', 'MMS_WILLR', 'search', 'combine',"TOP5"]
path_indicator= "../data/indicator/indicator_dict3"
if os.path.exists(path_indicator):
    file = open(path_indicator, "rb")
    indicator = pickle.load(file)
# for i in indicator['2017-01-12']['효성']:
#     print(i)


for idx,date_ in enumerate(indicator.keys()):
    #print(idx, " : ",date_)
    # if idx ==10:
    #     break
    if idx ==0:
        df = pd.DataFrame.from_dict(indicator[date_],orient='index',columns=menu_list)
        continue
    tmp = pd.DataFrame.from_dict(indicator[date_],orient='index',columns=menu_list)
    df = pd.concat([df,tmp])

df_ = df.dropna(axis=0) #없는 값 제거
# base_dir = "D:/수업/데마/stock_proj/KRX_API/data_mining/"
# file_nm = "df.xlsx"
# xlxs_dir = os.path.join(base_dir, file_nm)
# df_.to_excel(xlxs_dir)
# print(df_)
# input("!!!")

#train_pre=train_pre_.dropna(axis=0)
#pd.options.mode.chained_assignment = None#열 전체 값 바꾸는 것 허용


# for idx,val in enumerate(menu_list):
#     print(val)
#     if idx == len(menu_list)-1:
#         break
#     if idx>=6:
#         try :
#             le = LabelEncoder()
#             result = le.fit_transform(train_pre[val])
#             train_pre[val] = result
#         except Exception as e:
#             print("ERROR : ")
#             print(e)
#

train_pre = df_[menu_list[6:]]
train_pre = train_pre.sample(frac=0.8).reset_index(drop=True)

tmp = train_pre["TOP5"]
"""top5리스트 저장"""
import pickle
file = open("../data/indicator/level_top5","wb")
pickle.dump(train_pre["TOP5"],file)
file.close
# print(len(tmp))
# del train_pre["TOP5"]
# print(type(tmp))
# print(tmp.iloc[100:])
# tmp2 = tmp.iloc[100:]
# print("LENGTH 2 : ", len(tmp2))
# tmp3 = train_pre.iloc[0:len(train_pre)-100]
# print("LENGTH 3 : ", len(tmp3))
# input("TME " )
train_pre = train_pre.iloc[0:len(train_pre)-100]
up_list = tmp.iloc[100:]
train_pre = train_pre.iloc[:,:-3]#이부분을 통해 indicator 어떤 것들을 넣을 것인지
#x_train, x_test, y_train, y_test = train_test_split(train_pre, df_['TOP5'], test_size=0.1, random_state=13)
x_train, x_test, y_train, y_test = train_test_split(train_pre, up_list, test_size=0.1, random_state=13)
input("TME " )
tree_clf = DecisionTreeClassifier(criterion='entropy',max_depth=15 , random_state=13)


tree_clf.fit(x_train, y_train)
print(tree_clf.max_depth)

print('TRAIN Score: {}'.format(tree_clf.score(x_train, y_train)))
print('TEST Score: {}'.format(tree_clf.score(x_test, y_test)))



"""어떤 indicator를 많이 썼는지 시각화"""
import numpy as np
import matplotlib.pyplot as plt
feature_imp = tree_clf.feature_importances_
#print('{}'.format(feature_imp))

n_feature = train_pre.shape[1]
idx = np.arange(n_feature)
plt.barh(idx, feature_imp, align='center')
plt.yticks(idx, menu_list[6:-1])
plt.xlabel('feature importance', size=15)
plt.ylabel('feature', size=15)
plt.show()




print(menu_list[6:-1])
print("START MAKE DOT FILE")
export_graphviz(tree_clf, out_file="indicator_DT.dot",feature_names=menu_list[6:-3],class_names=["UP","DOWN"], filled=True, impurity=False)

print("FINISH MAKE DOT FILE")

import os
print("IMG START")
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
with open('./indicator_DT.dot') as file_reader:
    dot_data = file_reader.read()
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_png("iris4.png")
print("IMG FINISH")

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


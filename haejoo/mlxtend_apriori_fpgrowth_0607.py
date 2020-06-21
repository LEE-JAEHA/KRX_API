import warnings
warnings.filterwarnings("ignore")

from mlxtend.preprocessing import TransactionEncoder 
from mlxtend.frequent_patterns import apriori, association_rules, fpgrowth
import numpy as np
import pandas as pd
import time
from tqdm.notebook import tqdm
import seaborn as sns
import matplotlib.pyplot as plt

indicator_data = pd.read_excel('./top5_dataset_indicator.xlsx')
writer0 = pd.ExcelWriter("binary_indicator_dataset.xlsx")
writer1 = pd.ExcelWriter("mlxtend_frequent_pattern_result.xlsx")

level_data = indicator_data[['level_MA20P','level_MA60P','level_MA120P','level_ATR','level_slowk','level_slowd','level_MOM','level_RSI','level_ADX','level_macd','level_macdsignal','level_macdhist','level_aroondown','level_aroonup','level_VAR','level_WILLR']]
level_data = level_data.fillna('None')

level_list = [level_data.loc[i].tolist() for i in range(len(level_data))]

te = TransactionEncoder() 
te_result = te.fit(level_list).transform(level_list)
bi_data = pd.DataFrame(te_result, columns=te.columns_)
bi_data.to_excel(writer0, sheet_name='binary_indicator_dataset')


print("apriori start")
frequent_itemsets = apriori(bi_data, min_support=0.4, use_colnames=True)
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
frequent_itemsets.to_excel(writer1, sheet_name='frequent_itemsets')

print("association rule start")
association_rule = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
association_rule.to_excel(writer1, sheet_name='association_rule')

print("frequent itemsets filtering start")
frequent_itemsets_filtering = frequent_itemsets[ (frequent_itemsets['length'] == 4) &
                   (frequent_itemsets['support'] >= 0.4) ]
frequent_itemsets_filtering.to_excel(writer1, sheet_name='frequent_itemsets_filtering')

print("FP-growth start")
fp_frequent_itemsets = fpgrowth(bi_data, min_support=0.4, use_colnames=True)
fp_frequent_itemsets=association_rules(fp_frequent_itemsets,metric="lift",min_threshold=1)
fp_frequent_itemsets.to_excel(writer1, sheet_name='fp_growth')

writer0.save()
writer1.save()

print("Apriori_Vs_FP_Growth start")
l=[0.3,0.4,0.5,0.6,0.7]
f=[]
t=[]
for i in tqdm(l):
    t1=time.time()
    apriori(bi_data, min_support=i, use_colnames=True)
    t2=time.time()
    t.append((t2-t1)*1000)
    fpgrowth(bi_data,min_support=i,use_colnames=True)
    t3=time.time()
    f.append((t3-t2)*1000)

sns.lineplot(x=l,y=f,label="fpgrowth")
sns.lineplot(x=l,y=t,label="apriori")
plt.xlabel("Min_support Threshold")
plt.ylabel("Run Time in ms")
plt.savefig('Apriori_Vs_FP_Growth.png')
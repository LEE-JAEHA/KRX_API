from apyori import apriori
import pandas as pd

indicator_data = pd.read_excel('./top5_dataset_indicator.xlsx')

level_data = indicator_data[['level_MA20P','level_MA60P','level_MA120P','level_ATR','level_slowk','level_slowd','level_MOM','level_RSI','level_ADX','level_macd','level_macdsignal','level_macdhist','level_aroondown','level_aroonup','level_VAR','level_WILLR']]

observation = []
for i in range(len(level_data)):
    observation.append([str(level_data.values[i,j]) for j in range(16)])

associations = apriori(observation, min_length = 6, min_support = 0.3, min_confidence = 0.2, min_lift = 2)
associations = list(associations)
print(associations[0])
print("=====================================")

for item in associations:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")

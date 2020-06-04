from sklearn.datasets import load_iris
import numpy as np
import pandas as pd


data = load_iris()
y = data.target
X = data.data[:, 2:]
feature_names = data.feature_names[2:]

from sklearn.tree import DecisionTreeClassifier

tree1 = DecisionTreeClassifier(criterion='entropy', max_depth=1, random_state=0).fit(X, y)

"""
https://jfun.tistory.com/41
"""

top5 = pd.read_csv("./data/combine_data.xlsx")

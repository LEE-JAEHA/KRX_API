# Load libraries
from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets
from IPython.display import Image
from sklearn import tree
import pydotplus
import os


os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

with open('./indicator_DT.dot') as file_reader:
    dot_data = file_reader.read()




graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_png("iris2.png")
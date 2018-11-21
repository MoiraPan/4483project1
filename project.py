import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

#get data
test_ds = pd.read_csv("test.csv")
train_ds = pd.read_csv("train.csv")
train_ds.info()

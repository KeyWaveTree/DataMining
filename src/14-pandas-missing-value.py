import pandas as pd

data = pd.read_csv('../data/train.csv')
print(data.isnull().sum())

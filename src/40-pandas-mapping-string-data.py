import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/train.csv')

print('Sex')
print(data['Sex'].unique())
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
print(data['Sex'].unique())

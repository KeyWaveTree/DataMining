import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/train.csv')

for sex in ['male', 'female']:
    for pclass in range(1, 4):
        age_median = data[(data['Sex'] == sex) & (data['Pclass'] == pclass)]['Age'].median()
        data.loc[(data['Age'].isnull()) & (data['Sex'] == sex) & (data['Pclass'] == pclass), 'Age'] = age_median

print(data['Age'].isnull().sum())

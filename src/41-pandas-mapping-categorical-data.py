import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/train.csv')

for sex in ['male', 'female']:
    for pclass in range(1, 4):
        age_median = data[(data['Sex'] == sex) & (data['Pclass'] == pclass)]['Age'].median()
        data.loc[(data['Age'].isnull()) & (data['Sex'] == sex) & (data['Pclass'] == pclass), 'Age'] = age_median

print('Age')
print(data['Age'].unique())
data['Age'] = data['Age'].apply(lambda x: x // 10)
print(data['Age'].unique())


def fare2quantile(x):
    quantiles = [0.25, 0.5, 0.75]
    for i in range(len(quantiles)):
        if x < data['Fare'].quantile(quantiles[i]):
            return i
    else:
        return 3


data['Fare'] = data['Fare'].apply(fare2quantile)
print(data['Fare'].unique())

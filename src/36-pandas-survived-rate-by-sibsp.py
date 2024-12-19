import pandas as pd

data = pd.read_csv('../data/train.csv')

print(data[['SibSp', 'Survived']].groupby(['SibSp']).mean().sort_values(by='Survived', ascending=False))

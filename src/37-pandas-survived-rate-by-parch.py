import pandas as pd

data = pd.read_csv('../data/train.csv')

print(data[['Parch', 'Survived']].groupby(['Parch']).mean().sort_values(by='Survived', ascending=False))

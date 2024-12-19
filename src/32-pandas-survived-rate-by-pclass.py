import pandas as pd

data = pd.read_csv('../data/train.csv')

print(data[['Pclass', 'Survived']].groupby(['Pclass']).mean().sort_values(by='Survived', ascending=False))

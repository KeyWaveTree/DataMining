import pandas as pd

data = pd.read_csv('../data/train.csv')

print(data[['Sex', 'Survived']].groupby(['Sex']).mean().sort_values(by='Survived', ascending=False))

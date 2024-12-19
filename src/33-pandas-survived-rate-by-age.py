import pandas as pd

data = pd.read_csv('../data/train.csv')

data['Age'] = data['Age'].apply(lambda x: 10 * (x // 10))

print(data[['Age', 'Survived']].groupby(['Age']).mean().sort_values(by='Survived', ascending=False))

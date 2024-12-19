import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/train.csv')

data['Age'] = data['Age'].apply(lambda x: 10 * (x // 10))

pclass1 = data[data['Pclass'] == 1][['Age', 'Survived']].groupby(['Age']).mean().sort_values(by='Survived', ascending=False)
pclass2 = data[data['Pclass'] == 2][['Age', 'Survived']].groupby(['Age']).mean().sort_values(by='Survived', ascending=False)
pclass3 = data[data['Pclass'] == 3][['Age', 'Survived']].groupby(['Age']).mean().sort_values(by='Survived', ascending=False)

print('Pclass1')
print(pclass1)

print('Pclass2')
print(pclass2)

print('Pclass3')
print(pclass3)

fig, axes = plt.subplots(1, 3, figsize=(18, 8))

pclass1.plot(kind='bar', ax=axes[0], title='Pclass1')
pclass2.plot(kind='bar', ax=axes[1], title='Pclass2')
pclass3.plot(kind='bar', ax=axes[2], title='Pclass3')

plt.show()

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/train.csv')

survived = data[data['Survived'] == 1]['Sex'].value_counts()
dead = data[data['Survived'] == 0]['Sex'].value_counts()
df = pd.DataFrame([survived, dead])
df.index = ['Survived', 'Dead']
print(df)
df.plot(kind='bar')
plt.show()

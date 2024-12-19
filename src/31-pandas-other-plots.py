import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/train.csv')

data['Cabin'] = data['Cabin'].fillna('N')

data['Cabin'] = data['Cabin'].apply(lambda x: x[0])

plt.figure(0)
data['Age'].fillna(data['Age'].median()).apply(lambda x: (int(x) // 10) * 10).value_counts().sort_index().plot(kind='bar', stacked=True)

plt.figure(1)
data['Age'].fillna(data['Age'].median()).apply(lambda x: (int(x) // 10) * 10).value_counts().sort_index().plot(kind='barh', stacked=True)

plt.figure(2)
data.plot(kind='line')

plt.figure(3)
data['Age'].fillna(data['Age'].median()).plot(kind='hist', bins=[i * 10 for i in range(0, 10)])

plt.figure(4)
data.plot(kind='box')

plt.figure(5)
data['Age'].plot(kind='kde')

plt.figure(6)
data['Cabin'].value_counts().plot(kind='pie')

plt.figure(7)
N = 100
x = np.random.normal(scale=10, size=(N))
a = -5000
b = -60000
noise = np.random.normal(scale=50000, size=(N))
y = a * x + b + noise
xy = []
for xi, yi in zip(x, y):
    xy.append([xi, yi])
df = pd.DataFrame(xy, columns=['x', 'y'])
df.plot(kind='scatter', x='x', y='y')

plt.show()

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/train.csv')

data['Cabin'] = data['Cabin'].fillna('N')
data['Cabin'] = data['Cabin'].apply(lambda x: x[0])

cabins = data['Cabin'].value_counts().index.tolist()

cabins_survived_count = []

for cabin in cabins:
    cabin_survived_count = data[data['Cabin'] == cabin]['Survived'].value_counts()
    cabins_survived_count.append(cabin_survived_count)
df = pd.DataFrame(cabins_survived_count)
df.index = cabins
df.columns = ['0: Dead', '1: Survived']
print(df)
df.plot(kind='bar')
plt.show()

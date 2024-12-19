import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/train.csv')

pclass1_survived_count = data[data['Pclass'] == 1]['Survived'].value_counts()
pclass2_survived_count = data[data['Pclass'] == 2]['Survived'].value_counts()
pclass3_survived_count = data[data['Pclass'] == 3]['Survived'].value_counts()
df = pd.DataFrame([pclass1_survived_count, pclass2_survived_count, pclass3_survived_count])
df.index = ['Pclass1', 'Pclass2', 'Pclass3']
df.columns = ['0: Dead', '1: Survived']
print(df)
df.plot(kind='bar')
plt.show()

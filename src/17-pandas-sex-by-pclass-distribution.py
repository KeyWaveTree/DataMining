import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/train.csv')

pclass1_sex_count = data[data['Pclass'] == 1]['Sex'].value_counts()
pclass2_sex_count = data[data['Pclass'] == 2]['Sex'].value_counts()
pclass3_sex_count = data[data['Pclass'] == 3]['Sex'].value_counts()
df = pd.DataFrame([pclass1_sex_count, pclass2_sex_count, pclass3_sex_count])
df.index = ['Pclass1', 'Pclass2', 'Pclass3']
print(df)
df.plot(kind='bar')
plt.show()

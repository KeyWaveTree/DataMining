import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/train.csv')

male_survived_count = data[data['Sex'] == 'male']['Survived'].value_counts()
female_survived_count = data[data['Sex'] == 'female']['Survived'].value_counts()
df = pd.DataFrame([male_survived_count, female_survived_count])
df.index = ['male', 'female']
df.columns = ['0: Dead', '1: Survived']
print(df)
df.plot(kind='bar')
plt.show()

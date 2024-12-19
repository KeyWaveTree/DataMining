import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/train.csv')

data['Embarked'] = data['Embarked'].fillna('S')

s_survived_count = data[data['Embarked'] == 'S']['Survived'].value_counts()
c_survived_count = data[data['Embarked'] == 'C']['Survived'].value_counts()
q_survived_count = data[data['Embarked'] == 'Q']['Survived'].value_counts()
df = pd.DataFrame([s_survived_count, c_survived_count, q_survived_count])
df.index = ['S', 'C', 'Q']
df.columns = ['0: Dead', '1: Survived']
print(df)
df.plot(kind='bar')
plt.show()

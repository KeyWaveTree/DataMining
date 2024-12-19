import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/train.csv')

data['Age'] = data['Age'].apply(lambda x: x // 10)

ages_survived_count = []
for i in range(0, 10):
    age_survived_count = data[data['Age'] == i]['Survived'].value_counts()
    ages_survived_count.append(age_survived_count)
df = pd.DataFrame(ages_survived_count)
df.index = [str(i * 10) + 's' for i in range(0, 10)]
df.columns = ['0: Dead', '1: Survived']
print(df)
df.plot(kind='bar')
plt.show()

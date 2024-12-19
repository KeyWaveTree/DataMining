import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/train.csv')

data['Cabin'] = data['Cabin'].fillna('N')
data['Cabin'] = data['Cabin'].apply(lambda x: x[0])

cabin_count = data['Cabin'].value_counts()
print(cabin_count)
cabin_count.plot(kind='bar')
plt.show()

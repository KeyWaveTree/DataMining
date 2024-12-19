import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/train.csv')

data['Cabin'] = data['Cabin'].fillna('N')
data['Cabin'] = data['Cabin'].apply(lambda x: x[0])

cabin_without_missing_value = data[data['Cabin'] != 'N']['Cabin']

cabin_count = cabin_without_missing_value.value_counts()
print(cabin_count)
cabin_count.plot(kind='bar')
plt.show()

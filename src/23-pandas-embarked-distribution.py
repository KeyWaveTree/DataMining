import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/train.csv')

data['Embarked'] = data['Embarked'].fillna('S')

embarked_count = data['Embarked'].value_counts()
print(embarked_count)
embarked_count.plot(kind='bar')
plt.show()

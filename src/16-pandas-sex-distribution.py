import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/train.csv')

sex_count = data['Sex'].value_counts()
print(sex_count)
sex_count.plot(kind='bar')
plt.show()

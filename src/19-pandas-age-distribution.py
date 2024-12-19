import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/train.csv')

print(data['Age'])
data['Age'].plot(kind='hist')
# data['Age'].plot(kind='hist', bins=[i * 10 for i in range(0, 10)])
plt.show()

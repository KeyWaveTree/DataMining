import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/train.csv')

data['Age'].plot(kind='kde')
data[data['Sex'] == 'male']['Age'].plot(kind='kde')
data[data['Sex'] == 'female']['Age'].plot(kind='kde')
plt.legend(['Total', 'male', 'female'])
plt.show()

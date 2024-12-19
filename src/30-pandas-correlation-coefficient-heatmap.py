import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('../data/train.csv')

sns.heatmap(data=data.corr(), annot=True, fmt='.2f', cmap='Blues')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

#통계
mpg_data=sns.load_dataset('mpg')
mpg_data=mpg_data.drop('origin', axis=1)
mpg_data=mpg_data.drop('name', axis=1)

print(mpg_data.describe())

#그래프
sns.pairplot(mpg_data.describe())
plt.show()


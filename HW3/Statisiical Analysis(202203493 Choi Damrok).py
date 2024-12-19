import seaborn as sns
import numpy as np
import pandas as pd
import scipy.stats as stat
import statsmodels.formula.api as smf
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn import linear_model

#연속형 데이터
#mpg, displacement, horsepower, weight, acceleration
#범주형 데이터
#cylinders, model_year, origin, name
from statsmodels.regression.linear_model import OLS

mpg_data=sns.load_dataset('mpg')
#범주형 연속형 나누기
contiueus_data=['displacement', 'horsepower', 'weight', 'acceleration']
describe_data=['cylinders', 'model_year', 'origin', 'name']
independent_data=['displacement', 'horsepower', 'weight', 'acceleration',
                  'cylinders', 'model_year', 'origin', 'name']

print(mpg_data.groupby('cylinders').mean())
#범주형 변수들이 mpg의 평균값에 차이점이 존재하는 지를 검증(T-test)
for des in describe_data:
    mpg_array = np.array(mpg_data[des])
    data_array_series = pd.Series(mpg_array)
    if data_array_series.dtypes != object:
        t_stat, p_val=stat.ttest_ind(mpg_data['mpg'], data_array_series, equal_var=True)
        print(des)
        print('T-stat:', t_stat, 'P-value:', p_val)

#연속형 변수들이 mpg에 미치는 영향에 대한 상관분석(ANOVA)
model= smf.ols(formula='mpg~ displacement + horsepower + weight + acceleration',data=mpg_data)
fitting=model.fit()
anova=sm.stats.anova_lm(fitting)
print(anova)

#회귀모형
reg=linear_model.LinearRegression()
X=mpg_data.drop('mpg', axis=1)
y=mpg_data['mpg']
reg.fit(X, y)
y_2=reg.predict(X)

plt.scatter(X, y)
plt.plot(X, y_2)
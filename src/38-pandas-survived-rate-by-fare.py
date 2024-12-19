import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/train.csv')

def fare2quantile(x):
    quantiles = [0.25, 0.5, 0.75]
    for quantile in quantiles:
        if x < data['Fare'].quantile(quantile):
            return quantile
    else:
        return 1


data['Fare'] = data['Fare'].apply(fare2quantile) #apply: ()있는 데이터를 넘겨줌

print(data[['Fare', 'Survived']].groupby(['Fare']).mean().sort_values(by='Survived', ascending=False))

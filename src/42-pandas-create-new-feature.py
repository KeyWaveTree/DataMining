import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/train.csv')

data['FamilySize'] = data['SibSp'] + data['Parch']

print(data.columns)

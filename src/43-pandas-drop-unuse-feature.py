import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/train.csv')

data = data.drop(['PassengerId', 'Name', 'Ticket', 'Cabin', 'Embarked'], axis=1)

print(data.columns)

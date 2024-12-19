from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv('../data/train.csv')

for sex in ['male','female']:
    for pclass in range(1,4):
        age_median = data[(data['Sex'] == sex) and (data['Pclass'] == pclass)]['Age'].median()
        data.loc[(data['Age'].isnull()) and (data['Sex'] == sex) and (data['Pclass'] == pclass), 'Age'] = age_median

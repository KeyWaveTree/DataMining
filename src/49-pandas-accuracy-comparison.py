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

data = pd.read_csv('../data/train.csv')

for sex in ['male', 'female']:
    for pclass in range(1, 4):
        age_median = data[(data['Sex'] == sex) & (data['Pclass'] == pclass)]['Age'].median()
        data.loc[(data['Age'].isnull()) & (data['Sex'] == sex) & (data['Pclass'] == pclass), 'Age'] = age_median

data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data['Age'] = data['Age'].apply(lambda x: x // 10)


def fare2quantile(x):
    quantiles = [0.25, 0.5, 0.75]
    for i in range(len(quantiles)):
        if x < data['Fare'].quantile(quantiles[i]):
            return i
    else:
        return 3


data['Fare'] = data['Fare'].apply(fare2quantile)

data['FamilySize'] = data['SibSp'] + data['Parch']

data = data.drop(['PassengerId', 'Name', 'Ticket', 'Cabin', 'Embarked', 'SibSp', 'Parch'], axis=1)

X_train = data.drop('Survived', axis=1).values
target_label = data['Survived'].values

X_tr, X_var, y_tr, y_var = train_test_split(X_train, target_label, test_size=0.3, random_state=0)

classifier_names = ['Logistic', 'Radial SVM', 'Linear SVM', 'Random Forest', 'Decision Tree', 'KNN', 'Naive Bayes']
models = [LogisticRegression(), svm.SVC(kernel='rbf'), svm.SVC(kernel='linear'), RandomForestClassifier(), DecisionTreeClassifier(), KNeighborsClassifier(), GaussianNB()]
accuracies = []

for i in range(len(classifier_names)):
    models[i].fit(X_tr, y_tr)
    y_pred = models[i].predict(X_var)
    score = accuracy_score(y_pred, y_var)
    accuracy = round(np.mean(score) * 100, 2)
    accuracies.append(accuracy)

df = pd.DataFrame({'Model': classifier_names, 'Accuracy': accuracies}).sort_values(by='Accuracy', ascending=False)
df.reset_index(drop=True, inplace=True)
print(df)

from sklearn import svm

from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

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
y_label = data['Survived'].values

X_tr, X_val, y_tr, y_val = train_test_split(X_train, y_label, test_size=0.3, random_state=0)

model = svm.SVC(kernel='rbf')
model.fit(X_tr, y_tr)

y_pred = model.predict(X_val)

acc = round(accuracy_score(y_pred, y_val) * 100, 2)

print('[Radial SVM] Accuracy: {}%'.format(acc))

model = svm.SVC(kernel='linear')
model.fit(X_tr, y_tr)

y_pred = model.predict(X_val)

acc = round(accuracy_score(y_pred, y_val) * 100, 2)

print('[Linear SVM] Accuracy: {}%'.format(acc))

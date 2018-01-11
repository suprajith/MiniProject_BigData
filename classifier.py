import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from collections import Counter

from sklearn.externals.six.moves import zip

df = pd.read_csv("/home/supra/Downloads/project/Accidents_2016.csv")
'''
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
clf.predict([[2., 2.]])
'''
# x and y 
X = df.iloc[:,[9,11,12,13,14,15]]
y = df.iloc[:,3]

X = X.values
y = y.values
np.unique(y)
n_split = 109296

X_train, X_test = X[:n_split], X[n_split:]
y_train, y_test = y[:n_split], y[n_split:]

bdt_discrete = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=None),
    n_estimators=50,
    learning_rate=1,
    algorithm="SAMME")

bdt_discrete.fit(X_train, y_train)

discrete_test_errors = []
discrete_test_accuracy = []

for discrete_train_predict in bdt_discrete.staged_predict(X_test):
	discrete_test_accuracy.append(accuracy_score(discrete_train_predict, y_test))
	discrete_test_errors.append(1. - accuracy_score(discrete_train_predict, y_test))

n_trees_discrete = len(bdt_discrete)

discrete_estimator_errors = bdt_discrete.estimator_errors_[:n_trees_discrete]
discrete_estimator_weights = bdt_discrete.estimator_weights_[:n_trees_discrete]

print("The estimator error of 50 stages are : ",discrete_estimator_errors)
print("The estimator weights of 50 stages are : ",discrete_estimator_weights)
print("The accuracy scores of 50 stages are : ",discrete_test_accuracy)



n_trees_discrete = len(bdt_discrete)


# Boosting might terminate early, but the following arrays are always
# n_estimators long. We crop them to the actual number of trees here:
discrete_estimator_errors = bdt_discrete.estimator_errors_[:n_trees_discrete]
discrete_estimator_weights = bdt_discrete.estimator_weights_[:n_trees_discrete]

plt.figure(figsize=(15, 5))

plt.subplot(131)
plt.plot(range(1, n_trees_discrete + 1),
         discrete_test_errors, c='black', label='SAMME')

plt.legend()
plt.ylim(0.18, 0.62)
plt.ylabel('Test Error')
plt.xlabel('Number of Trees')

plt.subplot(132)
plt.plot(range(1, n_trees_discrete + 1), discrete_estimator_errors,
         "b", label='SAMME', alpha=.5)

plt.legend()
plt.ylabel('Error')
plt.xlabel('Number of Trees')
plt.ylim((.2,discrete_estimator_errors.max() * 1.2))
plt.xlim((-20, len(bdt_discrete) + 20))

plt.subplot(133)
plt.plot(range(1, n_trees_discrete + 1), discrete_estimator_weights,
         "b", label='SAMME')
plt.legend()
plt.ylabel('Weight')
plt.xlabel('Number of Trees')
plt.ylim((0, discrete_estimator_weights.max() * 1.2))
plt.xlim((-20, n_trees_discrete + 20))

# prevent overlapping y-axis labels
plt.subplots_adjust(wspace=0.25)
plt.show()

# import the necessary modules
import sklearn
from sklearn import tree

features = [[2, 100], [6, 25], [1, 300], [1, 1000], [4, 100], [10, 100]]
labels = [1, 2, 1, 1, 2, 2] # 1 is Sports/Race car, 2 is Family Car

# train the model and test it
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print(clf.predict([[1, 140]]))
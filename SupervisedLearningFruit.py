# import the necessary modules
import sklearn
from sklearn import tree

features = [[140, 1], [130, 1], [150, 0], [170, 0]] # 1 is smooth, 0 is bumpy
labels = [0, 0, 1, 1] # 0 is apple, 1 is orange

# train the model and test it
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print(clf.predict([[150, 0]]))
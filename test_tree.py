from decision_tree import *
from numpy import array
import scipy.io as sio

def max_depth(node):
    if node.is_leaf():
        return node.depth
    else:
        return max(max_depth(node.left_child), max_depth(node.right_child))

all_data = sio.loadmat('spam.mat')

dt = decision_tree(all_data['Xtrain'][0:3200,:], all_data['ytrain'][0:3200])
score = 0
for i in range(3200, 3450):
    score += dt.classify(all_data['Xtrain'][i,:]) == all_data['ytrain'][i][0]

print 'score = ' + str(score)
print 'error = ', str(1 - float(score) / 250)
print 'max depth = ', max_depth(dt.root)


dt = decision_tree(all_data['Xtrain'], all_data['ytrain'])
predictions = []
for i in range(len(all_data['Xtest'])):
    predictions.append(dt.classify(all_data['Xtest'][i,:]))


from decision_tree import *
from forest import *
from numpy import array
import scipy.io as sio
import csv

all_data = sio.loadmat('spam.mat')
data = all_data['Xtrain'][:,:]
labels = all_data['ytrain'][:]

#f = forest(data[0:3200,:], labels[0:3200], 100)
#score = 0
#for i in range(3200, 3450):
#    score += f.classify(data[i,:]) == labels[i][0]

#print 'score = ' + str(score)
#print 'error = ', str(1 - float(score) / 250)

print len(all_data['Xtest'])
f = forest(data, labels, 100)
predictions = []
for i in range(len(all_data['Xtest'])):
    predictions.append([i+1, f.classify(all_data['Xtest'][i,:])])

print predictions

with open('forestpredictions.csv', 'w', newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(predictions)

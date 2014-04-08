import adaboost
import scipy.io as sio

all_data = sio.loadmat('spam.mat')
data = all_data['Xtrain']
labels = all_data['ytrain']

ada = adaboost.ada_boost_forest(data, labels)

f = open('predictions.csv', 'w')
f.write("Id,Category\n")
for i in range(len(data)):
    f.write(str(i+1)+ "," + str(ada.classify(all_data['Xtest'][i,:])) + "\n")
f.close()


import forest
import scipy.io as sio
from numpy import array, ones
import math

def error(tree, data, labels):
    score = 0
    for i in range(len(data)):
        score += tree.classify(data[i,:]) == labels[i][0]
    error = 1 - (float(score) / len(data))
    return error



class ada_boost_forest():

    def __init__(self, data, labels, num_trees=10, num_iter=10):
        self.alphas = []
        self.trees = []
        weights = array(ones(len(data))) / float(len(data))
        for i in range(num_iter):
            print 'iteration', i
            tree = forest.forest(data, labels, num_trees, weights) 
            self.trees.append(tree)
            err = error(tree, data, labels)
            alpha = .5 * math.log((1 - err) / err)
            self.alphas.append(alpha)
            #check if each point was classified correctly, and update point's weight
            for d in range(len(data)):
                if tree.classify(data[d,:]) == labels[d][0]:
                    weights[d] *= math.exp(-alpha)
                else:
                    weights[d] *= math.exp(alpha)
            weights /= sum(weights)

    def classify(self, observation):
        final_hyp = 0
        for i in range(len(self.trees)):
            tree = self.trees[i]
            alpha = self.alphas[i]
            hyp = tree.classify(observation)
            if hyp == 0:
                hyp = -1
            final_hyp += alpha * hyp
        return int(final_hyp > 0)

    
if __name__ == '__main__':
    all_data = sio.loadmat('spam.mat')
    data = all_data['Xtrain']
    labels = all_data['ytrain']

    ada_boost = ada_boost_forest(data[:-250,:], labels[:-250])
    f = forest.forest(data[:-250,:], labels[:-250], 10)

    print 'ada', error(ada_boost, data[-250:,:], labels[-250:])
    print 'stand forest', error(f, data[-250:,:], labels[-250:])




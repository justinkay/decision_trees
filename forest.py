import random
import numpy
from decision_tree import *

class forest():

      def __init__(self, data, labels, num_trees, weights=None, randomized=False):
            self.data = data
            self.labels = labels
            self.trees = []
            num_obs = data.shape[0]
            num_features = data.shape[1]
            # uniformly weight data as default (can be modified for boosting)
            if weights == None:
                  weights = 1.0/num_obs*numpy.ones((num_obs,1))
            # split into num_trees training sets with data sampled with replacement according to weighting scheme
            # the sets are the same size as the original training set
            data_sets = numpy.zeros((num_trees, num_obs, num_features))
            label_sets = numpy.zeros((num_trees, num_obs, 1))
            for i in range(num_trees):
                  for j in range(num_obs):
                        sampled_obs_index = self.sample_index(weights)
                        data_sets[i,j] = data[sampled_obs_index, :]
                        label_sets[i,j] = labels[sampled_obs_index]
                        
            # train num_trees decision trees
            for i in range(num_trees):
                  self.trees.append(decision_tree(data_sets[i,:,:], label_sets[i,:], randomized))
                  #print i

      # assumes 0-1 labels
      def classify(self, observation):
            decision_sum = 0
            for tree in self.trees:
                  decision_sum = decision_sum + tree.classify(observation)
            return int(round(1.0*decision_sum/len(self.trees)))

      def sample_index(self, weights):
            rand_num = random.uniform(0.0,numpy.sum(weights))
            total = 0.0
            for (i, w) in numpy.ndenumerate(weights):
                  total += w
                  if total >= rand_num:
                        return i[0]
            print 'sampling error'
            return 0

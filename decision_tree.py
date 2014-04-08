import math
import pdb
import random
from numpy import array
from operator import itemgetter

class node():

    def __init__(self):
        self.func = None
        self.thresh = None
        self.parent = None
        self.right_child = self.left_child = None
        self.labels = None
        self.depth = 0

    def is_leaf(self):
        return self.right_child is None and self.left_child is None

    def set_right_child(self, child):
        self.right_child = child
        child.parent = self
        child.depth = self.depth + 1

    def set_left_child(self, child):
        self.left_child = child
        child.parent = self
        child.depth = self.depth + 1

    def decide(self, observation):
        if self.is_leaf():
            return self.labels.index(max(self.labels))
        if self.func(observation) < self.thresh:
            return self.left_child.decide(observation)
        else:
            return self.right_child.decide(observation)
        

class decision_tree():

    def __init__(self, data, labels, randomized=False):
        self.root = node()
        self.split(self.root, data, labels, randomized)
        

    def split(self, this_node, data, labels, randomized=False):
        
        try:
            lcount = (sum(labels==0)[0], sum(labels==1)[0])
        except:
            pdb.set_trace()
        this_node.labels = lcount
        
        # if leaf - return
        if 0 in lcount:
            #print lcount
            return

        if this_node.depth > 8:
            #print lcount
            return

        # find a function and thresh to split on
        # Iterate over the features
        min_entropy = float("inf")
        entropy_tuples = []
        for i in range(57):
            column = data[:,i]
            spam = column[(labels == 1)[:,0]]
            not_spam = column[(labels == 0)[:,0]]
            spam_av = float(sum(spam)) / len(spam)
            not_spam_av = float(sum(not_spam)) / len(not_spam)
            #print not_spam.shape, spam.shape, column.shape
            assert len(not_spam) + len(spam) == len(column)
            average = (spam_av + not_spam_av) / 2
            
            splitcol = column < average
            left = labels[splitcol]
            right = labels[array(map(lambda x : not x, splitcol))]
    

            # Compress the left and right labels into tuples of the counts, and calculate the entropy
            entropy = self.get_entropy((sum(left == 0), sum(left==1)),(sum(right==0), sum(right==1)))
            feature_tuple = (i, entropy, average)
            entropy_tuples.append(feature_tuple)

        # sort by entropy
        # if "randomized", pick randomly from the top 10 splits
        top_splits = sorted(entropy_tuples, key=itemgetter(1))
        if randomized == True:
            indx = random.randrange(10)
            feature = top_splits[indx][0]
            min_entropy = top_splits[indx][1]
            thresh = top_splits[indx][2]
        else:
            feature = top_splits[0][0]
            min_entropy = top_splits[0][1]
            thresh = top_splits[0][2]
        
        if min_entropy == self.get_entropy(lcount, (0, 0)):
            return
        func = lambda x: x[feature]
        this_node.func = func
        this_node.thresh = thresh
        
        left_child = node()
        right_child = node()
        this_node.set_left_child(left_child)
        this_node.set_right_child(right_child)

        # Recursively call split on our children
        col = data[:, feature]
        splitcol = col < thresh
        left_data = data[splitcol, :]
        right_data = data[array(map(lambda x : not x, splitcol)), :]
        left_labels = labels[splitcol]
        right_labels = labels[array(map(lambda x : not x, splitcol))]
        #print left_data.shape, right_data.shape, left_labels.shape, right_labels.shape
        self.split(left_child, left_data, left_labels)
        self.split(right_child, right_data, right_labels)

    def classify(self, observation):
        return self.root.decide(observation)

    # Calculates the entropy that results from a particular split of labels l1 and l2
    # l1 and l2 are tuples with the counts of each label in a particular segment
    def get_entropy(self, l1, l2):
        entropy1 = entropy2 = 0
        for count in l1:
            count = float(count)
            if count == 0:
                continue
            entropy1 -= (count/sum(l1)) * math.log(count/sum(l1),2)
        for count in l2:
            count = float(count)
            if count == 0:
                continue
            entropy2 -= (count/sum(l2)) * math.log(count/sum(l2),2)
        entropy = ((entropy1 * sum(l1)) + (entropy2 * sum(l2))) / (sum(l1) + sum(l2))
        return entropy

    #gini index, want to minimize
    def get_gini_impurity(self, l1, l2):
        return ((min(l1) / len(l1)) * sum(l1)) + ((min(l2) / len(l2)) * sum(l2))




import numpy
import math

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
            return self.labels.index(max(labels))
        if self.func(observation) < thresh:
            return self.left_child.decide(observation)
        else:
            return self.right_child.decide(observation)
        

class decision_tree():

    def __init__(self, data, labels):
        self.root = node()
        self.split(self.root, data, labels)
        

    def split(self, node, data, labels):

        
        lcount = (sum(labels==0), sum(labels==1))
        node.labels = lcount
        
        # if leaf - return
        if 0 in lcount:
            return

        # find a function and thresh to split on
        # Iterate over the features
        min_entropy = float("inf")
        for i in range(57):
            column = data[:,i]
            average = (min(column) + max(column)) / 2
            splitcol = column < average
            left = labels[splitcol]
            right = labels[not splitcol]
    

            # Compress the left and right labels into tuples of the counts, and calculate the entropy
            entropy = self.get_entropy((sum(left == 0), sum(left==1)),(sum(right==0), sum(right==1)))
            if entropy < min_entropy:
                min_entropy = entropy
                feature = i
                thresh = average


        func = lambda x: x[feature]
        node.func = func
        node.thresh = thresh
        
        left_child = node()
        right_child = node()
        node.set_left_child(left_child)
        node.set_right_child(right_child)

        # Recursively call split on our children
        col = data[:, feature]
        splitcol = col < thresh
        left_data = data[splitcol, :]
        right_data = data[not splitcol, :]
        left_labels = labels[splitcol]
        right_labels = labels[not splitcol]
        self.split(left_child, left_data, left_labels)
        self.split(right_child, right_data, right_labels)

    def classify(self, observation):
        return self.root.decide(observation)

    # Calculates the entropy that results from a particular split of labels l1 and l2
    # l1 and l2 are tuples with the counts of each label in a particular segment
    def get_entropy(self, l1, l2):
        entropy = 0
        for count in l1:
            count = float(count)
            if count == 0:
                continue
            entropy -= count/sum(l1) * math.log(count/sum(l1),2)
        for count in l2:
            count = float(count)
            if count == 0:
                continue
            entropy -= count/sum(l2) * math.log(count/sum(l2),2)

        return entropy




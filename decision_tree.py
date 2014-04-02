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
        pass
        # create root node
        # split
        

    def split(self, node, data, labels):
        pass
        # count labels, assign to node.labels
        # find a function and thresh to split on
        # if leaf - return
        # else - set node.func, thresh. create children, assign to parent, and call split on them.

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




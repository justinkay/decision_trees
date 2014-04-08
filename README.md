decision_trees
==============

Extra features:

1. Randomization in choosing features to split on - Our decision trees have the option of splitting on the best feature or choosing randomly from the top 10 features to split on. This did not affect our cross-validation accuracy for a single tree, but improved our cross-validation accuracy by 0.012 on a forest of 10 trees. Coupled with the random process of bagging, choosing features semi-randomly creates a more diverse set of trees to poll for classification.
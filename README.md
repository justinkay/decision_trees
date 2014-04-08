decision_trees
==============

Running the code:

decision_tree, forest, and adaboost are all classes in separate files, but
nothing automatically runs from calling those files. Running test_tree.py,
test_forest.py, and test_adaboost.py will actually build the appropriate classes
and genenerate the prediction csv. Assuming the correct files are in the same
directory. 

Extra features:

1. Randomization in choosing features to split on - Our decision trees have the option of splitting on the best feature or choosing randomly from the top 10 features to split on. This did not affect our cross-validation accuracy for a single tree, but improved our cross-validation accuracy by 0.012 on a forest of 10 trees. Coupled with the random process of bagging, choosing features semi-randomly creates a more diverse set of trees to poll for classification.
2. Gini impurity for splitting was also implemented. However in our current
code it isn't being used. It didn't seem to change permformance very much,
and most of the literature we saw said that these metrics are indeed not
very different. 

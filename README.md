decision_trees
Stefan Isenberger, Justin Kay, Avi Press
==============

We implemented the required decision tree, forest, and adaboost, and other
features explained at the end of the readme. By
cross-validating these on the training set, we aquired less than 1 percent
error (roughly .8, .7, .6% errors, respectively) while maintaing a reasonable maximum tree-depth (we ended settling on a
depth of 8). In addition to the given
reading materials, we also referred to wikipedia. 


Running the code:

decision_tree.py, forest.py, and adaboost.py are all classes in separate files, but
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

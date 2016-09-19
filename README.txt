the featureGeneration.py and featuresToDecisionTree.py files must be run by
following the steps below:

1. run "python featureGeneration.py <input.csv> <output.csv>"
where input.csv is a csv file of connect 4 test data with the first row
containing strings to identify each column.
and where output.csv is an empty or nonexistent csv file to save the feature
generation results to.

2. run "python featuresToDecisionTree.py <input.csv> <numFolds>"
where input.csv is the file created in step 1.
and where numFolds is the number of folds to use for the k-fold cross
validation method.


By default the feature numbers for featuresToDecisionTree.py are as follows:

feature1 = Piece in the bottom left
feature2 = Control of the center three columns
feature3 = Control of the bottom two rows
feature4 = First (highest) piece on the board
feature5 = Player with the highest average piece height


The output of featuresToDecisionTree.py is created in the following way.

For each test data set run during the k-fold cross validation the decision
tree returns an output and a list of the features used to classify the data
set.
If the outcome is the same as the winner of the test data it counts as a
success for each feature used to classify the data set.
if the outcome is different then it counts as a failure for each feature used
to classify the data set.
After all tests run the program prints the following for each feature:
  number of successes
  number of failures
  %error (number of failures divided by (successes + failures))

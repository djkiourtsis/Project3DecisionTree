import sys
import os.path
import csv
import math


def main(argv = None):
    # check arguments
    if len(argv) != 3:
        print "The correct input format is as follows: python featureToDecisionTree.py <input csv> <number of folds>"
        return
    inputData = []
    trainingData = []
    featureSuccess = []
    featureFail = []
    # try and open file
    if not os.path.isfile(argv[1]):
        print "This file either doesn't exist or the name was misspelled"
        sys.exit(0)
    # Extract input data from file
    # Iterate over the number of folds
    # Treat current fold as test data
    # trainingData = inputData[start:end] + inputData[start:end]
    # Create decision tree with rest as training data
    # Run fold as test data and modify feature success/fail
    # Print output for each feature
    return 0


class decisionTree:
    parentNode = None
    childNodes = [0]
    splitFeatureID = 0
    prevFeatureIDs = None
    treeTrainingData = None
    baseCaseOutput = 0
    # stuff
    def __init__(self, parentNode, prevFeatureIDs, treeTrainingData):
        self.parentNode = parentNode
        self.prevFeatureIDs = prevFeatureIDs
        self.treeTrainingData = treeTrainingData
        self.genChildren()
    #stuff
    def genChildren(self):
        # determine if base case (all data classified).  Set baseCaseOutput if so and return.
        # determine best attribute to split on
        # create children
        return
    #stuff
    def testData(self, testArray):
        # check if base case.  Return output and prevFeatureIDs if so.
        # pass testData to correct child
        return


main(sys.argv)

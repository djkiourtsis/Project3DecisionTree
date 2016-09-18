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
    featureSuccess = [0, 0, 0, 0, 0]
    featureTests = [0, 0, 0, 0, 0]
    testingData = []
    # try and open file
    if not os.path.isfile(argv[1]):
        print "This file either doesn't exist or the name was misspelled"
        sys.exit(0)
    # Extract input data from file
    r = open(argv[1])
    read = csv.reader(r)
    for row in read:
        for x in xrange(0, len(row)):
            row[x] = int(row[x])
        inputData.append(row)
    # Iterate over the number of folds
    split = len(inputData)/int(argv[2])
    for fold in xrange(0, int(argv[2])):
        # Treat current fold as test data
        # trainingData = inputData[start:end] + inputData[start:end]
        foldStartIndex = int(fold * split)
        foldEndIndex = int((fold * split) + split)
        testingData = inputData[foldStartIndex:foldEndIndex]
        trainingData = inputData[0:foldStartIndex] + inputData[foldEndIndex:len(inputData)]
        # Create decision tree with rest as training data
        dTree = decisionTree(None, [], [0,1,2,3,4], trainingData)
        # Run fold as test data and modify feature success/fail
        for row in xrange(0, len(testingData)):
            featureSplits, output = dTree.testData(testingData[row])
            for f in xrange(len(featureSplits)):
                featureTests[featureSplits[f]] += 1
                if output == testingData[row][42]:
                    featureSuccess[featureSplits[f]] += 1
    # Print output for each feature
    for row in xrange(0, len(featureSuccess)):
        print featureSuccess[row]
    for row in xrange(0, len(featureTests)):
        print featureTests[row]
    return 0


class decisionTree:
    parentNode = None
    childNodes = []
    childSplitValues = []
    splitFeatureID = 0
    prevFeatureIDs = []
    remainingFeatureIDs = []
    treeTrainingData = None
    baseCaseOutput = 0
    numFeatures = 5
    treeEntropy = 0.0
    # stuff
    def __init__(self, parentNode, prevFeatureIDs, remainingFeatureIDs, treeTrainingData):
        self.parentNode = parentNode
        self.prevFeatureIDs = prevFeatureIDs
        self.remainingFeatureIDs = remainingFeatureIDs
        self.treeTrainingData = treeTrainingData
        self.numFeatures = len(prevFeatureIDs) + len(remainingFeatureIDs)
        if (parentNode == None):
            # Get entropy for table outcome
            self.treeEntropy = binaryEntropy(1)
        self.genChildren()
    #stuff
    def genChildren(self):
        # determine if base case (all data classified).  Set baseCaseOutput if so and return.
        if (len(self.remainingFeatureIDs) < 1): # No more features to split on
            self.baseCaseOutput = self.treeTrainingData[0][42]
            return
        # determine best attribute to split on
        infoGains = [0 for x in xrange(len(self.remainingFeatureIDs))]
        featureValues = []
        for x in xrange(len(self.remainingFeatureIDs)):
            # featureData is a list of feature values and result values for the training data
            featureData = [[],[]]
            featureValues.append([])
            for y in xrange(len(self.treeTrainingData)):
                featureData[0].append(self.treeTrainingData[y][43+self.remainingFeatureIDs[x]])
                featureData[1].append(self.treeTrainingData[y][42])
                if (not self.treeTrainingData[y][43+self.remainingFeatureIDs[x]] in featureValues[x]):
                    featureValues[x].append(self.treeTrainingData[y][43+self.remainingFeatureIDs[x]])
            infoGains[x] = gain(featureData, featureValues[x], self.treeEntropy)
        # create children
        self.splitFeatureID = self.remainingFeatureIDs[0]
        for x in xrange(1, len(self.remainingFeatureIDs)):
            for x in xrange(len(featureValues[0])):
                # Generate child for each possible split of feature
                # Add child and split feature value to self
                a = None
        return
    #stuff
    def testData(self, testArray):
        # check if base case.  Return output and prevFeatureIDs if so.
        # pass testData to correct child
        return


def gain(dataArray, featureValues, treeEntropy):
    return 0


# Entropy is binary since only possible outcomes are win/loss for player 1
def binaryEntropy(probability):
    return 0


main(sys.argv)

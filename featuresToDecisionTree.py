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
    baseCaseOutput = -1
    numFeatures = 5
    treeEntropy = 0.0
    # stuff
    def __init__(self, parentNode, prevFeatureIDs, remainingFeatureIDs, treeTrainingData, treeEntropy):
        self.parentNode = parentNode
        self.prevFeatureIDs = prevFeatureIDs
        self.remainingFeatureIDs = remainingFeatureIDs
        self.treeTrainingData = treeTrainingData
        self.numFeatures = len(prevFeatureIDs) + len(remainingFeatureIDs)
        # Get entropy for table outcome
        outputSuccesses = 0
        for x in xrange(len(treeTrainingData)):
            if(treeTrainingData[x][42] == 1):
                outputSuccesses += 1
        self.treeEntropy = binaryEntropy(float(outputSuccesses)/len(treeTrainingData))
        self.genChildren()
    #stuff
    def genChildren(self):
        # determine if base case (no more features).  Set baseCaseOutput if so and return.
        if (len(self.remainingFeatureIDs) < 1): # No more features to split on
            self.baseCaseOutput = self.treeTrainingData[0][42]
            return
        # determine if base case 2 (all data classified)
        res = self.treeTrainingData[0][42]
        for x in xrange(1, len(self.treeTrainingData)):
            if res != self.treeTrainingData[x][42]:
                res = -1
                break
        if res != -1:
            self.baseCaseOutput = res
            return
        # determine best attribute to split on
        # infoGains[x] and featureValues[x] correspond with self.remainingFeatureIDs[x]
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
        # determine feature with best gain
        bestGain = infoGains[0]
        bestGainIndex = 0
        for x in xrange(1,len(infoGains)):
            if infoGains[x] > bestGain:
                bestGain = infoGains[x]
                bestGainIndex = x
        # create children
        self.splitFeatureID = self.remainingFeatureIDs[bestGainIndex]
        childRemainingFeatures = (self.remainingFeatureIDs[0:bestGainIndex] +
                                  self.remainingFeatureIDs[bestGainIndex+1:len(self.remainingFeatureIDs)])
        for x in xrange(len(featureValues[bestGainIndex])):
            splitTrainingData = []
            for i in xrange(len(self.treeTrainingData)):
                if (self.treeTrainingData[i][43+self.remainingFeatureIDs[bestGainIndex]] ==
                        featureValues[bestGainIndex][x]):
                    splitTrainingData.append(self.treeTrainingData[i])
            # Generate child for each possible split of feature
            child = decisionTree(self, self.prevFeatureIDs.append(self.splitFeatureID),
                                 childRemainingFeatures, splitTrainingData)
            # Add child and split feature value to self
            self.childNodes.append(child)
            self.childSplitValues.append(featureValues[bestGainIndex])
        return
    #stuff
    def testData(self, testArray):
        # check if base case.  Return output and prevFeatureIDs if so.
        if self.baseCaseOutput != -1:
            return [self.prevFeatureIDs.append(self.splitFeatureID), self.baseCaseOutput]
        # pass testData to correct child
        for x in xrange(len(self.childSplitValues)):
            if testArray[43+self.splitFeatureID] == self.childSplitValues[x]:
                return self.childNodes[x].testData(testArray)
        # value not classified by decision tree.  Return failure.
        return [[], -1]


def gain(dataArray, featureValues, treeEntropy):
    remainder = 0
    for x in xrange(len(featureValues)):
        # s is the number of 'hits' (player 1 wins) for the specific feature value
        s = 0
        # numClassified is the number of data points that have the same feature value
        numClassified = 0
        for row in xrange(len(dataArray)):
            if (dataArray[row][0] == featureValues[x]):
                numClassified += 1
                if (dataArray[row][1] == 1):
                    s += 1
        remainder += (float(numClassified)/len(dataArray))*binaryEntropy(float(s)/numClassified)
    return treeEntropy - remainder


# Entropy is binary since only possible outcomes are win/loss for player 1
def binaryEntropy(p):
    return -1*(p*math.log2(p)+(1-p)*math.log2(1-p))


main(sys.argv)

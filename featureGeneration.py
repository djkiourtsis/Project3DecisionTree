import sys
import os.path
import csv


def main(argv = None):
    # check arguments
    if len(argv) != 3:
        print "The correct input format is as follows: python featureGeneration.py <input csv> <output csv>"
        sys.exit(0)
    inputData = []
    outputData = []
    # try and open file
    if not os.path.isfile(argv[1]):
        print "This file either doesn't exist or the name was misspelled"
        sys.exit(0)
    # Read file line by line
    # For each line of data extract features
    # Add extracted features to output data
    # Save all data to output file
    return 0


def featurePieceBottomLeft(row):
    return row[0]


def featureCenterControl(row):
    score = 0
    for col in xrange(2,5):
        for row in xrange(0,6):
            if(row[6*col + row] == 1):
                score += 1
            elif(row[6*col + row] == 2):
                score -= 1
    return score


def featureBottomControl(row):
    score = 0
    for row in xrange(0, 2):
        for col in xrange(0, 6):
            if (row[6 * col + row] == 1):
                score += 1
            elif (row[6 * col + row] == 2):
                score -= 1
    return score


def featureHighestPiece(row):
    score = 0
    for row in xrange(0, 6):
        for col in xrange(0, 6):
            if (row[6 * col + (6-row)] == 1):
                return 1
            elif (row[6 * col + (6-row)] == 2):
                return 2
    return -1


def feature5(row):
    return 0


main(sys.argv)

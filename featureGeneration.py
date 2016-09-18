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
    return 0


def featureCenterControl(row):
    return 0


def feature3(row):
    return 0


def feature4(row):
    return 0


def feature5(row):
    return 0


main(sys.argv)

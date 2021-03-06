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
    r = open(argv[1])
    r.next()
    read = csv.reader(r)
    for row in read:
        for x in xrange(0, len(row)):
            row[x] = int(row[x])
        inputData.append(row)
    # For each line of data extract features
    #print inputData
    for row in inputData:
        feature1 = featurePieceBottomLeft(row)
        feature2 = featureCenterControl(row)
        feature3 = featureBottomControl(row)
        feature4 = featureHighestPiece(row)
        features5 = featureHighestPlayerPieces(row)
        # Add extracted features to output data
        row.extend([feature1,feature2,feature3,feature4,features5])
        outputData.append(row)
    # Save all data to output file
    o = open(argv[2], "wb+")
    write = csv.writer(o)
    for row in outputData:
        write.writerow(row)
    return 0


def featurePieceBottomLeft(row):
    return row[0]


def featureCenterControl(row):
    score = 0
    for c in xrange(2,5):
        for r in xrange(0,6):
            if(row[6*c + r] == 1):
                score += 1
            elif(row[6*c + r] == 2):
                score -= 1
    return score


def featureBottomControl(row):
    score = 0
    for r in xrange(0, 2):
        for c in xrange(0, 6):
            if (row[6 * c + r] == 1):
                score += 1
            elif (row[6 * c + r] == 2):
                score -= 1
    return score


def featureHighestPiece(row):
    for r in xrange(0, 6):
        for c in xrange(0, 6):
            if (row[6 * c + (5-r)] == 1):
                return 1
            elif (row[6 * c + (5-r)] == 2):
                return 2
    return -1


def featureHighestPlayerPieces(row):
    score1 = 0
    score2 = 0
    for r in xrange(0, 6):
        for c in xrange(0, 6):
            if(row[6 * c + r] == 1):
                score1 += r + 1
            elif(row[6 * c + r] == 2):
                score2 += r + 1
    if(score1 > score2):
        return 1
    elif(score2 > score1):
        return 2
    elif(score1 == score2):
        return 0


main(sys.argv)

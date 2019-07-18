# This file changes a space separated file into a comma separated one
import csv
import os

inFileName = input("What file would you like converted? ")
outFileName = os.path.splitext(inFileName)[0] + ".csv"

with open(inFileName) as inFile, open(outFileName, 'w') as outFile:
    for line in inFile:
        outFile.write(" ".join(line.split()).replace(' ', ','))
        outFile.write(",")


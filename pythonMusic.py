# This file takes a CSV file and converts it into MP3

from numpy import genfromtxt
import sys
import csv

if (len(sys.argv) > 1):
    fileName = sys.argv[1]
else:
    fileName = input('Input the name of the file that you want converted into music: ')


# Checks if the file exists 
def FileCheck(fn):
    try:
        open(fn, "r") 
        return 1
    except IOError:
        print ("Error: the file", fileName, " does not appear to exist.")
        return 0

# Formats the csv file in the case of strange formats
def formatFile(fileName):
    cleanFile = fileName.clean()
    return cleanFile


# This function takes the file and converts it to a numpy array
def ConvertFile(fileName):
    fileArray = genfromtxt(str(fileName), delimiter=',', dtype=None, encoding=None)
    return fileArray

# Run the program only if the file exists
if(FileCheck(fileName) == 1):
    convertedFile = ConvertFile(fileName)
    print(convertedFile)
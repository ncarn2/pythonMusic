# This file takes a CSV file and converts it into WAV
# Removes all string instances from the dataset

import music, numpy

import sys
import csv
import re
import math


def main():
    if (len(sys.argv) > 1):
        fileName = sys.argv[1]
    else:
        fileName = input('Input the name of the file that you want converted into music: ')

    # Run the program only if the file exists
    if(FileCheck(fileName) == 1):
        # Opens the file
        fileArray = ConvertFile(fileName)
        # Cleans the file 
        fileArray = FormatFile(fileArray)
        # Creates the music
        CreateMusicFile(fileArray, fileName)
    
    EndProgram('default')

# Ends the program
def EndProgram(reason):
    if(reason == 'string'):
        print("Failed to convert data, the provided dataset contains strings.")
    if(reason == 'file'):
        print("Failed to convert data, the given file does not exist.")
    if(reason =='default'):
        print("Conversion Complete.")
    exit()

# Checks if the file exists 
def FileCheck(fn):
    try:
        open(fn, "r") 
        return 1
    except IOError:
        print ("Error: the file", fn, "does not appear to exist.")
        return 0

# Removes unwanted variables from the array
def FormatFile(fileArray):
    acceptedTypes = [int, float]

    # regex for not white space and not empty string
    unwanted = re.compile("(.|\s)*\S(.|\s)*")

    cleanArray = list(filter(unwanted.search, fileArray)) 

    # Convert to floats


    # Remove all whitespace
    for i, value in enumerate(cleanArray):
        cleanArray[i] = cleanArray[i].replace(" ", "")
        try:
            cleanArray[i] = float(cleanArray[i])
        except:
            # Leave the string
            continue

    # Remove all words from array 
    cleanArray = [value for value in cleanArray if type(value) in acceptedTypes]

    return cleanArray 

# This method takes the file and converts it to a array
def ConvertFile(fileName):
    fileArray = []

    with open(fileName) as csvFile:
        csvReader = csv.reader(csvFile)

        #for each row, add each element into the fileArray
        for row in csvReader:
            for value in row:
                fileArray.append(value)

    return fileArray

# This method takes the array and converts it into a midi file
# This also converts the data to music notes
def CreateMusicFile(fileArray, fileName):
    minVal = min(fileArray)
    maxVal = max(fileArray)

    table = music.tables.Basic()
    H = music.utils.H

    print("Min Val: ", minVal)
    print("Max Val: ", maxVal)


if __name__ == '__main__':
    main()
# This file takes a CSV file and converts it into WAV
# Removes all string instances from the dataset
# This is a class assignment and does not follow standard PIP8

import music
import re, numpy
import os, sys
import csv

def main():
    if (len(sys.argv) > 1):
        fileName = sys.argv[1]
    else:
        fileName = input('Input the name of the file that you want converted into music: ')

    # Run the program only if the file exists
    try:
        open(fileName, "r")
    except IOError:
        print ("Error: the file", fileName, "does not appear to exist. Check if the file is in your working directory.")
        exit()

    # Opens the file
    fileList = ConvertFile(fileName)
    # Cleans the file 
    fileList = FormatFile(fileList)
    # Creates the music
    SimpleConversion(fileList, fileName)
    ComplexConversion(fileList, fileName) 

    # End the Program
    print("[*] Conversion Complete")
    exit()

# Removes unwanted variables from the array
def FormatFile(fileList):
    print("[*] Cleaning Dataset")
    acceptedTypes = [int]

    # regex for not white space and not empty string
    unwanted = re.compile("(.|\s)*\S(.|\s)*")

    cleanList = list(filter(unwanted.search, fileList)) 

    # Remove all whitespace
    for i, value in enumerate(cleanList):
        cleanList[i] = cleanList[i].replace(" ", "")
        try:
            # This takes care of scientific notation
            cleanList[i] = int(float(cleanList[i]))
        except:
            # Leave the string in the array
            continue

    # Remove all words from list 
    # Removes all 0 from list
    cleanList = [value for value in cleanList if type(value) in acceptedTypes and value > 0] 
    median = numpy.median(cleanList)
    cleanList = [value for value in cleanList if value < (3 * median)] 
    return cleanList 

# This method takes the file and converts it to a array
def ConvertFile(fileName):
    fileList = []

    with open(fileName) as csvFile:
        csvReader = csv.reader(csvFile)

        #for each row, add each element into the fileList
        for row in csvReader:
            for value in row:
                fileList.append(value)

    return fileList

# This method takes the array and converts it into a midi file
# This also converts the data to music notes
def SimpleConversion(fileList, fileName):
    fileName = os.path.splitext(fileName)[0] + "_simple.wav"
    print("[*] Creating Audio File")

    H = music.utils.H

    minHz = 100
    maxHz = 5000

    # Arbitrary length of the song
    songLength = 180#seconds

    # Amount of data values per second
    notesPerSecond = int(len(fileList)/songLength) if \
        int(len(fileList)/songLength) > 0 else 1

    minVal = min(fileList)
    maxVal = max(fileList)

    synth = music.core.Being()
    synth.d_ = [1]  # durations in seconds
    synth.nu_ = [0] # single notes

    synth.f_ = []  # frequencies for the notes

    zscore = (maxHz - minHz) / (maxVal - minVal)
    frequencies = []

    for i, value in enumerate(fileList):
        if( (i % notesPerSecond) == 0):
            newVal = value * zscore
            if(newVal > minHz):
                frequencies.append(newVal)
    
    for value in frequencies:
        synth.f_.append(value)

    first = synth.render(songLength)

    temp = synth.f_[::-1]
    synth.f_ = temp 
    synth.d_ = [1]
    synth.nu_ = [1]

    second = synth.render(songLength)
    combined = H(first + second)
    music.core.WS(combined, fileName)

def ComplexConversion(fileList, fileName):
    fileName = os.path.splitext(fileName)[0] + "_complex.wav"

if __name__ == '__main__':
    main()
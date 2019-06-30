# This file takes a CSV file and converts it into MP3

from numpy import genfromtxt
import sys
import csv
import os
import wave

def main():
    if (len(sys.argv) > 1):
        fileName = sys.argv[1]
    else:
        fileName = input('Input the name of the file that you want converted into music: ')

    # Run the program only if the file exists
    if(FileCheck(fileName) == 1):
        convertedFile = ConvertFile(fileName)
        CreateWave(convertedFile, fileName)
        print(convertedFile)


    


# Checks if the file exists 
def FileCheck(fn):
    try:
        open(fn, "r") 
        return 1
    except IOError:
        print ("Error: the file", fn, "does not appear to exist.")
        return 0

# Formats the csv file in the case of strange formats
def formatFile(fileName):
    cleanFile = fileName.clean()
    return cleanFile


# This function takes the file and converts it to a numpy array
def ConvertFile(fileName):
    fileArray = genfromtxt(str(fileName), delimiter=',', dtype=None, encoding=None)
    return fileArray

# This function takes the numpy array and converts it into a wav file
def CreateWave(fileArray, fileName):
    waveFile = (os.path.splitext(fileName)[0] + ".wav")

    noise_output = wave.open(waveFile, 'w')
    noise_output.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))

    noise_output.close()

if __name__ == '__main__':
    main()
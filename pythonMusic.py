# This file takes a CSV file and converts it into MP3

from numpy import genfromtxt
from midi2audio import FluidSynth 

from pyknon.genmidi import Midi
from pyknon.music import NoteSeq
from pyknon.music import Note 
from pyknon.music import Rest

import sys
import csv
import os
import wave
import random
import struct

def main():
    if (len(sys.argv) > 1):
        fileName = sys.argv[1]
    else:
        fileName = input('Input the name of the file that you want converted into music: ')

    # Run the program only if the file exists
    if(FileCheck(fileName) == 1):
        convertedFile = ConvertFile(fileName)
        CreateMidi(convertedFile, fileName)

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

# This method takes the file and converts it to a numpy array
def ConvertFile(fileName):
    fileArray = genfromtxt(str(fileName), delimiter=',', dtype=None, encoding=None)
    return fileArray

# This method takes the numpy array and converts it into a wav file
def CreateMidi(fileArray, fileName):
    newFileName = (os.path.splitext(fileName)[0] + ".midi") 

    quarter_rest = Rest(0.25)

    # Dicitonary with all pyknon notes
    noteDict = dict(
        C = Note(0), 
        C_sharp = Note(1),
        D = Note(2), 
        D_sharp = Note(3), 
        E = Note(4), 
        F = Note(5), 
        F_sharp = Note(6), 
        G = Note(7), 
        G_sharp = Note(8), 
        A = Note(9) 
        A_sharp = Note(10) 
        B = Note(11) 
    )
    


    for i in range (0, fileArray.shape):
        fileArray[i]
    sequence = NoteSeq([noteDict["C_note"], A_note, quarter_rest, C_note])
    sequence += [C_note, A_note, A_note, A_note, A_note, A_note]

    midi = Midi(1, tempo=120)
    midi.seq_notes(sequence, track=0)
    midi.write(newFileName)

    midiFile = open(newFileName, "r")

# This method converts the midi file into a mp3 or wav
def ConvertMidi(midiFile):
    wavFileName = (os.path.splitext(midiFile.name)[0] + '.wav') 

    fs = FluidSynth()
    fs.midi_to_audio('example.midi', 'example.wav')

if __name__ == '__main__':
    main()
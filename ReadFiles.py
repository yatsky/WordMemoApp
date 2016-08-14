import os
import sys
import cfg

def greetings():


    print 'Hello! Nice to meet you!'

def readfile(FileName):


    if FileName == '':
        FileName = 'MedicalTerms.txt'

    try:
        with open(FileName, 'r') as f:
            raw = f.readlines()
    except IOError:
        print 'File name terribly wrong!'
        sys.exit()
    return raw
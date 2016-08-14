import os
import sys
import cfg


DefaultFileName = 'MediTermsComplete'
def greetings():
    print 'Hello! Nice to meet you!'


def readfile(FileName):


    if FileName == '':
        FileName = 'MediTermsComplete'
        cfg.FileName = FileName

    try:
        with open(FileName, 'r') as f:
            raw = f.readlines()
    except IOError:
        print 'File name terribly wrong!'
        sys.exit()
    return raw

# this module reads(creates) study records
import cfg
import os

def readstudyrecords(FileName, RawTerm):
    cw = os.getcwd()
    srPath = cw + '\\' + FileName + 'StudyRecord'
    
    if not os.path.isfile(srPath):
        with open(FileName + 'StudyRecord', 'w') as f:
            records = ['0'] * len(RawTerm)
            for record in records:
                f.write('%s\n' % record)
                
    with open(FileName + 'StudyRecord', 'r') as f:
        records = f.readlines()
    return records
# this module reads(creates) study records
import cfg
import os

def readstudyrecords(FileName, RawTerm):
    cw = os.getcwd()
    directory = os.path.join(os.getcwd(), 'StudyRecords')
    
    srPath = os.path.join(directory, FileName + 'StudyRecord')
    # print srPath
    if not os.path.isfile(srPath):
        # with open(FileName + 'StudyRecord', 'w') as f:
        with open(srPath, 'w') as f:
            records = ['0'] * len(RawTerm)
            for record in records:
                f.write('%s\n' % record)
                
    # with open(FileName + 'StudyRecord', 'r') as f:
    with open(srPath, 'r') as f:
        records = f.readlines()
    return records
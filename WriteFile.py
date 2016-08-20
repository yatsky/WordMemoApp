# this module writes your study records
import cfg
import os

def WriteFile(FileName, records):


    cw = os.getcwd()
    directory = os.path.join(os.getcwd(), 'StudyRecords')
    
    srPath = os.path.join(directory, FileName + 'StudyRecord')

    with open(srPath, 'w') as f:
        records = [str(i) for i in records]
        for line in records:
            f.write(line + '\n')
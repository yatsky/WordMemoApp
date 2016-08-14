# this module writes your study records
import cfg

def WriteFile(FileName, records):


    with open(FileName + 'StudyRecord', 'w') as f:
        records = [str(i) for i in records]
        for line in records:
            f.write(line + '\n')
# this module reads(creates) study records
import cfg
import os

def readstudyrecords(RawTerm):
	cw = os.getcwd()
	srPath = cw + '\\' + 'StudyRecord'
	
	if not os.path.isfile(srPath):
		with open('StudyRecord', 'w') as f:
			records = ['0'] * len(RawTerm)
			for record in records:
				f.write('%s\n' % record)
				
	with open('StudyRecord', 'r') as f:
		records = f.readlines()
	return records
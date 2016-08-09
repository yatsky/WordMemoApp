import re
import os

# this module do as follows
# 0. greetings
# 1. read(or create) study record file
# 2. ask user to provide term pool
# 3. read term pool
# 4. ask user to select study mode
AuthorInfo = ['Author Name: Thomas Wang', 'email: wyatsky@gmail.com',
	'facebook: wyatsky@gmail']
def Greetings():
	for info in AuthorInfo:
		print info
	print '''Welcome to this little vocabulary builder program!\n
I hope you find it useful and enjoyable!\n
Please let me know if you have any questions or want to add 
any awsome features.\n
Enjoy learning!\n'''
	
def ReadStudyRecord():
	cw = os.getcwd()
	srPath = cw + '\\' + 'StudyRecord'
	
	if not os.path.isfile(srPath):
		StudyRecord = open('StudyRecord', 'w')
		records = [0] * len(raw)
		# write records to file
		for record in records:
			StudyRecord.write('%s\n' % record)
		StudyRecord.close()
		
	with open('StudyRecord', 'r') as f:
		records = f.readlines()
	return records

def ReadTermPool():
	TermPool = raw_input('''Now please give me your term pool name.\n
The default term pool is \'MedicalTerms.txt\' provided by Lily Wang
and edited by Thomas Wang.\nYou can hit Enter for that one.''')
	if TermPool == '':
		TermPool = 'MedicalTerms.txt'
	with open(TermPool) as f:
		raw = f.readlines()
	return raw
	
def ModeSelection():
	mode = raw_input('Please select study mode.\nEnglish or Chinese?\n')
	if mode == '':
		mode = 'English'
	mode = mode.upper()
	if mode not in ['ENGLISH', 'CHINESE']:
		print 'We don\'t have this mode!\nPlease select again.\n'
		mode = ModeSelection() # this is very important because without 
		# this operation, the mode would value won't change		
	return mode


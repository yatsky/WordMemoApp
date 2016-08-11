import os
import cfg

def greetings():
	print 'Hello! Nice to meet you!'

def readfile(FileName):
	if FileName == '':
		FileName = 'MedicalTerms.txt'
	with open(FileName, 'r') as f:
		raw = f.readlines()
	return raw
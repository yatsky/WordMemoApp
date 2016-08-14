import re
import os

def ReadTermPool(FileName = ''):
    if FileName == '':
        FileName = 'MedicalTerms_ANSI.txt'
    with open(FileName, 'r') as f:
        raw = f.readlines()
    return raw

def ReadStudyRecord():
    cw = os.getcwd()
    srPath = cw + '\\' + 'StudyRecord'
    
    if not os.path.isfile(srPath):
        StudyRecord = open('StudyRecord', 'w')
        records = ['0'] * len(raw)
        # write list to file
        for record in records:
            StudyRecord.write('%s\n' % record)
        StudyRecord.close()
    with open('StudyRecord', 'r') as f:
        records = f.readlines()
    return records
    
def SliceTerms(raw):
    for line in raw:
        newline = line.rstrip()
        if not re.search('\w', newline):
            continue
        terms.append(newline)
        EnglishTerms.append(re.findall('[(\w].+[\w )]', newline)[0])
        ChineseTerms.append(re.findall('[^\w (),].+', newline)[0])
    return terms, EnglishTerms, ChineseTerms

def Selection(records, target):
    PosList = []
    records = [int(i) for i in records] #convert str list to int
    for i in range(len(records)):
        if records[i] < target:
            PosList.append(i) # term position in original records
    return PosList

def MainTest(QuestionList, AnswerList, PosList): #can be EnglishTerms or ChineseTerms
    for i in PosList:
        print QuestionList[i]
        answer = raw_input('Do you know this word?\n(Please type \'quit\' to quit.)\n')
        answer = answer.upper()
        check = AnswerList[i].strip()
        check = check.upper()
        if answer == check:
            records[i] = str(int(records[i]) + 1)
            print 'You remembered', QuestionList[i], records[i], 'time(s)!\n'
        elif answer == 'QUIT':
            print 'Remember to study daily!'
            break
        else:
            print 'Either you don\'t remember or your spelling needs some work!'
            print 'Peek the meaning!\n', AnswerList[i], '\n'

def WriteStudyRecord(records):
    with open('StudyRecord', 'w') as f:
        for record in records:
            record = record.rstrip()
            f.write('%s\n' % record)
            
records = []
terms = []
EnglishTerms = []
ChineseTerms = []

FileName = raw_input('Please input term pool name:\n')
raw = ReadTermPool(FileName)
records = ReadStudyRecord()
terms, EnglishTerms, ChineseTerms = SliceTerms(raw)
target = int(raw_input('input a integer number to set today\'s target.\n')) # default input is float!!!
PosList = Selection(records, target)
mode = raw_input('English mode or Chinese mode?\n')
if mode == 'English':
    MainTest(EnglishTerms, ChineseTerms, PosList)
elif mode == 'Chinese':
    MainTest(ChineseTerms, EnglishTerms, PosList)
else:
    print 'Wrong answer!'
    
WriteStudyRecord(records)
    

# this is the main program
import cfg, ReadFiles, ReadStudyRecords, checknumber, makeQAlist, test, counter, WriteFile

ReadFiles.greetings()
cfg.FileName = raw_input('Please give me your file name.\n')
cfg.RawTerms = ReadFiles.readfile(cfg.FileName)
cfg.records = ReadStudyRecords.readstudyrecords(cfg.RawTerms)
cfg.records = [int(i) for i in cfg.records]
for i in range(max(cfg.records) + 1):
    if i in cfg.records:
        print cfg.records.count(i), 'words remembered %s times.\n' %i

cfg.mode = raw_input('Please set your mode.\nThe default setting is Chinese.\n')
cfg.mode = cfg.mode.upper()

checknumber.is_number()
checknumber.is_big()

cfg.dict, cfg.QuestionList, cfg.AnswerList, cfg.EnglishTerms, cfg.ChineseTerms = \
    makeQAlist.makeQAlist(cfg.RawTerms, cfg.target, cfg.records, cfg.mode)
# print cfg.dict
cfg.TestFlag, cfg.QuestionIfCorrect = test.test(cfg.dict)

while True:
    if cfg.QuestionIfCorrect == 'QUIT':
        WriteFile.WriteFile(cfg.records)
        print 'Goodbye!'
        break

    if cfg.TestFlag:
        cfg.records = counter.counter(cfg.mode, cfg.records, cfg.TestFlag)
        cfg.TestFlag = False
    cfg.TestFlag, cfg.QuestionIfCorrect = test.test(cfg.dict)
	
# print cfg.records

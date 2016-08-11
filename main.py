# this is the main program
import cfg, ReadFiles, ReadStudyRecords, makeQAlist, test, counter, WriteFile

ReadFiles.greetings()
cfg.FileName = raw_input('Please give me your file name.')
cfg.RawTerms = ReadFiles.readfile(cfg.FileName)
cfg.records = ReadStudyRecords.readstudyrecords(cfg.RawTerms)
cfg.records = [int(i) for i in cfg.records]
cfg.mode = raw_input('Please set your mode.\nThe default is English.\n')
cfg.mode = cfg.mode.upper()
cfg.target = int(raw_input('Please set your target today.'))


cfg.dict, cfg.QuestiionList, cfg.AnswerList, cfg.EnglishTerms, cfg.ChineseTerms = makeQAlist.makeQAlist(cfg.RawTerms, cfg.target, cfg.records, cfg.mode)
# print cfg.dict
cfg.TestFlag, cfg.QuestionIfCorrect = test.test(cfg.dict)

while True:
	if cfg.QuestionIfCorrect == 'QUIT':
		WriteFile.WriteFile(cfg.records)
		print 'Goodbye!'
		break
		
	cfg.TestFlag, cfg.QuestionIfCorrect = test.test(cfg.dict)
	if cfg.TestFlag:
		cfg.records = counter.counter(cfg.mode, cfg.records, cfg.TestFlag)
		cfg.TestFlag = False

	
# print cfg.records

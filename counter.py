# this module records your successful attempts

import cfg

def counter(mode, records, flag):
	if flag:
		if mode == 'ENGLISH':
			inde = cfg.EnglishTerms.index(cfg.QuestionIfCorrect)
			#print inde
			#print cfg.QuestionIfCorrect
			records[inde] = records[inde] + 1
		else:
			#print mode
			inde = cfg.ChineseTerms.index(cfg.QuestionIfCorrect)
			records[inde] = records[inde] + 1
			
			
	return records
		
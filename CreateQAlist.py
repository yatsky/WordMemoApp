# this module creates terms list according to target number user gives
# 1. ask user to set a target number
# 2. create a new list to record position information of words
def CreateQAlist(records, mode, EnglishTerms, ChineseTerms):
    target = int(raw_input('Please give your target number.\n'))
    # go through each record in records and compare it with target
    QuestionList = []
    AnswerList = []
    if mode == 'ENGLISH':
        for i in range(len(records)):
            if int(records[i]) < int(target): # important to add int before target
                QuestionList.append(EnglishTerms[i])
                AnswerList.append(ChineseTerms[i])
    else:
        for i in range(len(records)):
            if int(records[i]) < int(target):
                QuestionList.append(ChineseTerms[i])
                AnswerList.append(EnglishTerms[i])

    return QuestionList, AnswerList

import ReadFiles, SliceTerms, CreateQAlist, RandomSelection, tester

print ReadFiles.Greetings()
raw = ReadFiles.ReadTermPool()
records = ReadFiles.ReadStudyRecord(raw)
mode = ReadFiles.ModeSelection()
EnglishTerms = []
ChineseTerms = []
EnglishTerms, ChineseTerms = SliceTerms.SliceTerms(raw, EnglishTerms, ChineseTerms)
QuestionList, AnswerList = CreateQAlist.CreateQAlist(records, mode, EnglishTerms, ChineseTerms)
question, answer = RandomSelection.RandomSelection(QuestionList, AnswerList)

while True:
    test = tester.tester(records, question, answer)
    if test:
        records[QuestionList.index(question)] = int(records[QuestionList.index(question)]) + 1
        print 'That\'s right!\n','You remembered', question, records[QuestionList.index(question)], 'time(s)!\n'
    else:
        print 'either you don\'t know this word, or you need improve your spelling!\n'
    question, answer = RandomSelection.RandomSelection(QuestionList, AnswerList)

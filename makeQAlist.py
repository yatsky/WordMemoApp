# this module slice terms into english and chinese groups
import cfg
import re

def makeQAlist(RawTerms, target, records, mode):
    EnglishTerms = []
    ChineseTerms = []
    QuestionList = []
    AnswerList = []
    for line in RawTerms:
        line = line.strip()
        if not re.search('\w', line):
            continue
        # EnglishTerms.append(re.findall('[(\w].+[\w )]', line)[0].strip())
        # ChineseTerms.append(re.findall('[^\w (),].+', line)[0].strip())
        EnglishTerms.append(re.match(r'([/.\-()\' \w]+)([^\w]+.+)', line).group(1).strip())
        ChineseTerms.append(re.match(r'([/.\-()\' \w]+)([^\w]+.+)', line).group(2).strip())

    mode = mode.upper()
    if mode == 'ENGLISH':
        for i in range(len(records)):
            if records[i] < target:
                QuestionList.append(EnglishTerms[i])
                AnswerList.append(ChineseTerms[i])
    else:
        for i in range(len(records)):
            if records[i] < target:
                QuestionList.append(ChineseTerms[i])
                AnswerList.append(EnglishTerms[i])
    adict = dict(zip(QuestionList, AnswerList))
    return adict, QuestionList, AnswerList, EnglishTerms, ChineseTerms
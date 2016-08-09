# this module randomly select word from term list
# with recorded successful times less than target number
# 3. randomly select from these selected words
# 4. return a term and its answer
import  random
def RandomSelection(QuestionList, AnswerList):
    # print random.choice(QuestionList)
    question = random.choice(QuestionList).rstrip()
    answer = AnswerList[QuestionList.index(question)].rstrip()
    return question, answer

# this module tests whether the answer is correct
import sys
def tester(question, answer):
    print question
    print answer
    UserAnswer = raw_input('Do you know this word?\n')
    UserAnswer = UserAnswer.upper()
    if UserAnswer == answer.upper():
        return True
    elif UserAnswer == 'QUIT':
        sys.exit(0)
    else:
        return False

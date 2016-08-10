# this module tests whether the answer is correct
import sys
def tester(records, question, answer):
    print question
    print answer
    UserAnswer = raw_input('Do you know this word?\n')
    UserAnswer = UserAnswer.upper()
    if UserAnswer == answer.upper():
        return True
    elif UserAnswer == 'QUIT':
        print 'Goodbye!'
        with open('StudyRecord', 'w') as f:
            for record in records:
                # record = record.rstrip()
                f.write('%s\n' % record)
        sys.exit(0)
    else:
        return False

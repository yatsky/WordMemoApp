# this is the test module
import cfg
import random

def test(QAdict):
	question = random.choice(QAdict.keys())
	answer = QAdict.get(question)
	answer = answer.upper()
	UserAnswer = raw_input('Do you know this word?\n%s\n' % question)
	UserAnswer = UserAnswer.upper()
	if UserAnswer == answer:
		print 'You nailed it!\n'
		return True, question
	elif UserAnswer == 'QUIT':
		return False, 'QUIT'
	else:
		print 'Either you don\'t remember or your spelling needs more work!\n'
		print 'The correct answer is: %s\n' % answer
		return False, None
	# print random.choice(QAdict.keys())
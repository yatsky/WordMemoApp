import re

# this module slices the terms list into
# an English list and a Chinese list
# global var EnglishTerms, ChineseTerms
def SliceTerms(raw, EnglishTerms, ChineseTerms): # both eng and chi terms lists are empty
	for line in raw:
		line = line.strip()
		if not re.search('\w', line):
			continue
		EnglishTerms.append(re.findall('[(\w].+[\w )]', line)[0])
		ChineseTerms.append(re.findall('[^\w (),].+', line)[0])
	return EnglishTerms, ChineseTerms
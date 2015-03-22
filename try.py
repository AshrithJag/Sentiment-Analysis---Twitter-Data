import re

filetmp = open("AFINN-111.txt")
scores = {}
for line in filetmp:
  term, score  = line.split("\t")
  scores[term] = int(score)


score = 0
line = u'Desperate'
for term in scores:
	if re.match(term,line):
		score += scores[term]

print score

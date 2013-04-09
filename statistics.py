import classifier as c
import operator
import math

nb, vocab = c.train()
prob = nb[1]
wordprob=[[],[]]
wordprob[0] = sorted(prob[0].iteritems(), key=operator.itemgetter(1))
wordprob[1] = sorted(prob[1].iteritems(), key=operator.itemgetter(1))
wordprob[0].reverse()
wordprob[1].reverse()

#for i in range(0, 2):
#	print "------------"
#	for j in range(1, 20):
#		print wordprob[i][j]

logratio = [{},{}]
for word in vocab:
	for i in range(0, 2):
		logratio[0][word]=math.log(prob[0][word])-math.log(prob[1][word])
		logratio[1][word]=math.log(prob[1][word])-math.log(prob[0][word])
logrank = [[],[]]
logrank[0] = sorted(logratio[0].iteritems(), key=operator.itemgetter(1))
logrank[1] = sorted(logratio[1].iteritems(), key=operator.itemgetter(1))
for i in range(0, 2):
	print "--------------"
	logrank[i].reverse()
	for j in range(1, 21):
		print logrank[i][j]

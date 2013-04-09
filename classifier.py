import sys
import math
trainfile = sys.argv[1]
testfile = sys.argv[2]

path = "../"

trlist = [line.strip() for line in open(path+"split/"+trainfile)]
telist = [line.strip() for line in open(path+"split/"+testfile)]

def train():
	vcount = 0
	vocab = {}
	pi = {0:0, 1:0}# 0 for con, 1 for lib
	text = [{},{}]
	prob = [{},{}]
	wcount = [0,0]
	for item in trlist:
		words = [line.strip() for line in open(path+"data/"+item)]
		for word in words:
			word = word.lower()
			if word in vocab:
				vocab[word]+=1
			else:
				vcount+=1
				vocab[word]=1
			if item.startswith("con"):
				wcount[0]+=1
				if word in text[0]:
					text[0][word]+=1
				else:
					text[0][word]=1
			else:
				wcount[1]+=1
				if word in text[1]:
					text[1][word]+=1
				else:
					text[1][word]=1
		if item.startswith("con"):
			pi[0]+=1
		else:
			pi[1]+=1
	for i in range(0, 2):
		pi[i]=float(pi[i])/float(len(trlist))
		for item in vocab:
			if item in text[i]:
				nk=text[i][item]
			else:
				nk=0
			prob[i][item]=float(nk+1)/float(wcount[i]+vcount)
	return ((pi, prob), vocab)
def classify(nb, vocab):
	pi = nb[0]
	prob = nb[1]
	for item in telist:
		result=[0, 0]
		words = [line.strip() for line in open(path+"data/"+item)]
		for word in words:
			word = word.lower()
			if word in vocab:
				for i in range(0, 2):
					result[i]+=math.log(prob[i][word], 2)
		for i in range(0, 2):
			result[i]+=math.log(pi[i])
		if result[0]>result[1]:
			print item+" C"
		else:
			print item+" L"

nb, vocab = train()
classify(nb, vocab)

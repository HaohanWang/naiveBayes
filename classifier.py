import sys
import math
import operator
trainfile = sys.argv[1]
testfile = sys.argv[2]

path = "../"

trlist = [line.strip() for line in open(path+"split/"+trainfile)]
telist = [line.strip() for line in open(path+"split/"+testfile)]
N = 50
F = 2  
M = 8827 
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
	#ignore the top count
	ignore = {}
	ilist = sorted(vocab.iteritems(), key=operator.itemgetter(1))
	ilist.reverse()
	for i in range(0, N+1):
		iword = ilist[i][0]
		ignore[iword]=ilist[i][1]
		for j in range(0, 2):
			if iword in text[j]:
				wcount[j]-=text[j][iword]
	vcount-=N
	#ignore the frequency	
	for item in vocab:
		if vocab[item]<=F:
			if item not in ignore:
				ignore[item]=vocab[item]
				vcount-=vocab[item]
				for j in range(0, 2):
					if item in text[j]:
						wcount[j]-=text[j][item]
	p = float(M)/float(vcount)
	q = getQ()
	for i in range(0, 2):
		pi[i]=float(pi[i])/float(len(trlist))
		for item in vocab:
			if item in text[i] and item not in ignore:
				nk=text[i][item]
			else:
				nk=0
			#prob[i][item]=float(nk+1)/float(wcount[i]+vcount)
			prob[i][item]=(float(nk)/float(wcount[i]))*(float(wcount[i])/(float(wcount[i])+M))+(float(M)/float(wcount[i]+M))*q[item]
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

def getQ():
	q={}
	wcount=0
	vocab = {}
	for item in trlist:
		words = [line.strip() for line in open(path+"data/"+item)]
		for word in words:
			word = word.lower()
			wcount+=1
			if word in vocab:
				vocab[word]+=1
			else:
				vocab[word]=1
	for item in vocab:
		q[item]=float(vocab[item]+1)/float(wcount+len(vocab))
#	print q
	return q

nb, vocab = train()
classify(nb, vocab)

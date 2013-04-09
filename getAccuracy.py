import math
text = [line.strip() for line in open("report")]

freq = []
for line in text:
	if line.startswith("** Classification accuracy"):
		word = line.split()
		freq.append(float(word[-1]))
s = 0.0
avg = 0.0
dev = 0.0
for i in freq:
	s+=i
avg = s/len(freq)
ds = 0.0
for i in freq:
	ds+=pow((i-avg), 2)
ds=ds/len(freq)
dev=math.sqrt(ds)
print "avg "+str(avg)
print "dev "+str(dev)

#!/bin/sh

declare tr=('split1.train' 'split2.train' 'split3.train' 'split4.train' 'split5.train' 'split6.train' 'split7.train' 'split8.train' 'split9.train' 'split10.train')
declare te=('split1.test' 'split2.test' 'split3.test' 'split4.test' 'split5.test' 'split6.test' 'split7.test' 'split8.test' 'split9.test' 'split10.test')
declare re=('result1' 'result2' 'result3' 'result4' 'result5' 'result6' 'result7' 'result8' 'result9' 'result10')

for ((i=0;i<=9;i++))
do
	python classifier.py ${tr[$i]} ${te[$i]} > ${re[$i]}
	perl eval.pl < ${re[$i]} 
done

# coding=UTF8
# encoding=utf8

import numpy as np
import sklearn.preprocessing
import csv
import sys

reload(sys)
sys.setdefaultencoding('utf8')

target='評價'

freq={}

with open('%s_scaled.csv'%target, 'rb') as f:
	reader = csv.reader(f)
	next(reader, None)
	next(reader, None)
	for row in reader:
		freq[row[1]]=int(float(row[2])*10000)+1

s = ''
for key, freq in freq.iteritems():
	for i in range(freq):
		s+=' '+key

with open('%s_wordcloud.txt', 'wb') as f:
	f.write(s)
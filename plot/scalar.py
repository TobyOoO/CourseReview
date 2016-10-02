# coding=UTF8
# encoding=utf8

import numpy as np
import sklearn.preprocessing
import csv
import sys

reload(sys)
sys.setdefaultencoding('utf8')

arr = []
output = []
headers = ['Source','Target','Weight','Freq','Semantic']
freq = {}

target = '上課'

with open('vocab.csv', 'rb') as f:
	for row in csv.reader(f):
		freq[row[0]]=int(row[1])

with open('%s.csv'%target, 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		output.append([target,row[0]])
		arr.append(float(row[1]))

scalar = sklearn.preprocessing.MinMaxScaler()
scalar.fit(np.array(arr).reshape(-1,1))
result = scalar.transform(np.array(arr).reshape(-1,1)).tolist()

print(result)

with open('%s_scaled.csv'%target, 'wb') as f:
	f.write(','.join(headers)+'\n')
	for i, row in enumerate(output):
		s = '{0},{1},{2},{3},\n'.format(row[0], row[1], result[i][0],freq[row[1]])
		f.write(s)
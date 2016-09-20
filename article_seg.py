# coding=UTF8
# encoding=utf8

import jieba
import sqlite3
import re
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def read_data():
	jieba.set_dictionary('dict.txt.big')
	stop1 = u"[★ηΨρμωδ\"，。、「」（）\(\)\.【】『』：；・．～？＝＼／！＠\@＄\$％＆\&\%\-\/\\\>\<\~\:\,\[\]\?\!\=\+＋\*＊]*"
	stop2 = "http[a-zA-Z\.\:\/\-\?\#]*"
	stop3 = "[0-9\.]*"
	result = []

	word_cate = {}
	color_dict = {}
	
	'''
	#read color dict
	header = True
	f = codecs.open('category_color.csv', 'r', encoding='utf8')
	for row in f:
		if(header):
			header = False
			continue
		row = row.replace('"', '').split(',')
		color_dict[row[0]] = None

	arr = color_dict.keys()
	cNorm  = colors.Normalize(vmin=-0.1, vmax=1)
	scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=plt.get_cmap('nipy_spectral') )
	for i in range(len(arr)):
		color = scalarMap.to_rgba(i/float(len(arr)))
		color_dict[arr[i]] = chroma.Color(color, format="RGB")
		print(arr[i]+', '+str(color_dict[arr[i]]))
	'''

	#read article
	conn = sqlite3.connect('ptt_course.db')
	c = conn.cursor()


	for i, article in enumerate(c.execute('SELECT Content FROM Article_Directory WHERE Category = "評價" AND Content not null')):
		print('reading %i' % i)
		result += ['UNK']
		text = article[0].replace('  ', '')
		text = re.sub(stop1, "", text)
		text = re.sub(stop2, "_URL_", text)
		text = re.sub(stop3, "", text)
		seg_list = jieba.lcut(text, cut_all=False)
		word_list = []
		for seg in seg_list:
			'''
			if(len(seg) == 1):
				continue
			'''
			word_list.append(seg)
		result += word_list

	with open('article_seg.txt', 'wb') as f:
		f.write(' '.join(result))

read_data()
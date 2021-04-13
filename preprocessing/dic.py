import csv

def get_dic():
	dic_kkma={}
	dic_mecab={}
	dic_okt={}
	i=0

	with open('data_frequency/kkma_frequency.txt', 'r') as kkma:
		for word in kkma:
			word=(word.split(' '))
			dic_kkma[word[0]]=i
			i+=1

	i=0
	with open('data_frequency/mecab_frequency.txt', 'r') as mecab:
		for word in mecab:
			word=(word.split(' '))
			dic_mecab[word[0]]=i
			i+=1

	i=0
	with open('data_frequency/okt_frequency.txt', 'r') as okt:
		for word in okt:
			word=(word.split(' '))
			dic_okt[word[0]]=i
			i+=1

	return dic_kkma, dic_mecab, dic_okt

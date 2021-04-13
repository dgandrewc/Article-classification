from konlpy.tag import Okt, Kkma, Mecab
import csv

okt=Okt()
kkma=Kkma()
mecab=Mecab()

dic1={}
dic2={}
dic3={}

count=0
okt_news=open('token_news/okt_news', 'w')
kkma_news=open('token_news/kkma_news', 'w')
mecab_news=open('token_news/mecab_news', 'w')

with open('cleaned_data.csv', newline='', encoding='euc-kr') as csvfile:
	text=csv.reader(csvfile, delimiter=',')
	for title in text:
		news_title=okt.nouns(title[0])
		for word in news_title:
			okt_news.write(word+' ')
		'''
			if word not in dic1.keys():
				dic1[word]=1
			else:
				dic1[word]+=1
		'''
		okt_news.write(','+str(title[1])+'\n')
		news_title=kkma.nouns(title[0])
		for word in news_title:
			kkma_news.write(word+' ')
		'''
			if word not in dic2.keys():
				dic2[word]=1
			else:
				dic2[word]+=1
		'''
		kkma_news.write(','+str(title[1])+'\n')
		news_title=mecab.nouns(title[0])
		for word in news_title:
			mecab_news.write(word+' ')
		'''
			if word not in dic3.keys():
				dic3[word]=1
			else:
				dic3[word]+=1
		'''
		mecab_news.write(','+str(title[1])+'\n')
		count+=1		
		print(count)

'''
dic1=sorted(dic1.items(), key=lambda x: x[1], reverse=True)
with open('data_frequency/okt_frequency.txt', 'w') as datafile:
	for data in dic1:
		datafile.write(data[0]+' '+str(data[1])+'\n')

dic2=sorted(dic2.items(), key=lambda x: x[1], reverse=True)
with open('data_frequency/kkma_frequency.txt', 'w') as datafile:
	for data in dic2:
		datafile.write(data[0]+' '+str(data[1])+'\n')

dic3=sorted(dic3.items(), key=lambda x: x[1], reverse=True)
with open('data_frequency/mecab_frequency.txt', 'w') as datafile:
	for data in dic3:
		datafile.write(data[0]+' '+str(data[1])+'\n')
'''
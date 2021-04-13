import dic

dic_kkma, dic_mecab, dic_okt=dic.get_dic()
kkma_news=open('token_news/kkma_news.txt', 'r')
mecab_news=open('token_news/mecab_news.txt', 'r')
okt_news=open('token_news/okt_news.txt', 'r')





number_news_kkma=open('number_news/number_news_kkma.txt', 'w')
number_news=str('')
for news in kkma_news:
	news=news.split(',')
	if(news[0] is not ''):
		text_news=news[0].split(' ')
		for word in text_news:
			number_news+=str(dic_kkma[word])+' '
		number_news+=','+news[1]
number_news_kkma.write(number_news)

count=0
number_news_mecab=open('number_news/number_news_mecab.txt', 'w')
number_news=str('')
for news in mecab_news:
	news=news.split(',')
	if(news[0] is not ''):
		text_news=(news[0].strip()).split(' ')
		for word in text_news:
			if(word is ''):
				continue
			number_news+=str(dic_mecab[word])+' '
		number_news+=','+news[1]
	count+=1
	print(count)
number_news_mecab.write(number_news)

number_news_okt=open('number_news/number_news_okt.txt', 'w')
number_news=str('')
for news in okt_news:
	news=news.split(',')
	if(news[0] is not ''):
		text_news=(news[0].strip()).split(' ')
		for word in text_news:
			number_news+=str(dic_okt[word])+' '
		number_news+=','+news[1]
number_news_okt.write(number_news)

import random

def set_data():
	data=open('data/number_news/number_news_kkma.txt', 'r')
	x=[]
	y=[]
	temp=list()

	for dat in data:
		dat=dat.split(' ,')
		words=dat[0].split(' ')
		for word in words:
			temp.append(int(word))
		x.append(temp)
		y.append(int(dat[1][0]))
		temp=list()
	
	bind=[[x, y] for x, y in zip(x, y)]
	random.shuffle(bind)
	x=[n[0] for n in bind]
	y=[n[1] for n in bind]
	return x[:500000], y[:500000], x[500000:], y[500000:]

if __name__=='__main__':
	set_data()
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

f=open('poli.csv', 'w', encoding='euc-kr', newline='')
wr=csv.writer(f)

def findnews(site, category):
	for k in range(1, 12):
		if(k<10):
			stK=k
			k=str('0')+str(k)
		for j in range(1, 31):
			if(j<10):
				stJ=j
				j=str('0')+str(j)
			for i in range(1, 10):
				
				url = "https://news.naver.com/main/list.nhn?mode=LS2D&sid2="+str(site)+"&sid1=100&mid=shm&date=2019"+str(k)+str(j)+"&page="+str(i)
				html = urlopen(url)
				source = html.read()
				html.close()
				soup = BeautifulSoup(source, "html5lib")
				soup=soup.find_all('dt')
				print(url)
				for news in soup:
					if(news.a.string!=None):
						title=str(news.a.string).strip()
						title=title.replace("\r\n|\n\r", "")
						try:
							wr.writerow([title, category])
						except:
							continue;
			j=stJ
		k=stK

#정치
findnews(264, 0)
findnews(265, 0)
findnews(266, 0)
findnews(267, 0)
findnews(268, 0)
findnews(269, 0)
#경제
findnews(258, 1)
findnews(259, 1)
findnews(261, 1)
findnews(771, 1)
findnews(260, 1)
findnews(262, 1)
findnews(310, 1)
findnews(263, 1)
#사회
findnews(249, 2)
findnews(250, 2)
findnews(251, 2)
findnews(754, 2)
findnews(252, 2)
findnews(255, 2)
findnews(356, 2)
findnews(276, 2)
findnews(257, 2)
#생활/문화
findnews(241, 3)
findnews(239, 3)
findnews(240, 3)
findnews(237, 3)
findnews(238, 3)
findnews(376, 3)
findnews(242, 3)
findnews(243, 3)
findnews(244, 3)
findnews(248, 3)
findnews(245, 3)
#세계
findnews(231, 4)
findnews(232, 4)
findnews(233, 4)
findnews(234, 4)
findnews(322, 4)
#IT/과학
findnews(731, 5)
findnews(226, 5)
findnews(227, 5)
findnews(230, 5)
findnews(732, 5)
findnews(283, 5)
findnews(229, 5)
findnews(228, 5)
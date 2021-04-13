# 네이버 뉴스 기사 데이터 분류

### 1. crawling_final.py
##### 2019년 네이버 뉴스기사 수집
##### 정치, 경제, 사회, 생활/문화, 세계, IT/과학 카테고리별로 라벨링
![image](https://user-images.githubusercontent.com/82406128/114529461-ee25c180-9c84-11eb-934d-255c32b76bd4.png)
#
### 2. preprocessing/preprocessing.py
##### 한자 -> 한글 치환
##### 영어, 숫자, 특수문자 제거
![캡처](https://user-images.githubusercontent.com/82406128/114520941-e9f5a600-9c7c-11eb-9f1a-e3e815ef5c73.PNG)
#
### 3. preprocessing/tokenizer.py
##### KKMA, MECAB, OKT 등의 형태소 분석기 사용
##### 분석기와 형태소별 단어 빈도 저장
##### 형태소로 분해된 뉴스 기사 저장
![캡처](https://user-images.githubusercontent.com/82406128/114522014-e6165380-9c7d-11eb-9cf5-ab28295ff6af.PNG)
![캡처](https://user-images.githubusercontent.com/82406128/114527878-6db29100-9c83-11eb-8504-48079d846cee.PNG)
#
### 4. preprocessing/dic.py
##### 이후 인코딩 처리를 위해 단어빈도 순위와 단어를 매칭한 딕셔너리 반환
#
### 5. preprocessing/number_news.py
##### dic.py에서 반환받은 딕셔너리를 이용하여 숫자로 이루어진 뉴스기사 저장
![image](https://user-images.githubusercontent.com/82406128/114529158-a56e0880-9c84-11eb-9049-c9e27de341f6.png) 
#
### 6. set_data.py
##### 데이터 셔플, 학습&평가용 데이터 나누어서 반환
#
### 7. CNN.ipynb/LSTM.ipynb/RCNN.ipynb
##### 문장 패딩 처리, 원 핫 인코딩, 임베딩
##### 이후 간단한 모델로 정확도 측정
##### 약 80%의 정확도 달성
#
##### #CNN
![캡처](https://user-images.githubusercontent.com/82406128/114535881-78712400-9c8b-11eb-9f6b-1cad4409ebbe.PNG)
##### 평가 결과 : [loss : 0.5229010138174692, accuracy : 0.8301788568496704]
![image](https://user-images.githubusercontent.com/82406128/114535508-19131400-9c8b-11eb-8243-9a97fd6168af.png)
#
##### #LSTM
![캡처](https://user-images.githubusercontent.com/82406128/114540091-18c94780-9c90-11eb-865d-0600061ab4dd.PNG)
##### 평가 결과 : [loss : 0.5270308029996911, accuracy : 0.8370682001113892]
#
##### #RCNN
![캡처](https://user-images.githubusercontent.com/82406128/114540229-3d252400-9c90-11eb-925d-80d7aac8193d.PNG)
##### 평가 결과 : [loss : 0.6732165386017915, accuracy : 0.8145400285720825]
import hanja
import csv
import re
import hangul

INPUT_FILE='./each_100thousand.csv'
OUTPUT_FILE='cleaned_data.csv'

write_file = open(OUTPUT_FILE,'w', encoding='euc-kr')
with open(INPUT_FILE, newline='') as csvfile:
	hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
	text=csv.reader(csvfile, delimiter=',')
	for row in text:
		row[0]=hanja.translate(row[0], 'substitution')
		row[0]=hangul.sub('', row[0])
		write_file.write(row[0]+","+row[1]+"\n")
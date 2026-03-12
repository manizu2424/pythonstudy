import csv

def write_csv():
  with open('01_fileControl\\testfold1\\testfold1_data.csv', 'w', encoding='utf-8-sig', newline='') as f:
      writer = csv.writer(f)
      writer.writerow(['이름', '나이', '지역'])
      writer.writerow(['홍길동', 20, '서울'])
      writer.writerow(['Alice', 30, 'New York'])
      writer.writerow(['Bob', 25, 'Los Angeles'])
      writer.writerow(['Charlie', 35, 'Chicago'])
      print ("파일 생성")

# write_csv()

# csv.reader() : csv 파일을 리스트 형태로 읽어오는 함수
def read_csv():
  with open('01_fileControl\\testfold1\\testfold1_data.csv', 'r', encoding='utf-8-sig') as f:
      reader = csv.reader(f)
      lists = list(reader)
      print (lists)
      for row in lists:
          print(row)

# read_csv()

# csv.DictReader() : csv 파일을 딕셔너리 형태로 읽어오는 함수
with open('01_fileControl\\testfold1\\testfold1_data.csv', 'r', encoding='utf-8-sig') as f:
    dic_reader = csv.DictReader(f)
    for row in dic_reader:
        print(row)
        print(row['이름'], row['나이'], row['지역'])
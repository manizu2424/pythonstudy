# 파일 쓰기, 반드시 close() 해줘야 함
def fileWrite1():
  file = open("01_fileControl\\testfold1\\testfold1_test.txt", "w", encoding="utf-8")
  file.write("test 파일 입니다.\n파일 쓰기 연습입니다.")  
  file.close()
  print ("파일 생성")

# 파일 읽기, 반드시 close() 해줘야 함
def fileRead1():
  file = open("01_fileControl\\testfold1\\testfold1_test.txt", "r", encoding="utf-8")
  data = file.read()
  file.close()
  print (data)

# fileWrite1()
# fileRead1()

######################################################
# 파일쓰기 with 구문 사용, 자동으로 close() 해줌
def fileWrite2():
  with open("01_fileControl\\testfold1\\testfold1_test.txt", "w", encoding="utf-8") as f:
      f.write("test 파일 입니다.\n파일 쓰기 연습입니다.")
      print ("파일 생성")

# 파일읽기 with 구문 사용, 자동으로 close() 해줌
def fileRead2():
  with open("01_fileControl\\testfold1\\testfold1_test.txt", "r", encoding="utf-8") as f:
      data = f.read()
      print (data)

# fileWrite2()
fileRead2()

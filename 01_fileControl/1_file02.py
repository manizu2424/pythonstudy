import shutil
import os

#파일, 폴더 생성
''' 파일, 폴더 생성 '''
def filefoldMake():
  if not os.path.exists("01_fileControl\\testfold1"):
      os.makedirs("01_fileControl\\testfold1")
      print ("폴더 생성")
  else:
      print ("testfold1 폴더 있음")

  if not os.path.exists("01_fileControl\\testfold1\\testfold1_test.txt"):
    with open("01_fileControl\\testfold1\\testfold1_test.txt", "w") as f:
        f.write("test")
        print ("파일 생성")
  else:
      print ("testfold1\\testfold1_test.txt 파일 있음")

  if not os.path.exists("01_fileControl\\testfold1\\subfold1"):
      os.makedirs("01_fileControl\\testfold1\\subfold1")
      print ("testfold1\\subfold1 폴더 생성")
  else:
      print ("testfold1\\subfold1 폴더 있음")

  lists = os.listdir("01_fileControl\\testfold1")
  for list in lists:
      print (list)
  print (f"testfold1 목록 개수 : {len(lists)}")
  return lists

# filefoldMake()

#폴더 복사, 폴더안 내용까지 복사
''' 폴더 복사, 폴더안 내용까지 복사 '''
def foldCopy():
  path_from = "01_fileControl\\testfold1"
  path_to = "01_fileControl\\testfold1_1"
  if not os.path.exists(path_to):
      shutil.copytree(path_from, path_to)
      print ("폴더 복사")
  else:
      print ("testfold1_1 폴더 있음")

  lists = os.listdir(path_to)
  for list in lists:
      print (list)
  print (f"testfold1_1 목록 개수 : {len(lists)}")
  return lists

# foldCopy()

#파일 삭제
''' 파일 삭제 '''
def fileDelete():
  path = "01_fileControl\\testfold1_1\\testfold1_test.txt"
  if os.path.exists(path):
      os.remove(path)
      print ("파일 삭제")
  else:
      print ("testfold1_1\\testfold1_test.txt 파일 없음")

  lists = os.listdir("01_fileControl\\testfold1_1")
  for list in lists:
      print (list)
  print (f"testfold1_1 목록 개수 : {len(lists)}")
  return lists

# fileDelete()

#폴더 삭제
''' 폴더 삭제 '''
def foldDelete():
  path = "01_fileControl\\testfold1_1"
  if os.path.exists(path):
      shutil.rmtree(path)
      print ("폴더 삭제")
  else:
      print ("testfold1_1 폴더 없음")

  lists = os.listdir("01_fileControl\\")
  for list in lists:
      print (list)
  print (f"01_fileControl 목록 개수 : {len(lists)}")
  return lists

# foldDelete()

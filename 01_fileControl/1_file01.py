import os
import uuid

if not os.path.exists("01_fileControl\\test1"):
    print ("폴더 없음")
else:
    print ("폴더 있음")

if not os.path.exists("01_fileControl\\test1"):
    os.makedirs("01_fileControl\\test1")
    print ("폴더 생성")

if os.path.exists("01_fileControl\\test1"):
    os.rename("01_fileControl\\test1", f"01_fileControl\\test_{uuid.uuid4()}")
    print ("폴더 이름 변경")

lists = os.listdir("01_fileControl")
for list in lists:
    print (list)
print (f"목록 개수 : {len(lists)}")

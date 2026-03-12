import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"}
response = requests.get(url, headers=headers)
response.raise_for_status()
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
print(soup.find("meta"))          
print(soup.find(attrs={"name":"twitter:card"})) 
print("=="*40)
print(soup.find_all(attrs={"name":"twitter:card"})) 
print("=="*40)
print(soup.meta)                   
print("=="*40)
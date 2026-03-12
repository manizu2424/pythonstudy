import requests

url = "https://www.naver.com"
response = requests.get(url)

print("상태 코드:", response.status_code)

if response.status_code == 200:
  print("정상 응답")
else:
  print("error:", response.status_code)

response.raise_for_status()  # 위 if문 코드와 동일한 기능을 하는 코드
print("정상 응답")
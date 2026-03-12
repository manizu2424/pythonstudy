from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <title>온라인 쇼핑몰</title>
</head>
<body>
<h1>장바구니</h1>
  <div>
    <p id="clothes" class="name" title="라운드티"> 라운드티
      <span class="number"> 25 </span>
      <span class="price"> 29000 </span>
      <span class="menu">  의류 </span>
      <a href="https://www.naver.com"> 바로가기 </a>
    </p>
    <p id="watch" class="name" title="시계"> 시계
      <span class="number"> 28 </span>
      <span class="price"> 32000 </span>
      <span class="menu"> 액세서리 </span>
      <a href="https://www.google.com"> 바로가기 </a>
    </p>
  </div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
def printFind():
  print("**1.\n", soup.find_all("p")) # p 태그를 모두 찾아서 리스트로 반환
  print("=="*40)
  print("**2.\n", soup.find(id="clothes")) # id 속성이 clothes인 요소를 찾아서 반환
  print("=="*40)
  print("**3.\n", soup.find_all(id="clothes")) # id 속성이 clothes인 요소를 모두 찾아서 리스트로 반환
  print("=="*40)
  print("**4.\n", soup.find("p").find("span")) # p 태그를 먼저 찾고, 그 안에서 span 태그를 찾아서 반환
  print("=="*40)
  print("**5.\n", soup.find_all("p")[0].find_all("span")[0]) # p 태그를 모두 찾아서 리스트로 반환한 후, 첫 번째 요소에서 span 태그를 모두 찾아서 리스트로 반환한 후, 첫 번째 요소를 반환
  print("=="*40)
  print("**6.\n", soup.find("span", class_="menu").get_text()) # span 태그 중에서 class 속성이 menu인 요소를 찾아서 텍스트만 반환
  print("=="*40)
  print("**7.\n", soup.find("span", attrs={"class": "menu"}).get_text(strip=True)) # span 태그 중에서 class 속성이 menu인 요소를 찾아서 텍스트만 반환, strip=True 옵션을 사용하여 양쪽 공백 제거
  print("=="*40)
  print("**8.\n", soup.find("span", attrs={"class": "menu"}).text.strip()) # span 태그 중에서 class 속성이 menu인 요소를 찾아서 텍스트만 반환, strip() 메서드를 사용하여 양쪽 공백 제거
  print("=="*40)
  print("**9.\n", soup.find("a")["href"]) # a 태그를 찾아서 href 속성의 값을 반환
  print("=="*40)

# printFind()

def printSelect():
  tag = soup.select("p")
  print("**1.")
  for i in tag:
    print(i)
  print("=="*40)
  print("**2.\n", soup.select("p")) # p 태그를 모두 찾아서 리스트로 반환
  print("=="*40)
  print("**3.\n",soup.select("#clothes")) # id 속성이 clothes인 요소를 찾아서 텍스트만 반환
  print("=="*40)
  print("**4.\n",soup.select(".name")) # class 속성이 name인 요소를 모두 찾아서
  print("=="*40)
  print("**5.\n",soup.select("p > span.price")) # p 태그의 자식 요소 중에서 class 속성이 price인 span 태그를 모두 찾아서 리스트로 반환
  print("=="*40)
  print("**6.\n",soup.select("p > span.menu")) # p 태그의 자식 요소 중에서 class 속성이 menu인 span 태그를 모두 찾아서 리스트로 반환
  print("=="*40)
  print("**7.\n",soup.select("#watch")) # id 속성이 watch인 요소를 찾아서 리스트로 반환
  print("=="*40)
  print("**8.\n",soup.select("div > .menu")) # div 태그의 자식 요소 중에서 class 속성이 menu인 요소를 찾아서 리스트로 반환, div 태그의 자식 요소 중에서 class 속성이 menu인 요소가 없기 때문에 빈 리스트를 반환
  print("=="*40)
  print("**9.\n",soup.select("div .menu")) # div 태그의 자손 요소 중에서 class 속성이 menu인 요소를 찾아서 리스트로 반환, div 태그의 자손 요소 중에서 class 속성이 menu인 요소가 있기 때문에 해당 요소를 포함한 리스트를 반환
  print("=="*40)
  print("**10.\n",soup.select("div .menu")[0].get_text(strip=True)) # div 태그의 자손 요소 중에서 class 속성이 menu인 요소를 찾아서 텍스트만 반환, strip=True 옵션을 사용하여 양쪽 공백 제거
  print("=="*40)
  print("**11.\n",soup.select_one("div .menu").get_text()) # div 태그의 자손 요소 중에서 class 속성이 menu인 요소를 찾아서 텍스트만 반환, select_one() 메서드를 사용하여 첫 번째 요소만 반환
  print("=="*40)

# printSelect()

tag = soup.find("a")
print("**1.\n", tag.parent) # a 태그의 바로 위 부모 요소를 찾아서 반환
print("=="*40)
print("**2.\n", list(tag.parents)) # a 태그의 모든 부모 요소를 찾아서 리스트로 반환
print("=="*40)
print("**3.\n")
for i in tag.parents:
  print(i)
  print("***"*20) # a 태그의 모든 부모 요소를 찾아서 반복문으로 출력
print("=="*40)
print("**4.\n", soup.find("span").find_next_sibling("span")) # a 태그의 바로 다음 형제 요소를 찾아서 반환, a 태그의 바로 다음 형제 요소가 없기 때문에 None을 반환
print("=="*40)


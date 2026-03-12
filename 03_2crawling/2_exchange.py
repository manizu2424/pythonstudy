import requests
from bs4 import BeautifulSoup

C_from = "USD"
url = f"https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_{C_from}KRW"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 환율 정보 가져오기
# rate_info = []
# rate = soup.select("p.no_today span")
# for r in rate:
#   rate_info.append(r.text)
# rate_info = "".join(rate_info)
# print(rate_info)
# print("=" * 50)
 
# today = soup.select_one("p.no_today").get_text(strip=True)
# print(today)
# print("=" * 50)

country_info = soup.find("div", class_="h_company").find("h2").get_text(strip=True)
print(country_info)
print("=" * 50)


rate_info = soup.find("p", class_="no_today").get_text(strip=True)
print(rate_info)
print("=" * 50)

c_icon = soup.find("span", class_="ico")
if c_icon:
    if "up" in c_icon["class"]:
        c_sign = "▲"
    elif "down" in c_icon["class"]:
        c_sign = "▼"
    else:
        c_sign = ""
        
exday_info = soup.find("p", class_="no_exday").get_text(strip=True).replace("전일대비", "").strip()
print(c_sign, exday_info)
print("=" * 50)

print(f"{country_info} {C_from} 실시간 환율: {rate_info} | 전일대비 {c_sign} {exday_info}")
print("=" * 50)
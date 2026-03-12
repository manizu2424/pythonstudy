import pandas as pd

url = "https://finance.naver.com/marketindex/exchangeList.naver"

# 환율 정보 가져오기
exchange = pd.read_html(url, encoding="euc-kr", flavor="html5lib")

df = exchange[0]
print(df)
print("=" * 50)

# Save DataFrame to CSV file
df.to_csv('03_2crawling\\1_exchange.csv', index=False, encoding='utf-8-sig') 
print("DataFrame saved to CSV file.")
print("=" * 50)

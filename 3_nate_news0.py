import requests
from bs4 import BeautifulSoup
from newspaper import Article
import pandas as pd
from datetime import datetime

# cat0 = "subsection"
# cat1 = "its03"
# cat2 = "n0604"
# date = "20260309"
# page = "1"
# https://news.nate.com/recent?cate=its&mid=n0601&type=c&date=20260309&page=1 최신뉴스
# https://news.nate.com/subsection?cate=its03&mid=n0604&type=c&date=20260309&page=2 컴퓨터/인터넷 


def make_urllist(cats, date, page):
    cat0, cat1, cat2 = cats
    url_list = []
    for i in range(1, page + 1):
        url = f"https://news.nate.com/{cat0}?cate={cat1}&mid=n{cat2}&type=c&date={date}&page={i}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
        }
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "lxml")
        # news_list = soup.find_all("a", class_="lt1")
        news_list = soup.select("a.lt1")
        for link in news_list:
            url_list.append(f"https:{link.get('href')}")
    return url_list


rec = ("recent", "its", "0601")
sci = ("subsection", "its01", "0602")
dig = ("subsection", "its02", "0603")
com = ("subsection", "its03", "0604")
med = ("subsection", "its04", "0605")
gam = ("subsection", "its05", "0606")
gen = ("subsection", "its06", "0607")
url_list = make_urllist(rec, "20260309", 1)
# print(url_list)
print("뉴스 기사의 개수 : ", len(url_list))


idx2word = {
    "0601": "최신뉴스",
    "0602": "과학",
    "0603": "디지털",
    "0604": "컴퓨터/인터넷",
    "0605": "뉴미디어/통신",
    "0606": "게임",
    "0607": "IT/과학일반"
}

def make_data(url_list, cat1, cat2):
    title_list = []
    text_list = []
    source_url_list = []
    for url in url_list:
        article = Article(url, language="ko")
        article.download()
        article.parse()
        title_list.append(article.title)
        text_list.append(article.text)
        source_url_list.append(url)

    df = pd.DataFrame({"title": title_list, "news": text_list, "url": source_url_list})
    df["title"] = df["title"].str.replace("\n", " ")
    df["news"] = df["news"].str.replace("\n", " ")
    # CSV를 엑셀에서 열 때 제목 클릭으로 본문 URL에 이동하도록 HYPERLINK 수식 생성
    df["title_link"] = df.apply(
        lambda row: f'=HYPERLINK("{row["url"]}","{str(row["title"]).replace("\"", "\"\"")}")',
        axis=1,
    )
    df["category"] = idx2word.get(cat2, "알 수 없는 카테고리")
    return df

data = make_data(url_list, rec[1], rec[2])
print(data[["title"]].head())


def save_csv(df, cat2, target_date):
    file_name = f"nate_news_{cat2}_{target_date}.csv"
    df.to_csv(file_name, index=False, encoding="utf-8-sig")
    return file_name


target_date = datetime.now().strftime("%Y%m%d")
saved_file = save_csv(data, rec[2], target_date)
print(f"CSV 저장 완료: {saved_file}")



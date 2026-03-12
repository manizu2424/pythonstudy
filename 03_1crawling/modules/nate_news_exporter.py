from concurrent.futures import ThreadPoolExecutor
import pandas as pd
from newspaper import Article
import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/145.0.0.0 Safari/537.36"
    )
}

DEFAULT_TIMEOUT = 6
DEFAULT_RETRIES = 1
DEFAULT_ARTICLE_WORKERS = 8


def _create_session(headers=None, retries=DEFAULT_RETRIES):
    session = requests.Session()
    session.headers.update(headers or DEFAULT_HEADERS)

    retry = Retry(
        total=retries,
        connect=retries,
        read=retries,
        backoff_factor=0.5,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"],
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session


def build_news_url(cat0, cat1, cat2, date, page):
    return (
        f"https://news.nate.com/{cat0}"
        f"?cate={cat1}&mid=n{cat2}&type=c&date={date}&page={page}"
    )


def fetch_html(url, session, timeout=DEFAULT_TIMEOUT):
    response = session.get(url, timeout=timeout)
    response.raise_for_status()
    return response.text


def extract_article_urls(html):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.select("a.lt1")
    article_urls = []
    for link in links:
        href = link.get("href")
        if href:
            article_urls.append(f"https:{href}")
    return article_urls


def extract_article_items(html):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.select("a.lt1")
    article_items = []
    for link in links:
        href = link.get("href")
        if href:
            article_items.append({
                "url": f"https:{href}",
                "title": link.get_text(strip=True),
            })
    return article_items


def make_article_list(cats, date, pages, timeout=DEFAULT_TIMEOUT, retries=DEFAULT_RETRIES):
    cat0, cat1, cat2 = cats
    article_items = []
    session = _create_session(retries=retries)

    for page in range(1, pages + 1):
        url = build_news_url(cat0, cat1, cat2, date, page)
        html = fetch_html(url, session, timeout=timeout)
        article_items.extend(extract_article_items(html))

    # 순서를 유지하면서 중복 URL 제거
    deduped_items = []
    seen = set()
    for item in article_items:
        if item["url"] not in seen:
            seen.add(item["url"])
            deduped_items.append(item)
    return deduped_items


def make_url_list(cats, date, pages, timeout=DEFAULT_TIMEOUT, retries=DEFAULT_RETRIES):
    return [item["url"] for item in make_article_list(cats, date, pages, timeout, retries)]


def _parse_article(url, include_body):
    article = Article(url, language="ko")
    article.download()
    article.parse()
    return {
        "title": (article.title or "").replace("\n", " "),
        "news": (article.text or "").replace("\n", " ") if include_body else "",
    }

    # 순서를 유지하면서 중복 링크 제거
    return list(dict.fromkeys(url_list))


CATEGORY_MAP = {
    "0601": "최신뉴스",
    "0602": "과학",
    "0603": "디지털",
    "0604": "컴퓨터/인터넷",
    "0605": "뉴미디어/통신",
    "0606": "게임",
    "0607": "IT/과학일반",
}

REC_CATEGORY = ("recent", "its", "0601")
SCI_CATEGORY = ("subsection", "its01", "0602")
DIG_CATEGORY = ("subsection", "its02", "0603")
COM_CATEGORY = ("subsection", "its03", "0604")
MED_CATEGORY = ("subsection", "its04", "0605")
GAM_CATEGORY = ("subsection", "its05", "0606")
GEN_CATEGORY = ("subsection", "its998", "0607")

CATEGORY_ALIAS = {
    "rec": REC_CATEGORY,
    "recent": REC_CATEGORY,
    "sci": SCI_CATEGORY,
    "science": SCI_CATEGORY,
    "dig": DIG_CATEGORY,
    "digital": DIG_CATEGORY,
    "com": COM_CATEGORY,
    "computer": COM_CATEGORY,
    "med": MED_CATEGORY,
    "media": MED_CATEGORY,
    "gam": GAM_CATEGORY,
    "game": GAM_CATEGORY,
    "gen": GEN_CATEGORY,
    "general": GEN_CATEGORY,
}


def resolve_category(key):
    normalized = (key or "rec").strip().lower()
    return CATEGORY_ALIAS.get(normalized, REC_CATEGORY)


def collect_news_dataframe(
    category,
    date,
    pages,
    include_body=False,
    workers=DEFAULT_ARTICLE_WORKERS,
    timeout=DEFAULT_TIMEOUT,
    retries=DEFAULT_RETRIES,
):
    article_items = make_article_list(category, date, pages, timeout=timeout, retries=retries)

    title_list = [item["title"] for item in article_items]
    text_list = [""] * len(article_items)
    source_url_list = [item["url"] for item in article_items]

    if include_body and source_url_list:
        worker_count = max(1, min(workers, len(source_url_list)))
        with ThreadPoolExecutor(max_workers=worker_count) as executor:
            results = list(executor.map(lambda url: _parse_article(url, include_body=True), source_url_list))

        for idx, parsed in enumerate(results):
            # 리스트에서 가져온 제목이 비어 있으면 Article 제목으로 보강
            if not title_list[idx]:
                title_list[idx] = parsed["title"]
            text_list[idx] = parsed["news"]

    cat2 = category[2]
    df = pd.DataFrame({"title": title_list, "news": text_list, "url": source_url_list})
    df["title_link"] = df.apply(
        lambda row: f'=HYPERLINK("{row["url"]}","{str(row["title"]).replace("\"", "\"\"")}")',
        axis=1,
    )
    df["category"] = CATEGORY_MAP.get(cat2, "알 수 없는 카테고리")
    return df

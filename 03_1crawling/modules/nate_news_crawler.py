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

DEFAULT_TIMEOUT = 10
DEFAULT_RETRIES = 3


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


def make_url_list(cats, date, pages):
    cat0, cat1, cat2 = cats
    url_list = []
    session = _create_session()

    for page in range(1, pages + 1):
        url = build_news_url(cat0, cat1, cat2, date, page)
        html = fetch_html(url, session)
        url_list.extend(extract_article_urls(html))

    # 순서를 유지하면서 중복 링크 제거
    return list(dict.fromkeys(url_list))

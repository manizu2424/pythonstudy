import requests
from bs4 import BeautifulSoup


def get_exchange_rate(C_from):
    country_code = {
        "미국": "USD",
        "일본": "JPY",
        "중국": "CNY",
        "유럽연합": "EUR",
        "영국": "GBP",
        "호주": "AUD",
        "캐나다": "CAD",
        "스위스": "CHF",
        "홍콩": "HKD",
        "싱가포르": "SGD",
    }
    country_alias = {
        "미국": "미국",
        "일본": "일본",
        "중국": "중국",
        "유럽": "유럽연합",
        "eu": "유럽연합",
        "영국": "영국",
        "호주": "호주",
        "캐나다": "캐나다",
        "스위스": "스위스",
        "홍콩": "홍콩",
        "싱가포르": "싱가포르",
        "싱가폴": "싱가포르",
        "달러": "미국",
        "달라": "미국",
        "앤화": "일본",
        "엔화": "일본",
        "위안": "중국",
        "유로": "유럽연합",
        "파운드": "영국",
        "호주달러": "호주",
        "캐나다달러": "캐나다",
        "프랑크": "스위스",
        "홍콩달러": "홍콩",
        "싱가포르달러": "싱가포르",
    }

    input_text = C_from.strip()
    if not input_text:
        return "통화/국가를 입력해주세요. 예: 미국, 일본, USD, JPY"

    upper_code = input_text.upper()

    if upper_code in country_code.values():
        C_from_name = upper_code
    else:
        normalized_country = country_alias.get(input_text.lower(), country_alias.get(input_text, input_text))
        C_from_name = country_code.get(normalized_country, upper_code)

    if C_from_name not in country_code.values():
        supported_countries = ", ".join(country_code.keys())
        supported_codes = ", ".join(country_code.values())
        return (
            "지원하지 않는 입력입니다. "
            f"지원 국가: {supported_countries} | 지원 코드: {supported_codes}"
        )

    url = f"https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_{C_from_name}KRW"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    country_info = soup.find("div", class_="h_company").find("h2").get_text(strip=True)
    rate_info = soup.find("p", class_="no_today").get_text(strip=True)

    c_icon = soup.find("span", class_="ico")
    c_sign = ""
    if c_icon:
        if "up" in c_icon["class"]:
            c_sign = "▲"
        elif "down" in c_icon["class"]:
            c_sign = "▼"

    exday_info = soup.find("p", class_="no_exday").get_text(strip=True).replace("전일대비", "").strip()
    # print(f"{country_info} {C_from_name} 실시간 환율: {rate_info} | 전일대비 {c_sign} {exday_info}")
    r = f"{country_info} {C_from_name} 실시간 환율: {rate_info} | 전일대비 {c_sign} {exday_info}"
    return r



print(get_exchange_rate("미국"))
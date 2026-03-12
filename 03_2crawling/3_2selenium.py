from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# driver = webdriver.Chrome()
# driver.get("https://www.naver.com")
# result = driver.find_element(By.CLASS_NAME, "shortcut_list")
# print(result.text)
# driver.quit()

driver = webdriver.Chrome()
driver.implicitly_wait(10)  # 최대 10초까지 요소가 나타날 때까지 기다립니다.
driver.get("https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query=%EB%82%B4%EC%9D%BC%EB%82%A0%EC%94%A8")
element1 = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[1]/section/div[1]/ul/div[1]/div/div/div/div[1]/div/div[2]/div/div")
element2 = driver.find_element(By.CSS_SELECTOR, ".sds-comps-vertical-layout.sds-comps-full-layout.fds-ugc-single-intention-item-list-tab")
print(element2.text)
print("=" * 50)
title = driver.title
print(title)
time.sleep(1)
driver.quit()
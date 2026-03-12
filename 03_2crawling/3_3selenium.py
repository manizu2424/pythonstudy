from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.naver.com")

def search_naver():
  input_element = driver.find_element(By.ID, "query")
  input_element.send_keys("파이썬")
  input_element.send_keys(Keys.ENTER)
  # input_element.submit()
  sleep(3)
# search_naver()

def search_naver(item):
  input_element = driver.find_element(By.ID, "query")
  input_element.send_keys(item)
  input_element.send_keys(Keys.ENTER)
  # input_element.submit()
  sleep(3)
# search_naver("파이썬")

def search_naver_with_input():
  search_query = input("검색어를 입력하세요: ")
  input_element = driver.find_element(By.ID, "query")
  input_element.send_keys(search_query)
  input_element.send_keys(Keys.ENTER)
  sleep(3)
  driver.quit()

search_naver_with_input()
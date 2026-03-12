from selenium import webdriver
from time import sleep

# 크롬 브라우져 실행 후 창 크기 제어
def window_control():
  driver = webdriver.Chrome()
  driver.get("https://www.google.com")
  driver.set_window_size(800, 600)
  driver.set_window_position(100, 100)
  driver.maximize_window()
  sleep(3) # 3초 대기
  driver.quit()

# window_control()

# 크롬 브라우져 실행 전 창 크기 제어
def window_control_predefined_options():
  options = webdriver.ChromeOptions()
  # options.add_argument('window-size=800,600')
  # options.add_argument('window-position=100,100')
  options.add_argument('start-maximized')
  driver = webdriver.Chrome(options=options)
  driver.get("https://www.google.com")
  sleep(3)
  driver.quit()

window_control_predefined_options()
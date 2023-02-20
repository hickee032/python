import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://www.daum.net')
time.sleep(2)

input_ele = driver.find_element(By.NAME, 'q')
time.sleep(1)

input_ele.send_keys('빅데이터')
time.sleep(2)

input_ele.submit()
time.sleep(2)

link_info = driver.find_element(By.LINK_TEXT, '빅데이터(Big Data)란 무엇일까?')
time.sleep(2)
link_info.click()
time.sleep(10)

driver.quit()  # 리소스를 반납한다 File.close() 같은

# 데이터 수집 - 데이터 (웹) 크롤링, 스크랩핑
# 시스템을 구축 -> 데이터 수집 -> 전처리

# 정형, 반정형, 비정형 ( 3가지로 구분 )
# 정형 - 엑셀, DB, CSV
# 반정형 - html, xml, json
# 비정형 - 소리(음성), 이미지, 영상 등등 ( 실생활에서의 아날로그 데이터들 )

# selenium
import time
from selenium import webdriver
# 크롬 -> 도움말 -> 크롬 정보 -> 버전 확인 109.0.5414.75
# 버전업이 되면서 크롬 드라이버 설치를 안해도 된다
from selenium.webdriver.common.by import By

"""
browser = webdriver.Chrome()  # 브라우저 정보를 얻음
browser.get('http://python.org')
time.sleep(2)  # 2초대기
browser.quit()  # browser 종료
"""

browser = webdriver.Chrome()  # 브라우저 정보를 얻음
browser.get('http://python.org')

menus = browser.find_elements(By.CSS_SELECTOR, '#top ul.menu li')

pypi = None
for m in menus:
    if m.text == 'Docs':
        pypi = m
    print(m.text)
time.sleep(2)

pypi.click()  # 메뉴를 선택

time.sleep(3)

browser.quit()



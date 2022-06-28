#webdriver_manager 활용
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import os
import time 

#selenium webdriver는 크롬 브루우저 버전 전용을 사용해야 한다. 
# 실습path: /home/자신의 homeid/datagather/selenium/chromedriver

#크롬에 옵션을 주기. 크롬 실행할 때 함수를 실행하듯이 할 수 있다. 
options = webdriver.ChromeOptions()             #옵션 설정 객체 생성
options.add_argument("window-size=1000,1000")   #브라우저 크기 설정
options.add_argument("no-sanbox")               #샌드박스 사용 안하겠음
#options.add.argument("headless")               #크롬 창을 안뜨게 함

driver_path = "/Users/gimhyeonjeong/datagather/selenium/chromedriver"
# patn 경로 확인은 밑에 터미널에서 pwd를 하면 위치가 나와 그것을 복사해 붙여넣는다. 
chrome = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# 창을 띄울 뗴 창을 제어하기 위한 옵션을 실행할 수 있다. 
chrome.get("http://naver.com")

wait = (chrome, 10)
#ele = wait.until(EC.presence_of_elemnet_located(By.CSS_SELECTOR, ""))
chrome.get("http://shopping.naver.com")
chrome.back()
time.sleep(2)
chrome.forward()
time.sleep(2) # 단위: sec
chrome.close()
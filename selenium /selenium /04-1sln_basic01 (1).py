from selenium import webdriver
import time
#selenium webdriver는 크롬 브루우저 버전 전용을 사용해야 한다. 
# 실습path: /home/자신의 homeid/datagather/selenium/chromedriver

driver_path = "/home/ubuntu/datagather/chromedriver"
# patn 경로 확인은 밑에 터미널에서 pwd를 하면 위치가 나와 그것을 복사해 붙여넣는다. 
chrome = webdriver.Chrome(driver_path)
chrome.get("http://naver.com")
#driver_path.get("http://naver.com")
time.sleep(3) # 단위: sec
chrome.close()
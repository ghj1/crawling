# naver login 하기
# input box에 텍스트 입력하기 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time  
import os

options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox") 
# options.add_argument("headless")  # 크롬 창을 안뜨게함.
#options.add_experimental_option("excludeSwitches", ["enable-logging"])

chrome = webdriver.Chrome(ChromeDriverManager().install(), options=options)
wait = WebDriverWait(chrome, 10) 
short_wait = WebDriverWait(chrome, 3)

chrome.get("https://www.daum.net/")
# login_botton = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a#gnb_login_button")))
login_botton = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a#gnb_login_button")))
print(login_botton.text)
login_botton.click()

input_id = wait.until(EC.visibility_of_all_elements_located(By.CSS_SELECTOR, "input#id"))
input_pw = wait.until(EC.visibility_of_all_elements_located(By.CSS_SELECTOR, "input#pw"))

#search.send_keys("아이폰 케이스\n") 

# chapchar때문에 로그인이 안됨
# input_id.send_keys("id")
# input_pw.send_keys("pw")
# input_pw.send_keys("\n")

 
# 잘못 입력해 에러났을 경우 빠져나오기 
# wait.until(EC.presence_of_element_located(By.CSS_SELECTOR, "a#gnb_logout_button"))

#time.sleep(3)
#chrome.close()
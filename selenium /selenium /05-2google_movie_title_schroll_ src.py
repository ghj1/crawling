# https://play.google.com/store/movies 할인정보 검색
# selenium과 beautifulsoup 연동한 크롤링 실습

#### 동적 페이지 스크롤
#from os import link
from selenium import webdriver
import time  

options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument("no-sandbox") 
#options.add_argument('headless')

driver_path = '/home/ubuntu/datagather/selenium/chromedriver'
chrome = webdriver.Chrome(driver_path, options=options)

# 페이지 이동
url =  "https://play.google.com/store/movies/top"
chrome.get(url)

# 지정한 위치로 스크롤 내리기
# 1920 x 1080 (해당도 위치로  스크롤)
# chrome.execute_script("window.scrollTo(0, 1080)")   #1920* 1080(x, y)
# chrome.execute_script("window.scrollTo(0, 2080)")   #1920* 1080
# chrome.execute_script("window.scrollTo(0, 0)")   #1920* 1080


# 화면 가장 아래로 스크롤 내리기
interval = 2

chrome.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# 현재 document의 높이 반환
prev_height = chrome.execute_script("return document.body.scrollHeight")

while True: # break를 항상 줘야 한다. 

    # 스크롤을 현재 페이지 가장 아래로 내림
    chrome.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    # 페이지 로딩 대기
    time.sleep(interval)
    # 현재 문서 높이를 가져와서 저장
    curr_height = chrome.execute_script("return document.body.scrollHeight")
    #print(prev_height,curr_height)
    if curr_height == prev_height:
        break
    # 이전 높이 변경
    prev_height = curr_height

print("스크롤 완료")
time.sleep(1)
#chrome.close()
#chrome.quit()


# https://play.google.com/store/movies 할인정보 검색하기
 

from bs4 import BeautifulSoup as bs

# selenium chrome 드라이버로 받은 결과를 beautifulsoup에 전달하여 html 문서로 파싱
soup = bs(chrome.page_source, "html.parser")

movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
print(len(movies))

# movies = soup.find_all("div", attrs={"class" : "ZmHEEd"})
# print(movies)
for movie in movies:
    title = movie.find("div", attrs= {"class": "WsMG1c nnK0zc"}).get_text()

###할인 된 것만 뽑기 
# 할인 전 가격 
    origin_price = movie.find("span", attrs= {"class" : "SUZt4c djCuy"})
    if origin_price:
        origin_price = origin_price.get_text()
        time.sleep(1)

    else:
        continue

    price = movie.find("span", attrs = {"class": "VfPpfd ZdBevf i5DZme"}).get_text()


    link = movie.find("a", attrs= {"class" : "JC71ub"})["href"]


    print(f"제목: {title}")
    print(f"할인 전 가격: {origin_price}")
    print(f"할인 후 가격: {price}")
    print("링크: ",  "https://play.google.com"+link)
    print("-" * 100)

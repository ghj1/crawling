# input box에 텍스트 입력하기
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time  

options = webdriver.ChromeOptions() 
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox") 
# options.add_argument("headless")  # 크롬 창을 안뜨게함.
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# chrome = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver_path = '/home/ubuntu/datagather/selenium/chromedriver'
chrome = webdriver.Chrome(driver_path, options=options)
wait = WebDriverWait(chrome, 10) 
short_wait = WebDriverWait(chrome, 3) 

chrome.get("http://shopping.naver.com")


def search_keyword(key_word):
    search = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name=query]")))
    search.send_keys(key_word)
    time.sleep(1)
    search.send_keys("\n")
    # div 태그의 class의 속성 값이 basicList_link__로 시작하는 것 가져오기
    short_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class ^= basicList_info_area__")))

# selector의 속성 지정 방법
# a[class = "logout_button"]  
# a[class ^= "logout"]  # logout으로 시작
# a[class $= "button"]  # button으로 끝나는
# a[class *= "out_but"]  # out_but 문자열이 들어있는 


## 무한 스크롤, js를 selenium이 실행
# console js :window.scrollBy(0, 1000)
# scrollBy(x, y) : 현재 위치를 기준으로 상대적 위치로 이동
# chrome.execute_script("window.scrollBy(0, 1000)")
#  scrollTo(x, y) : 현재 위치를 기준으로 절대적 위치로 이동
# chrome.execute_script("window.scrollTo(0, 1000)")

# 문서의 최대 길이로 반환, 스크롤을 내렸을 때 스크롤 길이가 달라짐
# chrome.execute_script("window.scrollBy(0, document.body.scrollHeight)") 
# chrome.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# 지정한 절대적 위치로 스크롤 내리기, 1920 x 1080 (해당도 위치로  스크롤)
# chrome.execute_script("window.scrollTo(0, 1080)")   #x, 1080(x, y)
# chrome.execute_script("window.scrollTo(0, 2080)")   #0, 2080(x, y)
# chrome.execute_script("window.scrollTo(0, 0)")      #0, 0

def gather_items():
    # 화면 가장 아래로 스크롤 내리기
    interval = 2

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

# for i in range(8):
#     chrome.execute_script("window.scrollBy(0, " + str((i+1) * 1000) + ")") 
#     time.sleep(1) # laoding 할때까지 좀 기다려줌

    print("스크롤 완료")

    items = chrome.find_elements_by_css_selector("div[class ^= basicList_info_area__")


    for item in items :
        # 광고 걸러내기
        try:
            item.find_element_by_css_selector("button[class ^= ad_")
            continue
        except:
            pass

        print(item.find_element_by_css_selector("a[class ^= basicList_link__]").text)


    time.sleep(1)
    next_page = chrome.find_element_by_css_selector("a[class ^= pagination_next__]")
    next_page.click()



if __name__ == "__main__" :
    key_word = input("검색할 키워드를 입력해 주세요: ")
    order_page = int(input("몇개의 페이지를 스크래핑 할까요?: "))
    page_num = 1
    search_keyword(key_word)

    while page_num <= order_page:
        print("-"*30)
        gather_items()
        page_num += 1

    


#chrome.quit()
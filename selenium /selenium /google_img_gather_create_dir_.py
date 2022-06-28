from re import search
from selenium import webdriver
from webdriver_manager import chrome
from webdriver_manager.chrome import ChromeDriverManager
import os
from webdriver_manager.driver import ChromeDriver
import create_dir_2



def search_selenium(search_name, search_path, search_limit) :
    search_url = "https://www.google.com/search?q=" + str(search_name) + "&hl=ko&tbm=isch"
    
    chrome = webdriver.Chrome(ChromeDriverManager().install())
    chrome.get(search_url)
    chrome.implicitly_wait(2)

    image_count =len(chrome.find_elements_by_tag_name("img"))
    print("로드된 이미지 개수: ", image_count)

    #파일을 저장하기 위한 디렉토리 생성
    create_dir_2.search_selenium(search_name, search_path)

    for i in range(search_limit) :
        image = chrome.find_elements_by_tag_name("img")[i]
        # search_path(현재 작업 디렉토리), search_name(ex. dog)
        #search_path + search_name + str(i) + ".png"
        image.screenshot(search_path + search_name + str(i) + ".png")
    chrome.close()

if __name__ == "__main__" :
    search_name = input("검색하고 싶은 키워드 : ")
    search_limit = int(input("원하는 이미지 수집 개수: "))
    search_path = os.path.dirname(os.path.realpath(__file__)) + "/" + search_name + "/"
    print(search_path)    
    search_selenium(search_name,search_path, search_limit)

# 네이버 웹툰 가우스 전자 타이틀과 별점을 추출
# title, 별점 틱트형으로 만들기
# 평균 평점 구해서 출력하기
# 함수로 title, 별정 추출하는 부분을 함수로 정의하기

from bs4 import BeautifulSoup as BS
import requests as req

url ="https://comic.naver.com/webtoon/list?titleId=335885"
res = req.get(url)
res.raise_for_status
soup = BS(res.text, "html.parser")

#네이버 웹툰 전체 목록 가져오기
# class 속성이 title인 모든 "a" element 추출
gause_dict = {}  # title, rate
total_rates = 0  # 평균 평점
def gause_func():
  # title 추출
  titles=[]
  
  cartoons = soup.find_all("td", attrs={"class":"title"})
  for cartoon in cartoons:
    title = cartoon.find("a").get_text()
    titles.append(title)
    #print(title)

  # 평점 추출
  rates = []
  total_rates = 0
  cratoons = soup.find_all("div", attrs={"class":"rating_type"})
  for cartoon in cratoons:
    rate = cartoon.find("strong").get_text()
    total_rates += float(rate)
    rates.append(rate)
    #print(rate)
  return titles, rates, total_rates

titles, rates, total_rates = gause_func()  
gause_dict['titles'] = titles
gause_dict['rates'] = rates

print("=============================")
print("전체 점수 : ", total_rates)
print("평균 점수 : ", total_rates / len(titles))
print(gause_dict)


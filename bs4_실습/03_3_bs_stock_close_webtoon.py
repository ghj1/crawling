from os import write
from bs4 import BeautifulSoup as BS
import requests as req
import csv

url ="https://comic.naver.com/webtoon/list?titleId=335885"
res = req.get(url)
soup = BS(res.text, "html.parser")
#print(res.raise_for_status) # 응답값 확인, 정상 200

dic_al= {}

trs = soup.select("td.title")
titles = []
for tr in trs:
  title = tr.select("a")[0].get_text(strip=True)
  titles.append(title)




trs = soup.select("div.rating_type")
scores = []
for tr in trs:
  score = tr.select("strong")[0].get_text(strip= True)
  scores.append(score)


dic_al['title'] = titles
dic_al['score'] = scores
print(dic_al)

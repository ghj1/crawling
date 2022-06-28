# 해외 증시 상위 종목 가져오기
from bs4 import BeautifulSoup as BS
import requests as req
import csv

url ="https://finance.yahoo.com/most-active"
res = req.get(url)
print(res.raise_for_status) # 응답값 확인, 정상 200

soup = BS(res.text, "html.parser")
data =[]
for tr in soup.select('table tr'):
  if len(tr.select('td:nth-child(2)')) == 0:
    continue
  tit = tr.select("td:nth-child(2)")[0].get_text(strip=True)
  data.append(tit)
  price = tr.select("td:nth-child(3) fin-streamer")[0].get_text(strip=True)
  data.append(price)
  change1 = tr.select("td:nth-child(4) span")[0].get_text(strip=True)
  data.append(change1)
  change2 = tr.select("td:nth-child(5) span")[0].get_text(strip=True)
  data.append(change2)

  print(tit+" : " + price +" : " + change1+" : "+change2)
  
with open("overseas_stock.csv", "w", encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
import requests as req 
from bs4 import BeautifulSoup as BS
import csv
import re

# bs 기본형식
#url ='https://finance.naver.com/marketindex/?tabSel=exchange#tab_section' 
url = 'https://finance.naver.com//marketindex/exchangeList.naver'
res = req.get(url)
soup = BS(res.text, "html.parser")


#print(soup)
tds = soup.find_all("td")  #가져오려고 하는 모든 요소들의 정보들(td안에 요소들)
#print(tds)


names = []
tds = soup.select("td.tit > a")
for td in tds:
    #if len(td.find_all("a")) == 0: 
    # continue
    #print(td.get_text(strip=True))
    names.append(td.get_text(strip=True))


# 환율값 가져오기 
prices = []
tds = soup.select("td.sale")
for td in tds:
    # if "class" in td.attrs: # keyerror: 'class' 해결
    #     if "sale" in td.attrs["class"]:
    prices.append(td.get_text(strip=True))
           # print(td.text)
           # prices.append(td.text) 
           


# try1: 크롤링 내용 파일로 저장하기
import csv
# with open("./exchange_rate.csv", "w", encoding="utf-8-sig", newline='') as f:
#   writer = csv.writer(f)
#   writer.writerows(names)
#   writer.writerows(prices)
# try2 : 
#with open("./exchange_rate.csv", "w", encoding="utf-8-sig", newline='') as f:
#  f.write(data_list)
# try3 :
csvFile = open('nameprice.csv', 'w+')
try:
    writer = csv.writer(csvFile)
    for i in range(len(names)):
        writer.writerow( (names[i], prices[i]))
finally:
    csvFile.close()  
###########################
# 환전
# 위의 두 결과를 출력하기
print("---------------")
print("환율 계산기")
print("---------------")
print("")
for c in zip(names, prices):
  temp = c[0] + " : " + c[1]
  print(temp)
print("")
#usd =captuers[0][1].replace(",", "")
usd = float(prices[0].replace(",", ""))
won = input("달러로 바꾸길 원하는 금액(원)을 입력해 주세요. : ")
won = int(won)
dollar = won / usd
dollar = int(dollar)
print(f"{dollar} 달러 환전되었습니다.")
'''
# 정리 ##################################
print('-------------')  
#방법1
for td in tds:
  if len(td.find_all("a")) == 0 :
    continue  # 값이 없으면 pass
  print(td.get_text(strip=True))
print('-------------')  
#방법2
for td in tds:
  if len(td.find_all("a")) == 0 :
    continue  # 값이 없으면 pass  
  for s in td.stripped_strings:
    print(s)
'''
''' # .stripped_strings 은 스트링 문자열은 편집할 때 사용
<div> 총 가격은 <b>19,000</b>원 입니다.</div>
총 가격은 19,000원 입니다.
["총 가격은", "19,000", "원 입니다."]
'''
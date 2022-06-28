import requests as req 
from bs4 import BeautifulSoup as BS
import csv
import re

# bs 기본형식
#url ='https://finance.naver.com/marketindex/?tabSel=exchange#tab_section' 
url = 'https://finance.naver.com//marketindex/exchangeList.naver'
res = req.get(url)
soup = BS(res.text, "html.parser")
body = res.text


#print(soup)
tds = soup.find_all("td")  #가져오려고 하는 모든 요소들의 정보들(td안에 요소들)
#print(tds)


names = []
# for td in tds:
#     if len(td.find_all("a")) == 0:
#         continue # 값이 없으면 pass

# 방법1 : 국가명 뽑아내기 
#     print(td.string)
#     print(td.get_text(strip =True))

# 방법2: 국가명 뽑아내기 
for td in tds:
    if len(td.find_all("a")) == 0:
        continue # 값이 없으면 pass
    #print(td.get_text(strip=True))
    names.append(td.get_text(strip=True))

    # print(td.strings)
    # for s in td.strings: # 공백 포함되어 있다. 
    #     print(s)

    # for s in td.stripped_strings:
    #     #print(s)
    #     #names.append(s)
    #     names.append(td.get_text(strip=True))

# 환율값 가져오기 
prices = []
for td in tds:
    if "class" in td.attrs: # keyerror: 'class' 해결
        if "sale" in td.attrs["class"]:
            prices.append(td.get_text(strip=True))
           # print(td.text)
           # prices.append(td.text) 
           
         
# print(names)
# print(prices)


# print(soup.title)
# print(soup.title.text)
# print(soup.title.string)
r = re.compile(r"h_lst.*?blind\">(.*?)</span>.*?value\">(.*?)</", re.DOTALL) 
captuers = r.findall(body)
for c in captuers:
  print(c[0] + " : " + c[1])

print("")
#usd =captuers[0][1].replace(",", "")
usd = float(captuers[0][1].replace(",", ""))
won = input("달러로 바꾸길 원하는 금액(원)을 입력해 주세요. : ")
won = int(won)
dollar = won / usd
dollar = int(dollar)
print(f"{dollar} 달러 환전되었습니다.")
#print(captuers)

print("---------------") 
print("환율 계산기") 
print("---------------") 
print("")

# for c in body: print(c[0] + " : " + c[1])
# print("")
# usd =body[0][1].replace(",", "")
# usd = float(body[0][1].replace(",", ""))
# won = input("달러로 바꾸길 원하는 금액(원)을 입력해 주세요. : ") 
# won = int(won)
# dollar = won / usd
# dollar = int(dollar)
# print(f"{dollar} 달러 환전되었습니다.")
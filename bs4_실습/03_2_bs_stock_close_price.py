from os import write
from bs4 import BeautifulSoup as BS
import requests as req
import csv


url = "https://finance.naver.com/sise/lastsearch2.nhn"
res = req.get(url)
soup = BS(res.text, "html.parser")
#print(res.raise_for_status()) #응답값을 확인 하는 코드 
#print(soup)
# tr:nth-child(3) > td:nth-child(2) > a

#print(soup.title)
#tds = soup.select("table.type_5 td a.title")


trs = soup.select("table.type_5 tr")
data_list = []
for tr in trs:
    temp = []
    if len(tr.select("a.tltle")) == 0: # []공백 없애기 
        continue
    data1= tr.select("a.tltle")[0].get_text(strip= True) #list이므로 인덱스가 하나이지만 list이기 때문에 인덱싱을 하고 get_text를 넣어야 한다. 
    data2= tr.select("td.number:nth-child(3)")[0].get_text(strip= True)
    data3= tr.select("td.number:nth-child(4)")[0].get_text(strip= True)
    #temp = td.get_text(strip=True)
    temp.append(data1)
    temp.append(data2)
    temp.append(data3)
    #print(temp)
    data_list.append(temp)



# with open("data.csv", "w", encoding= "utf-8-sig", newline=" ")as f:
#     write = csv.writer(f)
#     write.writerow(data_list)

csvFile = open('data.csv', 'w+')
try:
    writer = csv.writer(csvFile)
    for i in range(len(data_list)):
        writer.writerow(data_list[i])
finally:
    csvFile.close()  

# 한set로 묶기 


# temp = []
# for td in tds:
#     temp.append(td.get_text(strip=True)) # strip=True 공백 문자 날리는 법
# #print(temp)

# nowpe = []   
# tds = soup.select("td.number:nth-child(3)")
# for td in tds:
#     nowpe.append(td.get_text(strip=True))
# #print(nowpe)

# nowpr = []
# tds = soup.select("td.number:nth-child(4)")
# for td in tds:
#     nowpr.append(td.get_text(strip=True))
# #print(nowpr)

#     #contentarea > div.box_type_l > table > tbody > tr:nth-child(3) > td:nth-child(3)

# fin = []
# for c in zip(temp, nowpe, nowpr):
#   fin.append(c[0] + " : " + c[1] + " : " + c[2])
# print(fin)
# print("")
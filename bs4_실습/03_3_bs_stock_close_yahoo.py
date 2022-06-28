from bs4 import BeautifulSoup as BS
import requests as req
import csv
import pymysql

conn = pymysql.connect(host='localhost', port = 3306, user = 'ubuntu', 
passwd= 'ubuntu', db = 'stockdb')

cur = conn.cursor()

CREATE_SQL = """
CREATE TABLE IF NOT EXISTS items(
    id integer auto_increment,
    company VARCHAR(50) NOT NULL,
    stock_price FLOAT(20),
    changes VARCHAR(20),
    per_changes VARCHAR(30),
    primary key(id))"""

cur.execute(CREATE_SQL)

# per_changes, changes float로 줘서 오류가 나서 보니 +, %는 문자열로 줘야지 들어간다. 

url = "https://finance.yahoo.com/most-active"
res = req.get(url)
soup = BS(res.text, "html.parser")
#print(soup)

trs = soup.select("tr.simpTblRow")

data = []
for tr in trs:
    temp = []
    company = tr.select("td:nth-child(2)")[0].get_text(strip=True)
    stock_price = tr.select("td:nth-child(3)")[0].get_text(strip=True)
    changes = tr.select("td:nth-child(4)")[0].get_text(strip=True)
    per_changes = tr.select("td:nth-child(5)")[0].get_text(strip=True)
    temp.append(company)
    temp.append(stock_price)
    temp.append(changes)
    temp.append(per_changes)

    data.append(temp)


csvFile = open('data2.csv', 'w+')
try:
    writer = csv.writer(csvFile)
    for i in range(len(data)):
        writer.writerow(data[i])
finally:
    csvFile.close()  

with open('data2.csv','w',encoding="utf-8-sig",newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

cur.execute("INSERT INTO items(company, stock_price, changes, per_changes) VALUES(%s,%s,%s,%s)",
(company, stock_price, changes, per_changes))
#cur.execute("SELECT*FROM items")

conn.commit()
conn.close()

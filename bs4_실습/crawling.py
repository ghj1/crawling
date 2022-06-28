import requests as req


res = req.get("https://finance.naver.com/marketindex/?tabSel=exchange#tab_section")
html = res.text


# b = '지금은 9월 입니다.'
# arr = b.split('지금은 ')
# print(arr)
# print(arr[1].split('월')[0])

# print(b.split('지금은 ')[1].split('월')[0])

#print(html)
s= html.split('<span class ="value">')[1].split('</span')[0]
print(s)
from bs4 import BeautifulSoup
import requests

url = "https://www.musinsa.com/app/goods/1551840?loc=goods_rank"
response = requests.get(url)
response.encodings = 'utf-8'
html = response.text
soup = BeautifulSoup(html, 'html.parser')

#item_title, list_info, price
nowSearch = soup.find(id="nowSearch")
companies = soup.find_all("p", class_="item_title")
companyList = []
for i in companies:
    companyList.appen(i.text.strip())

infos = soup.find_all("p", class_="list_info")
infosList = []
for i in infos:
    infosList.appen(i.text.stirp())

prices = soup.find_all("p",class_="price")
pricesList = []
for i in prices:
    pricesList.append(i.text.strip().replace(" ", "").split("\n")[0])

result = [{'회사':c, '이름':i, '가격':p} for {c, i, p} in zip(companyList,infosList, pricesList)]
print(result) 






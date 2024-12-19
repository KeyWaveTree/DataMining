from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import ssl
import datetime

context = ssl._create_unverified_context()

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
hds = {'User-Agent': user_agent}

action = 'priceinfo'
regday = '2020-11-03'
itemcategorycode = 200
itemcode = 211

# regday = datetime.datetime.now()
# print(regday.date(), regday.year, regday.month, regday.day, regday.weekday())
# regday -= datetime.timedelta(days=1)
# print(regday.date(), regday.year, regday.month, regday.day, regday.weekday())

web_url = 'https://www.kamis.or.kr/customer/price/retail/item.do?action={0}&regday={1}&itemcategorycode={2}&itemcode{3}'.format(action, regday, itemcategorycode, itemcode)
request = Request(web_url, headers=hds)
response = urlopen(request, context=context)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')

# print(html)

print(regday, '평균 판매가')

tr = soup.find("tr", {'class': 'fwb'})
td = tr.find_all('td')[1]
print(td.text, type(td.text))

price = td.text
price = int(price.replace(',', ''))
print(price, type(price))

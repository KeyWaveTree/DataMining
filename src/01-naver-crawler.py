from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import ssl

context = ssl._create_unverified_context()

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36' #유저정보를 포함하지 않으면 웹 크롤링을 할 수 없음
hds = {'User-Agent': user_agent}

web_url = 'https://datalab.naver.com/keyword/realtimeList.naver?where=main'
request = Request(web_url, headers=hds)
response = urlopen(request, context=context)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')

# print(html)

spans = soup.find_all("span", {'class', 'item_title'})
for i in range(len(spans)):
    print(i + 1, spans[i].text)

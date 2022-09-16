import requests
from bs4 import BeautifulSoup as bs

URL = 'https://www.gismeteo.ru/diary/4368/2022/1/'
HEADERS = {
              "Accept": "*/*",
"User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"

}

req = requests.get(URL, headers=HEADERS)
src = req.text

one_day = []
soup = bs(req.content, 'lxml')
items = soup.find_all("tr")
for item in items:
    number = item.find('td', class_="first"),
    temp = item.find('td', class_="first_in_group"),
    p = item.find('td', class_=""),
    wind = item.find('span', class_="")
    #print(f"{number}, {temp}, {p}, {wind}")
    print(number,temp,p,wind)







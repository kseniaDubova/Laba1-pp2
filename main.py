import requests
from bs4 import BeautifulSoup as bs
import csv

URL = 'https://www.gismeteo.ru/diary/4368/2022/1/'
HEADERS = {
              "Accept": "*/*",
"User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"

}
def get_html(url, param=""):
    req = requests.get(url, headers=HEADERS, params="param")
    return req
def clean_content(parametrs):
    index=0
    for i in parametrs:
        if parametrs[index] == '':
            parametrs.pop(index)
            index-=1
        index = index+1
    #return parametrs
def get_content(html):
#out_file = open("weather.txt", "w+")
    soup = bs(html, 'html.parser')
    items = soup.find_all("tr")
    all_number = []

    for item in soup.find_all("td"):
        if item.find('<td class="first">') != -1:
            all_number.append(item.get_text())

               # "temp": item.find('td', class_="first_in_group"),
                #"p": item.find('td', class_=""),
                #"wind": item.find('span', class_="")
    #print(all_number)
    clean_content(all_number)
    #clean_content(all_number)
    return  all_number

   # for item in items:
 #       all_weather.append(
            #{
                #"number": item.find('td', class_="first").get_text(),
                #"temp": item.find('td', class_="first_in_group").get_text(),
                ##"p": item.find('td', class_="").get_text(),
                #"wind": item.find('span', class_="").get_text()
            #}
    #    )
   # return all_weather

html = get_html(URL)
print(get_content(html.text))

#    out_file.write(number)

#out_file.close()
#print(one_day)



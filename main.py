import requests
from bs4 import BeautifulSoup as bs

URL = 'https://www.gismeteo.ru/diary/4368/2022/1/'
HEADERS = {
    "Accept": "*/*",
    "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"

}


def get_html(url):
    req = requests.get(url, headers=HEADERS)
    return req


def clean_content(parametrs):
    for number in parametrs:
        if number == '':
            parametrs.remove(number)
    return parametrs


def get_content(html):
    soup = bs(html, 'html.parser')
    all_number = []

    for item in soup.find_all("td"):
        if item.find('<td class="first">') != -1:
            all_number.append(item.get_text())

    for number in all_number:
        if number == '':
            clean_content(all_number)
    return all_number


html = get_html(URL)
main_list = get_content(html.text)
index = 0
out_file = open("dataset.csv", 'w+')
while not index==len(main_list):
    out_file.write("День №"+ main_list[index]+", "+ main_list[index+1]+", "+ main_list[index+2]+", "+ main_list[index+3]+", "+ "Вечер"+": "+ main_list[index+4]+", "+main_list[index+5]+", "+main_list[index+6]+'\n')
    index+=7
out_file.close()

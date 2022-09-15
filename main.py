import requests
from bs4 import BeautifulSoup as bs

NRL = 'https://www.gismeteo.ru/diary/4368/2022/1/'


def get_html(url, param =''):
    
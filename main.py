import requests
from bs4 import BeautifulSoup as bs

URL = 'https://www.gismeteo.ru/diary/4368/2022/1/'
HEADERS = {
              "Accept": "*/*",
"User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"

}

req = requests.get(URL, headers=HEADERS)
src = req.text

#with open("weather_file.html", "w") as file:
#    file.write(src)

#with open("weather_file.html") as file:
 #   src = file.read()
soup = bs(req.content, 'html.parser')
#all_day = soup.find_all("td")
#dd =soup.find_all(class_="first_in_group")
import re
for item in soup.find_all ("tr"):
   for item1 in soup.find_all("td"):
       tmp=item1.text
       print(tmp)
 #  number_of_day = item.text
   #number_of_day.next()
  # nof=number_of_day.text
 #  print(number_of_day)




    

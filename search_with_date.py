from datetime import date, datetime
import re

def searh_in_all(date):
    file = open("dataset.csv", "r")
    for row in file:
        new_date = re.search(r"\d{2}\-\d{2}\-\d{4}", row)
        if date==new_date:
            print(row)
            return 0
    print(None)

def search_in_year(date):
    file = open()

searh_in_all()
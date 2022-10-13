from datetime import date
import datetime
import re
import os

def search(file, date):
    for row in file:
        new_date = re.search(r"\d{2}\-\d{2}\-\d{4}", row)
        year = re.search(r"\d{4}", new_date[0])
        day = re.search(r"\b\d{2}",new_date[0])
        month = re.search(r"\-\d{2}\-",new_date[0])
        month = month[0].replace('-','')
        if date==datetime.date(int(year[0]), int(month), int(day[0])):
            print(row)
            return 0
    return 1

def searh_in_all(date):
    flag=0
    file = open("dataset.csv", "r")
    flag = search(file,date)
    file.close
    if flag==1:
        print(None)

def search_in_year(date):
    flag = 0
    for row in os.listdir('2'):
        file = open(os.path.join("2",row), "r")
        flag = search(file,date)
        file.close
        if flag==0:break
    if flag==1:
        print(None)

def search_in_week(date):
    flag = 0
    for row in os.listdir('3'):
        file = open(os.path.join("3",row), "r")
        flag = search(file,date)
        file.close      
        if flag==0:break      
    if flag==1:
        print(None)

def searh_in_data_and_date(date):
    count =0
    flag =0
    file_date = open(os.path.join("1","file_with_date.csv"), 'r')
    for row in file_date:
        count+=1
        new_date = re.search(r"\d{2}\-\d{2}\-\d{4}", row)
        year = re.search(r"\d{4}", new_date[0])
        day = re.search(r"\b\d{2}",new_date[0])
        month = re.search(r"\-\d{2}\-",new_date[0])
        month = month[0].replace('-','')
        if date==datetime.date(int(year[0]), int(month), int(day[0])):
            flag=1
            break
    file_date.close
    if flag==0:
        print(None)
        return 0
    file_data= open (os.path.join("1","file_with_data.csv"), "r") 
    for row in file_data:
        count-=1
        if count==0: 
            print(row)
            file_data.close
            return 1
    file_data.close

def next(count):
    file = open("dataset.csv", "r")
    data = []
    for row in file:
        data.append(row)
    print(data[count])
    file.close
    count+=1
    return count

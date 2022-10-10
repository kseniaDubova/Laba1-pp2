import re
import os

def creade_file(start,end,data):
    name_of_file=os.path.join("3",str(start)+"_"+str(end)+".csv")
    out_file = open(name_of_file,'w+')
    for param in data:
        out_file.write(param)
    out_file.close
    
def create(data):
    start = re.search(r"\d.*\d{4}", data[0])
    start = start[0].replace("-", "")
    end = re.search(r"\d.*\d{4}", data[len(data)-1])
    end = end[0].replace("-", "")
    creade_file(start,end,data)

def separation(data, day):
    new_data=[]
    for row in data:
        a = re.search(r"\d{1,2}", row)
        if a[0]!=str(day):
            new_data.append(row)
        else: return new_data

def create_for_first(data):
    new_data = []
    count = 0
    while count < 4:
        new_data.append(data[0])
        data.pop(0)
        count+=1
    return new_data

def clean_data(data):
    count = 0
    if len(data)>=7:
            while count!=7:
                data.pop(0)
                count+=1
    else: 
        while len(data)!=0:
            data.pop(0)

def chouse_day(data):
    if len(data)>=7:
        last_day= re.search(r"\d{1,2}", data[7])   
    else: 
        last_day= re.search(r"\d{1,2}", data[len(data)-1])
    return last_day


def main():
    data = []
    our_file = open("dataset.csv", "r")
    for param in our_file:
        data.append(param)
    create(create_for_first(data))
    last_day= re.search(r"\d{1,2}", data[7])
    #print(last_day[0])
    while len(data)!=1:
        new_data = separation(data, last_day[0])
        create(new_data)
        clean_data(data)
        last_day = chouse_day(data)

if __name__ == "__main__":
    main()
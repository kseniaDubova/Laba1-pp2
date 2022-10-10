import csv
import os



def separation(file):
    data=[]
    out_file = open(file,'r')
    with out_file as f:
        reader = csv.reader(f)
        for row in reader:
            for word in row:
                data.append(word)
    out_file.close
    return data


def print_in_files(main_list):
    file_of_date = open (os.path.join("1","file_with_date.csv"), 'w')   
    file_of_over = open (os.path.join("1","file_with_data.csv"), "w") 
    count = 0
    for number in main_list:
        if count==0:
            file_of_date.write(number+"\n")
        else:
            if (count==6):
                file_of_over.write(number+"\n")
            else:
                file_of_over.write(number)
        count += 1
        if count == 7:
            count = 0
    file_of_date.close
    file_of_over.close

def main():
    data = separation("dataset.csv")
    print_in_files(data)

if __name__ == "__main__":
    main()
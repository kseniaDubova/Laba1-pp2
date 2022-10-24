import re
import os


def creade_file(start, end, data):
    name_of_file = os.path.join("2", str(start) + "_" + str(end) + ".csv")
    out_file = open(name_of_file, "w+")
    for param in data:
        out_file.write(param)
    out_file.close


def create(data):
    start = re.search(r"\d.*\d{4}", data[0])
    start = start[0].replace("-", "")
    end = re.search(r"\d.*\d{4}", data[len(data) - 1])
    end = end[0].replace("-", "")
    creade_file(start, end, data)


def separation(data, year):
    new_data = []
    for row in data:
        a = re.search(r"\d{4}", row)
        if a[0] == str(year):
            new_data.append(row)
    return new_data


def main():
    data = []
    our_file = open("dataset.csv", "r")
    for param in our_file:
        data.append(param)
    year = 2008
    while year < 2023:
        new_data = separation(data, year)
        create(new_data)
        # print(new_data)
        year += 1


if __name__ == "__main__":
    main()

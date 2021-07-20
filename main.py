import csv
import pandas as pd
from itertools import permutations
import os

# Creating the Folder inside c drive

path = 'C:\Data'

def pathchecking():
    if os.path.exists(path):
        print("-------")
    else:
        os.mkdir(path)




# Checking if excel sheet is opened

def Input():
    while True:
        try:
            count = int(input("Enter Number of Elements"))
            break
        except ValueError:
            print("Please type the integer !!! Max digit upto 9")
    l = []
    R = []

    if count >= 2:
        for i in range(count):
            Question1st = input("Enter {0} Element name ".format(i + 1))
            l.append(Question1st)
        # Displaylist()

    else:
        A1 = input("Type the bonus that can be trigger on base game")
        l.append(A1)

    Perm = permutations(l)

    return Perm





# print(l)
P=Input()

# Creating the data into csv file or excel sheet

def write_in_csv():
    with open('books.csv', mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quotechar='_')

        for row in list(P):
            csv_writer.writerow(row)
            # print(row)

    # print(rename)


def error_message():
    rename = 'C:\\Data\\' + input("Enter Filename that you want to save") + '.csv'
    while True:  # repeat until the try statement succeeds
        try:
            websites = pd.read_csv('books.csv', header=None)
            websites.to_csv(rename, index=1)
            print("Excel sheet has been created " + rename)
            break
        except PermissionError:
            input("Could not abe to run script! Please close Excel and Press Enter to retry.")





if __name__=="__main__":
    pathchecking()
    Input
    write_in_csv()
    error_message()

































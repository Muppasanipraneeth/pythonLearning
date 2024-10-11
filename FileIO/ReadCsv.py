# this file is to read the csv file 

with open("Student.csv") as file:
    for line in file:
        name,house =line.rstrip().split(",")
        print(f"{name} is in the {house}")
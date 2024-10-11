import csv 
name=input("enter the name")
place=input(" enter the place")
with open("writeCsv.csv","a") as file :
    write=csv.writer(file)
    write.writerow([name,place])
    

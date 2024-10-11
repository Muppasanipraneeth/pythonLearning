# students=[]
# with open("student.csv") as file:
#     for line in file:
#         name,place=line.rstrip().split(",")
#         students.append(f"{name } is in the {place}")

# print(sorted(students))
# students=[]

# with open ("student.csv") as file:
#     for line in file :
#         name,place=line.rstrip().split(",")
#         student={"name":{name},"place":[place]}
#         students.append(student)

# for student in sorted(students ,key=lambda student :student["name"] ):
#     print(f"{student['name'] } is in {student['place']}")

# import csv # this is for the if the data is in the formated by the comma or the ""
# students=[]
# with open("student.csv") as file :
#     reader=csv.reader(file)
#     for name,place in reader :
#      students.append({"name":{name},"place":{place}})


# for student in sorted(students ,key=lambda student :student["name"] ):
#     print(f"{student['name'] } is in {student['place']}")

# we can also use the dicReader()

import csv # this is for the if the data is in the formated by the comma or the ""
students=[]
with open("student.csv") as file :
    reader=csv.DictReader(file)
    for row in reader :
     students.append({"name":row['name'],"place":row['place']})


for student in sorted(students ,key=lambda student :student["name"] ):
    print(f"{student['name'] } is in {student['place']}")
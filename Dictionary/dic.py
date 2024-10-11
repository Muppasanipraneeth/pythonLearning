students={
    "hermonie":"Griffindore",
    "harry":"Griffindore",
    "ron":"Griffindore",
    "Darco":"Slythernie"
}
print(students["harry"])
for student in students :
    print(student,students[student],sep=" : ")
student1=[
    {"name":"praneeth","age":"22","place":"kurnool"},
    {"name":"bhanu","age":"21","place":"kadapa"},
    {"name":"narendra","age":"23","place":"kurnool"},
]
for student in student1 :
    print(student["name"], student["age"],student["place"],sep=",")
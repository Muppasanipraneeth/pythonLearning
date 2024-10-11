# take the input from the user
name = input("what's your name   ").strip().title()
# this strip funtcion removes the gaps in the str 
# this title is used for the convert the each word as camel case
age=input("Enter your age ")
# hey to remove the new line end= "/n" this is default we change with end =""
#print("HEY",end="")
print("Hello  ",name,age)
print(f"Hello, {name}")
# using the split 
first ,last =name.split()
print(f" First Name,{first} and the Last Name  {last}")


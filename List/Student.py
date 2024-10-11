def main():
    students=["praneeth","Ram","Raj"]
    # here we cannot use the range we should use the in that's it
    print(" this is printing in the 1 way")
    for student in ( students):
        print(student)
    # another way of for the for loop
    print(" this is printing in another way")
    for i in range(len(students)):
        print(students[i])
    name="praneeth"
    # printing the character of the String
    
    for ch in range (len(name)):
        print(f"{name[ch]}") 



main()    
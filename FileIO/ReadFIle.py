# to read the file we will use the with open ("file_name","r") as file
with open("names.txt","r") as file:
    lines=file.readlines()

for line in lines :
    print(f"Hello {line}",end="")
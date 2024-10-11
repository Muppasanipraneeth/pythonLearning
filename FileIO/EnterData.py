name =input("enter the name ?")
# open will open the file and write in it
#file =open("names.txt","w")
#file =open("names.txt","a") this is for the appened
#file =open ("names.txt","a")
 
#file.write(f"{name} \n" ) wirte names in the file  and here in this case the file just appneded  no new line
#file.close() # this will close the file

# to auotmatically open and close the file we will use the With 
with open("names.txt","a") as file :
    file.write(f"{name} \n")
def insertion (array):
    for i in range(1,len(array)):
        current=array[i]
        prev=i-1
        while(prev>=0 and array[prev]>current):
            array[prev+1]=array[prev]
            prev=prev-1
        array[prev+1]=current

def printArr(array):
    for i in range(0,len(array)):
        print(array[i],end="")


if __name__ == "__main__":
 array=[5,3,2,1,0]
 insertion(array)
 printArr(array)
 print(array)
 

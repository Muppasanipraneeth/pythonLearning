# ****
"""
*
*
*

"""

def main():
    col(4)
    row(4)   
    square(4)



def square(s):
    for i in range(s):
        for j in range(s):
            print("* ",end=" ")
        print()
         
        


def row(r):
    for l in range(r):
        print("* \n" ,end="")
     

def col(a):
    for i in range(a):
        print("* ",end="")
     

main()
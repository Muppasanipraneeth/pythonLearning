def main() :
        x=int (input("Enter the value of the x ? "))
        y=int (input("Enter the value of the y ? "))
        check(x,y)


def check(x,y):

    if(x>y):
          print("X is greater than Y")
    else:
          print("Y is greater than X")

main()
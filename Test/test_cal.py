from Calculator import square 


def main():
    test_square()

# def test_square():
#     if(square(2)!=4):
#         print(" the square of 2 is 4 done something worng")
#     if(square(3)!=9):
#         print(" the square of 3 is 9 done something worng")
def test_square():
    try :
        assert square(2)==4
    except AssertionError :
        print(" the square 2 was not 4")
    try :
        assert square(3)==9
    except AssertionError :
        print(" the square of the 3 is not 9")

if __name__=="__main__" :
    main()


# pytest is used for the testing the python 

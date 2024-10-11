from Calculator import square
def main ():
    test_square()
    test_negitve()
    test_postive()
    test_zero()

def test_square():
    assert square(2)==4 
    assert square(3)==9
    assert square(-2)==4
    assert square(-3)==9
    assert square(0)==0
def test_postive():
    assert square(2)==4
    assert square(4)==16
    assert square(10)==100

def test_negitve():
    assert square(-1)==1
    assert square(-2)==4
    assert square(-3)==9

def test_zero():
    assert square(0)==0
if __name__ =="__main__":
    main()
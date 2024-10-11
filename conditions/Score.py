def main():
    score=int( input("Enter the Score "))
    print(checkGrade(score))


def checkGrade(score):
    if(score>90 and score<=100):
        return "EX"
    elif(score>80 and score<=90) :
        return "A"   
    elif(score>70 and score<=80) :
        return "B"   
    elif(score>60 and score<=70) :
        return "C"   
    elif(score>50 and score<=60) :
        return "D"   
    else :
        return "R"
main() 
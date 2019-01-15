while(1):
    a=float(input("enter your first value:- "))
    b=float(input("enter your second value:- "))
    operator =input("Enetr the operator: ")
    if (operator == "+"):
        print("The adition of",a,"and",b,"is",a+b)
    elif (operator =="-"):
        print("the subtraction of",a,"and",b,"is",a-b)
    elif (operator =="*"):
        print("the multipaction of",a,"and",b,"is",a*b)
    elif (operator =="/"):
        print("the division of",a,"and",b,"is",a/b)
    else:
        print("the operator is invalid")



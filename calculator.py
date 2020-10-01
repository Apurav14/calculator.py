while(1):
    a=float(input("enter your first value:- "))
    b=float(input("enter your second value:- "))
    operator =input("Enter the operator: ")
    if (operator == "+"):
        print("The addition of",a,"and",b,"is",a+b)
    elif (operator =="-"):
        print("the subtraction of",a,"and",b,"is",a-b)
    elif (operator =="*"):
        print("the multiplication of",a,"and",b,"is",a*b)
    elif (operator =="/"):
        print("the division of",a,"and",b,"is",a/b)
    else:
        print("the operator is invalid")



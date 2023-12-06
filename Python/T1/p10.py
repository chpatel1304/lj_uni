a=int(input("Enter Number A "))
b=int(input("Enter Number B "))
c=input("Enter operation ")
if c=='+':
    print("Sum :",a+b)
elif c=='-':
    print("Difference :",a-b)
elif c=='*':
    print("Multiply :",a*b)
elif c=='/':
    print("Division :",a/b)
else:
    print("Invalid Input")

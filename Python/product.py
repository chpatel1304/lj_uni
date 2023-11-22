n=int(input("Enter Single digit number "))
if n<0 or n>9:
    print("Enter Only Single Digit")
else:
    for i in range (100000,1000000):
        product=1
        for d in str(i):
            product*=int(d)
        if product==n:
            print(i)
    

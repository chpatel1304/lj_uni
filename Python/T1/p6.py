a=int(input("Enter Three Digit Number "))
sum=0
n=a%10
sum=sum+n
a=a//10
n=a%10
sum=sum+n
a=a//10
n=a%10
sum=sum+n
print("Sum :",sum)

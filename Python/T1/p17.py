#wap to check entered number by user is palindorme or not
d=0
a=int(input("Enter Number : "))
b=a
while a!=0:
    d=d*10+a%10
    a=a//10
if b==d:
    print("palidrone")
else:
    print("Not palidrone")

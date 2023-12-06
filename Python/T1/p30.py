min=0
max=0
avg=0
sum=0
count=0
while True:
    a=input("Enter Numbers ")
    if a=='done'or a=='Done':
        break
    else:
        if count==0:
            max=int(a)
            min=int(a)
        if(max<int(a)):
           max=int(a)
        if(min>int(a)):
            min=int(a)
        sum+=int(a)
        count+=1

avg=sum/count
print("Max ",max)
print("Min ",min)
print("Avg ",avg)

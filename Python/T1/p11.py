d=int(input("Enter Day"))
m=int(input("Enter Month"))
y=int(input("Enter Year"))
print("Entered Date : ",d,"-",m,"-",y)
if (m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
    max=31
elif (m==4 or m==6 or m==9 or m==11):
    max=30
elif (y%4==0 and y%100!=0) or y%400==0:
    max=29
else:
    max=28

if (m<0 or m>12):
    print("Invalid")
elif (d<0 or d>max):
    print("Invalid")
elif (y<0):
    print("Invalid")
elif (d==max and m==12):
    d=1
    m=1
    y=y+1
elif (d==max and m!=12):
    d=1
    m=m+1
else:
    d=d+1
print("Plus One Date : ",d,"-",m,"-",y)

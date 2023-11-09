#wap to check enter numbered is disarium number or not
def calculateLength(n):    
    length = 0;    
    while(n != 0):    
        length = length + 1;    
        n = n//10;    
    return length;    

num = 518;    
rem = sum = 0;    
len = len(str(num))         
n = num;    

while(num > 0):    
    rem = num%10;    
    sum = sum + int(rem**len);    
    num = num//10;    
    len = len - 1;    
     
if(sum == n):    
    print(str(n) + " is a disarium number");    
else:    
    print(str(n) + " is not a disarium number");    

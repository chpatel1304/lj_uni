n=123456
c=0
temp=n
while temp>0:
    temp//=10
    c=c+1
if c>1:
    f_d=n//10**(c-1)
    l_d=n%10
    n_without_f_l=(n%10**(c-1))//10
    swappped_no=l_d*(10**(c-1))+n_without_f_l*10+f_d
    print(swappped_no)
else:
    print(n)

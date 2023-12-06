c=0
f_l=None
s_l=None
while(True):
    n=input("Enter Number : ")
    if n=='done':
        break
    n=int(n)
    if n<0 or n>100:
        break
    c=c+1
    if f_l is None or n<f_l:
        s_l=f_l
        f_l=n
    elif s_l is None or n<s_l:
        s_l=n
print(f_l,s_l)

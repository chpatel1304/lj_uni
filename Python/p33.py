c=0
f_h=-1
s_h=-1
while(True):
    n=input("Enter Numbers :")
    if n=='done':
        break
    n=int(n)
    if n<0 or n>100:
        break
    c=c+1
    if n>f_h:
        s_h=f_h
        f_h=n
    elif n>s_h and n!=f_h:
        s_h=n
print(f_h)
print(s_h)

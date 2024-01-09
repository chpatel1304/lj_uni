f=open("b.txt","r")
l=[]
def text_line(a):
    if len(a)<=80:
        l.append(a)
    else:
        if a[79]==" ":
            l.append(a[:79])
            text_line(a[80:])
        elif a[79] !=" ":
            x=a.rfind(' ',0,79)
            l.append(a[:x])
            text_line(a[x+1:])
            
for i in f:
    if len(i)<=80:
        l.append(i)
    else:
        text_line(i)
    
f1=open("d.txt","w")
for j in l :
    if j[-1]=='':
        j=j[:-1]+'\n'
    else:
        j+='\n'
    f1.write(j)
        

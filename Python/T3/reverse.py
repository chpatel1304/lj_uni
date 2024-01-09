#wapp to read data from file and reverser the words starts form i
r=open("a.txt","r+")
s=""
while True:
    d=r.readline()
    if not d:
        break
    else:
        m=d.split()
        for i in m:
            if i[0]=="i" or i[0]=="I":
                s=s+' '+i[::-1]
            else:
                s=s+' '+i
        print(s)
        
    

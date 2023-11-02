def star():
    print("***************************************")

for i in range (1,10):
    print("*"*i)
star()
for i in range (1,10):
    print(" "*(9-i),"*"*i)
star()
for i in range (1,10):
    print(" "*(9-i)," *"*i)
star()
for i in range (9,0,-1):
    print(" "*(9-i)," *"*i)
star()
for i in range (9,0,-1):
    print(" "*(9-i),"*"*i)
star()
for i in range (1,10):
    for j in range (1,i+1):
        print(j,end="")
    print()
star()
for i in range (1,10):
    for j in range (1,i+1):
        print(i,end="")
    print()
star()


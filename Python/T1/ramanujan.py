for i in range (1,5000):
    max_n=int(i**(1/3)+1)
    for a in range (1,max_n):
        for b in range (1,max_n):
            for c in range (1,max_n):
                for d in range (1, max_n):
                    if a**3+b**3==i and c**3+d**3==i and a!=b and a!=c and a!=d and b!=c and b!=d and c!=d:
                        print(i)

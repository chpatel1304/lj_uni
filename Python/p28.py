def add (sum,a):
    return sum+a
def adding(days,sum,week):
    for i in range (0,7):
        if(days>14):
            return sum
        sum=add(sum,week+i)
        days+=1
    week+=1
    return adding(days,sum,week)

print(adding(1,0,1))

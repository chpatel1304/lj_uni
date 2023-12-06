#wap to calcuate sum and average of digits prsent in given string 
s="xyz12pq8905A7"
sum=0
c=0
for i in s:
    if i.isdigit():
        i=int(i)
        sum+=i
        c=c+1
avg=int(sum/c)
print(sum,"    ",avg)

cents=int(input("Enter Cents"))
print("Cents : ",cents)
q=0
di=0
ni=0
p=0
q=cents//25
rem=cents%25
di=rem//10
rem=rem%10
ni=rem//5
rem=rem%5
p=rem
print(q," Quatres ",di," Denny ",ni," Ni ",p," penny")


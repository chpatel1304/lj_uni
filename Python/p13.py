type=input("Enter TYpe Of Vehcile : ")
e_hr=int(input("Enter Entering hour "))
e_mi=int(input("Enter Entering minute "))
if e_hr<0 or e_mi<0 or e_hr>24 or e_mi>61:
    print("Inavlid Entrey ")
    exit
x_hr=int(input("Enter Exiting hour "))
x_mi=int(input("Enter Exiting minute "))
if x_hr<0 or x_mi<0 or x_hr>24 or x_mi>61:
    print("Inavlid Entrey ")
    exit
total_hr=x_hr-e_hr
total_min=x_mi-e_mi
if total_hr<0 or total_min<0:
    print("Invalid Data Entry")
    exit
print("Entry Time : ",e_hr,":",e_mi)
print("Exit Time : ",x_hr,":",x_mi)
print("Total Time : ",total_hr,":",total_min)
fare=0
if total_hr<3 and total_mi<60:
    if type=='car':
        fare+=10
    elif type=='truck':
        fare+=20
    elif type=='two-wheeler':
        fare+=5
    else:
        print("Invalid Type Of vehcile")
        exit
else:
    if type=='car':
        fare+=20
    elif type=='truck':
        fare+=30
    elif type=='two-wheeler':
        fare+=10
    else:
        print("Invalid Type Of vehcile")
        exit
print("Fare : ",fare)
    
    

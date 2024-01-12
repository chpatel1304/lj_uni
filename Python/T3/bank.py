class Bank_account:
    def __init__ (self,acc_num,name,balance):
        self.acc_num=acc_num
        self.name=name
        self.balance=balance

    def depoist(self,amount):
        if amount<0:
            print("Negative Amount Cant Be added")
        else:
            self.balance=amount+self.balance
            print("Upadted Balance After Deposit :",self.balance)


    def withdrawl(self,amount):
        if amount>self.balance or amount<0:
            print("Insufficent Balance !")
        else:
            self.balance=self.balance-amount
            print("Upadted Balance After Withhdrwal :",self.balance)
        
    def display(self):
        print("Name : ",self.name)
        print("Acc Num : ",self.acc_num)
        print("Balance : ",self.balance)

num=int(input("Enter Account Number : "))
name=input("Enter Name:  ")
n=int(input("Enter Balance : "))

b=Bank_account(num,name,n)
while True:
    print("1. For Depositing ")
    print("2. For Withdrawling ")
    print("3. For Information about Account ")
    print("4. For Exit ")
    n=int(input("Enter What You Want to do ? "))
    if n==1:
        d=int(input("Enter How Many Amount You Want Depoist ?"))
        b.depoist(d)
        continue
    elif n==2:
        w=int(input("Enter How Many Amount You Want withdrwal ?"))
        b.withdrawl(w)
        continue
    elif n==3:
        b.display()
        continue
    elif n==4:
        print("Thank you !")
        break
    else:
        print("Invalid Input !")
        continue

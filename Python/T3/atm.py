class ATM:
    pin=0
    balance=0
    def menu(self):
        while True:
            print("Welcome To ATM !")
            print("1.Press 1 to create Pin")
            print("2.Press 2 to change Pin")
            print("3.Press 3 to chechk balnce ")
            print("4.Press 4 to withdraw")
            print("5. Press 5 to deposit ")
            print("Anything else to enter")
            n=int(input("Enter your Choice ?"))
            if n==1:
                self.create_pin()
            elif n==2:
                self.change_pin()
            elif n==3:
                self.display()
            elif n==4:
                amount=int(input("Enter Your Amount "))
                self.withdrawl(amount)
            elif n==5:
                amount=int(input("Enter Your Amount "))
                self.depoist(amount)
            else:
                print("Thank You For Using ATM !")
                break

    def depoist(self,amount):
        u_pin=int(input("Enter Your Pin " ))
        if self.pin==u_pin:
            if amount<0:
                print("Negative Amount Cant Be added")
            else:
                self.balance=amount+self.balance
                print("Upadted Balance After Deposit :",self.balance)
        else:
            print("Enter Valid Pin !")

    def withdrawl(self,amount):
        u_pin=int(input("Enter Your Pin " ))
        if self.pin==u_pin:
            if amount>self.balance or amount<0:
                print("Insufficent Balance !")
            else:
                self.balance=self.balance-amount
                print("Upadted Balance After Withhdrwal :",self.balance)
        else:
            print("Enter Valid Pin !")

            
    def display(self):
        u_pin=int(input("Enter Your Pin " ))
        if self.pin==u_pin:
            print("Balance : ",self.balance)
        else:
            print("Enter Valid Pin !")


    def create_pin(self):
        self.pin=int(input("Enter Your New Pin " ))
        print("Pin Set Successfully !")
        self.balance=int(input("Enter Your Balance " ))
        print("Balance Added Successfully !")

    def change_pin(self):
       
        while True:
            u_pin=int(input("Enter Your Pin " ))
            if self.pin==u_pin:
                    n_pin=int(input("Enter Your New Pin " ))
                    if n_pin==self.pin:
                        print("Please Set Different Pin Not as same old one")
                        continue
                    else:
                        self.pin=n_pin
                        print("Pin Changed Successfully !")
                        break
            else:
                print("Enter Valid Pin !")
                continue

a=ATM()
a.menu()
    
                
            
        
        

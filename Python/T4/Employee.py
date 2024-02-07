from abc import ABC,abstractmethod

class employee(ABC):
    def __init__(self):
        self.id=0
        self.name=""
        self.salary=0

    def getemp(self):
        id=int(input("Enter your Employee ID :"))
        name=input("Enter your Employee Name :")
        salary=int(input("Enter your Employee Salary :"))
        self.id=id
        self.name=name
        self.salary=salary

    def printEmp(self):
        print("ID : ",self.id)
        print("Name : ",self.name)
        print("Salary : ",self.salary)

    def getsalary(self):
        return self.salary

    @abstractmethod
    def emp_id(self):
        pass

class perks:
    def calperks(self):
        self.getemp()
        sal=self.getsalary()
        
    

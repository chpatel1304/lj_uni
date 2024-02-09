from tkinter import *
import mysql.connector
import tkinter.messagebox as msg

def create_conn():
    return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Python_project"
        )

def main():
    root=Tk()
    root.resizable(width=False,height=False)
    app=Window1(root)
    
class Window1:
    def __init__(self,r):
        self.r=r
        self.r.title("Hospital Login System ")
        self.r.geometry("350x450")
        self.r.config(bg="cornsilk2")
        
        self.l_id=Label(self.r,text="USER ID",bg="cornsilk2",fg="black")
        self.l_id.place(x=50,y=100)

        self.l_fname=Label(self.r,text="PASSWORD",bg="cornsilk2",fg="black")
        self.l_fname.place(x=50,y=140)

        self.e_id=Entry(self.r)
        self.e_id.place(x=150,y=100)

        self.e_fname=Entry(self.r)
        self.e_fname.place(x=150,y=140) 
        
        self.insert=Button(self.r,text="LOGIN",bg="azure2",fg="black",font=("Helvetica",10),command=self.new_window)
        self.insert.place(x=150,y=200)

    def new_window(self):
        self.newWindow=Toplevel(self.r)
        self.app=Window2(self.newWindow)
        
        

class Window2:
    def __init__(self,r):

        self.r=r
        self.r.title("Hospital Management System ")
        self.r.geometry("350x450")
        self.r.config(bg="blanchedalmond")
        self.r.resizable(width=False,height=False)

        self.home=Button(self.r,text="Home",bg="azure2",fg="black",font=("Helvetica",10),width=10,height=1)
        self.home.place(x=50,y=0)
        self.Exit=Button(self.r,text="EXIT",bg="red",fg="black",font=("Helvetica",10),width=10,height=1)
        self.Exit.place(x=200,y=0)
        
        
        self.addp=Button(self.r,text="Add Paitent",bg="azure2",fg="black",font=("Helvetica",10),width=10,height=1)
        self.addp.place(x=120,y=100)
        
        self.addD=Button(self.r,text="Add Doctor",bg="azure2",fg="black",font=("Helvetica",10),width=10,height=1)
        self.addD.place(x=120,y=150)
        
        self.cp=Button(self.r,text="Check Paitent",bg="azure2",fg="black",font=("Helvetica",10),width=10,height=1)
        self.cp.place(x=120,y=200)



main()

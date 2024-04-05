import tkinter as tk
from PIL import ImageTk,Image
import tkinter.messagebox as msg
import mysql.connector

class HospitalManagementSystem:

    def create_conn(self):
        
        #Database Connections
        return mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="python_project"
            )
#----------------------------------------------------------------------INIT METHOD -------------------------------------------------------------------------
    def __init__(self, master):
        
        self.master = master
        self.master.title("Harmony Health Center")
        self.master.geometry("450x450")
        self.master.resizable(width=False,height=False)

        self.login_frame = tk.Frame(self.master)
        self.login_frame.pack()

        #LOGO
        self.image=Image.open("aa.jpg")
        self.photo=ImageTk.PhotoImage(self.image)
        self.l1=tk.Label(self.login_frame,image=self.photo)
        self.l1.grid(row=15, columnspan=2, padx=10, pady=10)

        #USERNAME FOR RECEPTIONIST
        self.username_label = tk.Label(self.login_frame, text="Username:")
        self.username_label.grid(row=60, column=0, padx=1, pady=0)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=60, column=1, padx=5, pady=5)

        #PASSWORD FOR RECEPTIONIST
        self.password_label = tk.Label(self.login_frame, text="Password:")
        self.password_label.grid(row=80, column=0, padx=5, pady=5)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=80, column=1, padx=5, pady=5)

        #LOGIN BUTTON
        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.grid(row=100, columnspan=2, padx=5, pady=5)
        
#--------------------------------------------------------------------LOGIN METHOD ------------------------------------------------------------------------
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

     
        if username == "1" and password == "1":
            self.login_frame.destroy()
            self.create_main_menu()
        else:
          
            tk.messagebox.showerror("Error", "Invalid username or password")

#-----------------------------------------------------------------MAIN MENU METHOD -------------------------------------------------------------------------
    def create_main_menu(self):
        self.main_menu = tk.Menu(self.master)

        self.menu_frame = tk.Frame(self.master)
        self.menu_frame.pack()

        #LOGO
        self.image=Image.open("aa.jpg")
        self.photo=ImageTk.PhotoImage(self.image)
        self.l1=tk.Label(self.menu_frame,image=self.photo)
        self.l1.grid(row=15, columnspan=2, padx=10, pady=10)

        #OLD PAITENT BUTTON
        self.old_patient_button = tk.Button(self.menu_frame , text="OLD Patient", command=self.old_patient)
        self.old_patient_button .grid(row=100, columnspan=4, padx=5, pady=5)

        #NEW PAITENT BUTTON
        self.new_patient_button = tk.Button(self.menu_frame , text="NEW Patient", command=self.new_patient)
        self.new_patient_button .grid(row=120, columnspan=4, padx=5, pady=5)

        #ADD DOCTOR BUTTON
        self.add_doctor_button = tk.Button(self.menu_frame , text="Add Doctor", command=self.add_doctor)
        self.add_doctor_button .grid(row=140, columnspan=4, padx=5, pady=5)

        #SHOW PAITENT DETAILS BUTTON
        self.check_patient_button = tk.Button(self.menu_frame , text="Show Patient Details", command=self.check_patient)
        self.check_patient_button .grid(row=160, columnspan=4, padx=5, pady=5)

        #SHOW DOCTOR DETAILS BUTTON
        self.check_doctor_button = tk.Button(self.menu_frame , text="Show Doctor Details", command=self.check_doctor)
        self.check_doctor_button .grid(row=180, columnspan=4, padx=5, pady=5)

#--------------------------------------------------------------------OLD PAITENT METHOD---------------------------------------------------------------------

    def old_patient(self):
        
        self.menu_frame.destroy()
        self.old_p = tk.Menu(self.master)

        self.old_p_frame= tk.Frame(self.master)
        self.old_p_frame.pack()

        #LOGO
        self.image=Image.open("aa.jpg")
        self.photo=ImageTk.PhotoImage(self.image)
        self.l1=tk.Label(self.old_p_frame,image=self.photo)
        self.l1.grid(row=15, columnspan=2, padx=10, pady=10)

        #OLD PAITENT ID
        self.old_paitent_id=tk.Label(self.old_p_frame,text="Paitent ID :")
        self.old_paitent_id.grid(row=30,column=0,padx=5,pady=5)
        self.old_paitent_id_entry=tk.Entry(self.old_p_frame)
        self.old_paitent_id_entry.grid(row=30,column=1,padx=5,pady=5)

        #OLD PAITENT NAME
        self.old_paitent_name=tk.Label(self.old_p_frame,text="Paitent Name :")
        self.old_paitent_name.grid(row=35,column=0,padx=5,pady=5)
        self.old_paitent_name_entry=tk.Entry(self.old_p_frame)
        self.old_paitent_name_entry.grid(row=35,column=1,padx=5,pady=5)

        #OLD PAITENT DOB
        self.old_paitent_dob=tk.Label(self.old_p_frame,text="Paitent DOB :")
        self.old_paitent_dob.grid(row=40,column=0,padx=5,pady=5)
        self.old_paitent_dob_entry=tk.Entry(self.old_p_frame)
        self.old_paitent_dob_entry.grid(row=40,column=1,padx=5,pady=5)

        #OLD PAITENT NUMBER
        self.old_paitent_num=tk.Label(self.old_p_frame,text="Phone Number :")
        self.old_paitent_num.grid(row=45,column=0,padx=5,pady=5)
        self.old_paitent_num_entry=tk.Entry(self.old_p_frame)
        self.old_paitent_num_entry.grid(row=45,column=1,padx=5,pady=5)

        #OLD PAITENT DISEASE
        self.old_paitent_d=tk.Label(self.old_p_frame,text="Paitent Disease:")
        self.old_paitent_d.grid(row=50,column=0,padx=5,pady=5)
        self.old_paitent_d_entry=tk.Entry(self.old_p_frame)
        self.old_paitent_d_entry.grid(row=50,column=1,padx=5,pady=5)

        #OLD PAITENT DOCTOR
        self.old_paitent_dr=tk.Label(self.old_p_frame,text="Paitent Doctor:")
        self.old_paitent_dr.grid(row=55,column=0,padx=5,pady=5)
        self.old_paitent_dr_entry=tk.Entry(self.old_p_frame)
        self.old_paitent_dr_entry.grid(row=55,column=1,padx=5,pady=5)

        #OLD PAITENT PENDING AMOUNT
        self.old_paitent_ppa=tk.Label(self.old_p_frame,text="Pending Amount :")
        self.old_paitent_ppa.grid(row=60,column=0,padx=5,pady=5)
        self.old_paitent_ppa_entry=tk.Entry(self.old_p_frame)
        self.old_paitent_ppa_entry.grid(row=60,column=1,padx=5,pady=5)

        #OLD PAITENT SEARCH BUTTON
        self.old_paitent_search=tk.Button(self.old_p_frame,text="Search Paitent",command=self.search_old_paitent)
        self.old_paitent_search.grid(row=70,column=0,padx=5,pady=5)

        #OLD PAITENT UPDATE BUTTON
        self.old_paitent_update=tk.Button(self.old_p_frame,text="Update Details",command=self.update_old_paitent)
        self.old_paitent_update.grid(row=70,column=1,padx=5,pady=5)

        #BACK BUTTON
        self.back = tk.Button(self.old_p_frame, text="BACK",command=self.destory_old_patient)
        self.back.grid(row=75, columnspan=2, padx=5, pady=5)

#--------------------------------------------------------------------OLD PAITENT SEARCH METHOD ---------------------------------------------------------------------

    def search_old_paitent(self):
        if self.old_paitent_num_entry.get()=="":
            msg.showinfo("Search Status","Mobile Number  Is Mandatory")
        else:
            self.conn=self.create_conn()
            self.cursor=self.conn.cursor()
            self.q="select * from paitent where pnum=%s"
            self.args=(self.old_paitent_num_entry.get(),)
            self.cursor.execute(self.q,self.args)
            self.row=self.cursor.fetchall()
            if self.row:
                for i in self.row:
                    self.old_paitent_id_entry.insert(0,i[0])
                    self.old_paitent_name_entry.insert(0,i[1])
                    self.old_paitent_dob_entry.insert(0,i[2])
                    #self.old_paitent_num_entry.insert(0,i[3])
                    self.old_paitent_d_entry.insert(0,i[4])
                    self.old_paitent_dr_entry.insert(0,i[5])
                    self.old_paitent_ppa_entry.insert(0,i[7])
            else:
                msg.showinfo("Search Status","Mobile Number is not found")
            self.conn.close()

#--------------------------------------------------------------------OLD PAITENT UPDATE METHOD---------------------------------------------------------------------

    def update_old_paitent(self):
        
        if self.old_paitent_id_entry.get()=="" or self.old_paitent_name_entry.get()=="" or self.old_paitent_dob_entry.get()=="" or self.old_paitent_num_entry.get()=="" or self.old_paitent_d_entry.get()=="" or self.old_paitent_dr_entry.get()=="" or self.old_paitent_ppa_entry=="":
            msg.showinfo("Update Status","All Fields Are Mandatory")
        else:
            self.conn=self.create_conn()
            self.cursor=self.conn.cursor()
            self.q="update paitent set id=%s,pname=%s,pdob=%s,pnum=%s,pd=%s,dname=%s,ppa=%s where pnum=%s"
            self.args=(self.old_paitent_id_entry.get(),self.old_paitent_name_entry.get(),self.old_paitent_dob_entry.get(),self.old_paitent_num_entry.get(),self.old_paitent_d_entry.get(),self.old_paitent_dr_entry.get(),self.old_paitent_ppa_entry.get(),self.old_paitent_num_entry.get())
            self.cursor.execute(self.q,self.args)
            self.conn.commit()
            self.conn.close()
            msg.showinfo("Update Status","Data Updated Succesfully !")
            self.destory_old_patient()

#--------------------------------------------------------------------OLD PAITENT DESTROY METHOD---------------------------------------------------------------------

    def destory_old_patient(self):
        self.old_p_frame.destroy()
        self.create_main_menu()

#--------------------------------------------------------------------NEW PAITENT METHOD---------------------------------------------------------------------
        
    def new_patient(self):
        
        self.menu_frame.destroy()
        self.new_p = tk.Menu(self.master)

        self.new_p_frame= tk.Frame(self.master)
        self.new_p_frame.pack()

        #LOGO
        self.image=Image.open("aa.jpg")
        self.photo=ImageTk.PhotoImage(self.image)
        self.l1=tk.Label(self.new_p_frame,image=self.photo)
        self.l1.grid(row=15, columnspan=2, padx=10, pady=10)

        #NEW PAITENT ID
        self.new_paitent_id=tk.Label(self.new_p_frame,text="Paitent ID :")
        self.new_paitent_id.grid(row=30,column=0,padx=5,pady=5)
        self.new_paitent_id_entry=tk.Entry(self.new_p_frame)
        self.new_paitent_id_entry.grid(row=30,column=1,padx=5,pady=5)

        #NEW PAITENT NAME
        self.new_paitent_name=tk.Label(self.new_p_frame,text="Paitent Name :")
        self.new_paitent_name.grid(row=35,column=0,padx=5,pady=5)
        self.new_paitent_name_entry=tk.Entry(self.new_p_frame)
        self.new_paitent_name_entry.grid(row=35,column=1,padx=5,pady=5)

        #NEW PAITENT DOB
        self.new_paitent_dob=tk.Label(self.new_p_frame,text="Paitent DOB (DD/MM/YYYY) :")
        self.new_paitent_dob.grid(row=40,column=0,padx=5,pady=5)
        self.new_paitent_dob_entry=tk.Entry(self.new_p_frame)
        self.new_paitent_dob_entry.grid(row=40,column=1,padx=5,pady=5)
        
        #NEW PAITENT NUMBER
        self.new_paitent_num=tk.Label(self.new_p_frame,text="Phone Number :")
        self.new_paitent_num.grid(row=45,column=0,padx=5,pady=5)
        self.new_paitent_num_entry=tk.Entry(self.new_p_frame)
        self.new_paitent_num_entry.grid(row=45,column=1,padx=5,pady=5)

        #NEW PAITENT DISEASE
        self.new_paitent_d=tk.Label(self.new_p_frame,text="Paitent Disease :")
        self.new_paitent_d.grid(row=50,column=0,padx=5,pady=5)
        self.new_paitent_d_entry=tk.Entry(self.new_p_frame)
        self.new_paitent_d_entry.grid(row=50,column=1,padx=5,pady=5)

        doctor_names=self.fetch_dr()
        # DOCTOR DROPDOWN MENU
        self.doctor_label = tk.Label(self.new_p_frame, text="Select Doctor:")
        self.doctor_label.grid(row=55, column=0, padx=5, pady=5)
        self.doctor_var = tk.StringVar(self.new_p_frame)
        self.doctor_var.set(doctor_names[0])
        self.doctor_dropdown = tk.OptionMenu(self.new_p_frame, self.doctor_var, *doctor_names)
        self.doctor_dropdown.grid(row=55 , column=1, padx=5, pady=5)

        #NEW PAITENT FEES AMOUNT
        self.new_paitent_fees=tk.Label(self.new_p_frame,text="FEES :")
        self.new_paitent_fees.grid(row=60,column=0,padx=5,pady=5)
        self.new_paitent_fees_entry=tk.Entry(self.new_p_frame)
        self.new_paitent_fees_entry.grid(row=60,column=1,padx=5,pady=5)
        
        #NEW PAITENT AMOUNT PAID
        self.new_paitent_paid=tk.Label(self.new_p_frame,text="AMOUNT PAID :")
        self.new_paitent_paid.grid(row=70,column=0,padx=5,pady=5)
        self.new_paitent_paid_entry=tk.Entry(self.new_p_frame)
        self.new_paitent_paid_entry.grid(row=70,column=1,padx=5,pady=5)

        #NEW PAITENT ADD BUTTON
        self.new_paitent_add=tk.Button(self.new_p_frame,text="ADD Paitent",command=self.insert_patient)
        self.new_paitent_add.grid(row=75,column=0,padx=5,pady=5)

        #BACK BUTTON
        self.back = tk.Button(self.new_p_frame, text="BACK",command=self.destroy_new_patient)
        self.back.grid(row=75, column=1, padx=5, pady=5)

#--------------------------------------------------------------------NEW PAITENT INSERT METHOD---------------------------------------------------------------------

    def insert_patient(self):

        if self.new_paitent_name_entry.get()=="" or self.new_paitent_dob_entry.get()=="" or self.new_paitent_num_entry.get()=="" or self.new_paitent_d_entry.get()=="" or self.new_paitent_fees_entry.get()=="" or self.new_paitent_paid_entry.get()=="" :
            msg.showinfo("Add New Patient","All Fields are Mandatory !")
        else:
            pname=self.new_paitent_name_entry.get()
            pdob=self.new_paitent_dob_entry.get()
            pnum=self.new_paitent_num_entry.get()
            pd=self.new_paitent_d_entry.get()
            pf=self.new_paitent_fees_entry.get()
            paid=self.new_paitent_paid_entry.get()
            ppa=int(pf)-int(paid)
            dname = self.doctor_var.get()
            
            flag=0
            #FETCHING NUMBER LIST
            paitent_num_list=self.fetch_num_paitent()
            
            if pnum in paitent_num_list:
                flag=1
            else:
                flag=0
                
            if flag==1:
                
                if len(pnum)==10:
                    
                    if pnum[0]=="9" or pnum[0]=="8" or pnum[0]=="7" or pnum[0]=="6": 
                        
                        if pdob[2]=="/" and pdob[5]=="/":
                            
                            if pdob[0:2].isdigit() and pdob[3:5].isdigit() and pdob[6:].isdigit():
                                
                                self.conn=self.create_conn()
                                self.cursor=self.conn.cursor()
                                self.q="insert into paitent (pname,pdob,pnum,pd,dname,pf,ppa) values(%s,%s,%s,%s,%s,%s,%s)"
                                self.args=(pname,pdob,pnum,pd,dname,pf,ppa)
                                self.cursor.execute(self.q,self.args)
                                self.conn.commit()
                                self.conn.close()

                                msg.showinfo("Add New Paitent","Paitent Added Successfully !!")
                                self.destroy_new_patient()
                                
                            else:
                                msg.showinfo("Add New Patient","Please Enter DOB in DD/MM/YYYY !")

                        else:
                            msg.showinfo("Add New Patient","Please Enter DOB in DD/MM/YYYY !")
                                
                    else:
                        msg.showinfo("Add New Patient","Please Enter Perfect Mobile Number !")

                else:
                    msg.showinfo("Add New Patient","Please Enter 10 Digits !")
            
            else:
                msg.showinfo("Add New Patient","Number Already Exists !")
    
            
        
#--------------------------------------------------------------------NEW PAITENT DESTROY METHOD---------------------------------------------------------------------

    def destroy_new_patient(self):
        self.new_p_frame.destroy()
        self.create_main_menu()

#--------------------------------------------------------------------NEW DOCTOR METHOD---------------------------------------------------------------------

    def add_doctor(self):

        self.menu_frame.destroy()
        self.add_d = tk.Menu(self.master)

        self.add_d_frame= tk.Frame(self.master)
        self.add_d_frame.pack()

        #LOGO
        self.image=Image.open("aa.jpg")
        self.photo=ImageTk.PhotoImage(self.image)
        self.l1=tk.Label(self.add_d_frame,image=self.photo)
        self.l1.grid(row=15, columnspan=2, padx=10, pady=10)

        #NEW DOCTOR ID
        self.add_dr_id=tk.Label(self.add_d_frame,text="Doctor ID :")
        self.add_dr_id.grid(row=30,column=0,padx=5,pady=5)
        self.add_dr_id_entry=tk.Entry(self.add_d_frame)
        self.add_dr_id_entry.grid(row=30,column=1,padx=5,pady=5)

        #NEW DOCTOR NAME
        self.add_dr_name=tk.Label(self.add_d_frame,text="Doctor Name :")
        self.add_dr_name.grid(row=35,column=0,padx=5,pady=5)
        self.add_dr_name_entry=tk.Entry(self.add_d_frame)
        self.add_dr_name_entry.grid(row=35,column=1,padx=5,pady=5)

        #NEW DOCTOR DOB
        self.add_dr_dob=tk.Label(self.add_d_frame,text="Doctor DOB :")
        self.add_dr_dob.grid(row=40,column=0,padx=5,pady=5)
        self.add_dr_dob_entry=tk.Entry(self.add_d_frame)
        self.add_dr_dob_entry.grid(row=40,column=1,padx=5,pady=5)

        #NEW DOCTOR NUMBER
        self.add_dr_num=tk.Label(self.add_d_frame,text="Phone Number :")
        self.add_dr_num.grid(row=45,column=0,padx=5,pady=5)
        self.add_dr_num_entry=tk.Entry(self.add_d_frame)
        self.add_dr_num_entry.grid(row=45,column=1,padx=5,pady=5)

        #NEW DOCTOR SPECIALITY
        self.add_dr_special=tk.Label(self.add_d_frame,text="Doctor Speciality :")
        self.add_dr_special.grid(row=50,column=0,padx=5,pady=5)
        self.add_dr_special_entry=tk.Entry(self.add_d_frame)
        self.add_dr_special_entry.grid(row=50,column=1,padx=5,pady=5)

        #NEW DOCTOR SALARY AMOUNT
        self.add_dr_salary=tk.Label(self.add_d_frame,text="SALARY :")
        self.add_dr_salary.grid(row=55,column=0,padx=5,pady=5)
        self.add_dr_salary_entry=tk.Entry(self.add_d_frame)
        self.add_dr_salary_entry.grid(row=55,column=1,padx=5,pady=5)
        
        #NEW DOCTOR EXPERIENCE
        self.add_dr_exp=tk.Label(self.add_d_frame,text="EXPERIENCE IN YEARS")
        self.add_dr_exp.grid(row=60,column=0,padx=5,pady=5)
        self.add_dr_exp_entry=tk.Entry(self.add_d_frame)
        self.add_dr_exp_entry.grid(row=60,column=1,padx=5,pady=5)

        #NEW DOCTOR ADD BUTTON
        self.add_dr_add=tk.Button(self.add_d_frame,text="ADD Doctor",command=self.new_doctor_insert)
        self.add_dr_add.grid(row=65,column=0,padx=5,pady=5)

        #BACK BUTTON
        self.back = tk.Button(self.add_d_frame, text="BACK",command=self.destory_add_dr)
        self.back.grid(row=65, column=1, padx=5, pady=5)

#--------------------------------------------------------------------NEW DCOTOR INSERT METHOD---------------------------------------------------------------------

    def new_doctor_insert(self):
        if self.add_dr_name_entry.get()=="" or self.add_dr_dob_entry.get()=="" or self.add_dr_num_entry.get()=="" or self.add_dr_special_entry.get()=="" or self.add_dr_salary_entry.get()=="" or self.add_dr_exp_entry.get()=="" :
            msg.showinfo("Add New Doctor","All Feilds Are Mandataory !")
        else:
            dname=self.add_dr_name_entry.get()
            ddob=self.add_dr_dob_entry.get()
            dnum=self.add_dr_num_entry.get()
            dspe=self.add_dr_special_entry.get()
            dsalary=self.add_dr_salary_entry.get()
            dexp=self.add_dr_exp_entry.get()
            
            flag=0
            #FETCHING DOCTOR NUMBERS
            doctor_number=self.fetch_num_dr()
            
            if dnum in doctor_number:
                flag=1
            else:
                flag=0
            
            
            if flag==1:
                
                if len(dnum)==10:
                    
                    if dnum[0]=="9" or dnum[0]=="8" or dnum[0]=="7" or dnum[0]=="6": 
                        
                        if ddob[2]=="/" and ddob[5]=="/":
                            
                            if ddob[0:2].isdigit() and ddob[3:5].isdigit() and ddob[6:].isdigit():
                                
                                self.conn=self.create_conn()
                                self.cursor=self.conn.cursor()
                                self.q="insert into doctor (dname,ddob,dnum,dspe,dsalary,dexp) values (%s,%s,%s,%s,%s,%s)"
                                self.args=(dname,ddob,dnum,dspe,dsalary,dexp)
                                self.cursor.execute(self.q,self.args)
                                self.conn.commit()
                                self.conn.close()

                                msg.showinfo("Add New Doctor","Doctore Added Successfully !!")
                                self.destory_add_dr()
                                
                            else:
                                msg.showinfo("Add New Doctor","Please Enter DOB in DD/MM/YYYY !")

                        else:
                            msg.showinfo("Add New Doctor","Please Enter DOB in DD/MM/YYYY !")
                                
                    else:
                        msg.showinfo("Add New Doctor","Please Enter Perfect Mobile Number !")

                else:
                    msg.showinfo("Add New Doctor","Please Enter 10 Digits !")
                    
            else:
                msg.showinfo("Add New Doctor","Number Already Exists !")

#--------------------------------------------------------------------NEW DOCTOR DESTORY METHOD---------------------------------------------------------------------

    def destory_add_dr(self):
        self.add_d_frame.destroy()
        self.create_main_menu()

#--------------------------------------------------------------------OLD PAITENT CHECK METHOD---------------------------------------------------------------------
        
    def check_patient(self):
        
        self.menu_frame.destroy()
        self.old_p = tk.Menu(self.master)

        self.check_p_frame= tk.Frame(self.master)
        self.check_p_frame.pack()

        #LOGO
        self.image=Image.open("aa.jpg")
        self.photo=ImageTk.PhotoImage(self.image)
        self.l1=tk.Label(self.check_p_frame,image=self.photo)
        self.l1.grid(row=15, columnspan=2, padx=10, pady=10)

        #OLD PAITENT ID
        self.check_p_id=tk.Label(self.check_p_frame,text="Paitent ID :")
        self.check_p_id.grid(row=30,column=0,padx=5,pady=5)
        self.check_p_id_entry=tk.Entry(self.check_p_frame)
        self.check_p_id_entry.grid(row=30,column=1,padx=5,pady=5)

        #OLD PAITENT NAME
        self.check_p_name=tk.Label(self.check_p_frame,text="Paitent Name :")
        self.check_p_name.grid(row=35,column=0,padx=5,pady=5)
        self.check_p_name_entry=tk.Entry(self.check_p_frame)
        self.check_p_name_entry.grid(row=35,column=1,padx=5,pady=5)

        #OLD PAITENT DOB
        self.check_p_dob=tk.Label(self.check_p_frame,text="Paitent DOB :")
        self.check_p_dob.grid(row=40,column=0,padx=5,pady=5)
        self.check_p_dob_entry=tk.Entry(self.check_p_frame)
        self.check_p_dob_entry.grid(row=40,column=1,padx=5,pady=5)

        #OLD PAITENT NUMBER
        self.check_p_num=tk.Label(self.check_p_frame,text="Phone Number :")
        self.check_p_num.grid(row=45,column=0,padx=5,pady=5)
        self.check_p_num_entry=tk.Entry(self.check_p_frame)
        self.check_p_num_entry.grid(row=45,column=1,padx=5,pady=5)

        #OLD PAITENT DISEASE
        self.check_p_d=tk.Label(self.check_p_frame,text="Paitent Disease:")
        self.check_p_d.grid(row=50,column=0,padx=5,pady=5)
        self.check_p_d_entry=tk.Entry(self.check_p_frame)
        self.check_p_d_entry.grid(row=50,column=1,padx=5,pady=5)

        #OLD PAITENT PENDING AMOUNT
        self.check_p_dob=tk.Label(self.check_p_frame,text="Pending Amount :")
        self.check_p_dob.grid(row=55,column=0,padx=5,pady=5)
        self.check_p_dob_entry=tk.Entry(self.check_p_frame)
        self.check_p_dob_entry.grid(row=55,column=1,padx=5,pady=5)

        #OLD PAITENT SEARCH BUTTON
        self.check_p_search=tk.Button(self.check_p_frame,text="Search Paitent",command=self.check_old_paitent)
        self.check_p_search.grid(row=60,column=0,padx=5,pady=5)

        #OLD PAITENT DELETE BUTTON
        self.check_p_delete=tk.Button(self.check_p_frame,text="Delete Details",command=self.delete_old_paitent)
        self.check_p_delete.grid(row=60,column=1,padx=5,pady=5)

        #BACK BUTTON
        self.back = tk.Button(self.check_p_frame, text="BACK",command=self.destory_check_patient)
        self.back.grid(row=65, columnspan=2, padx=5, pady=5)

#--------------------------------------------------------------------OLD PAITENT SEARCH METHOD---------------------------------------------------------------------

    def check_old_paitent(self):
        if self.check_p_num_entry.get()=="":
            msg.showinfo("Search Status","Mobile Number  Is Mandatory")
        else:
            self.conn=self.create_conn()
            self.cursor=self.conn.cursor()
            self.q="select * from paitent where pnum=%s"
            self.args=(self.check_p_num_entry.get(),)
            self.cursor.execute(self.q,self.args)
            self.row=self.cursor.fetchall()
            if self.row:
                for i in self.row:
                    self.check_p_id_entry.insert(0,i[0])
                    self.check_p_name_entry.insert(0,i[1])
                    self.check_p_dob_entry.insert(0,i[2])
                    #self.old_paitent_num_entry.insert(0,i[3])
                    self.check_p_d_entry.insert(0,i[4])
                    #self.old_paitent_dr_entry.insert(0,i[5])
                    self.check_p_dob_entry.insert(0,i[7])
            else:
                msg.showinfo("Search Status","Mobile Number is not found")
            self.conn.close()

#--------------------------------------------------------------------OLD PAITENT DELETE METHOD---------------------------------------------------------------------

    def delete_old_paitent(self):
        if self.check_p_num_entry.get()=="":
            msg.showinfo("Delete Status","Mobile Number Is Mandatory")
        else:
            self.conn=self.create_conn()
            self.cursor=self.conn.cursor()
            self.q="delete from paitent where pnum=%s"
            self.args=(self.check_p_num_entry.get(),)
            self.cursor.execute(self.q,self.args)
            self.conn.commit()
            self.conn.close()
            msg.showinfo("Delete Status","Data Deleted Successfully")
            

#--------------------------------------------------------------------CHECK PAITENT DESTROY METHOD---------------------------------------------------------------------            

    def destory_check_patient(self):
        self.check_p_frame.destroy()
        self.create_main_menu()

#--------------------------------------------------------------------OLD DOCTOR METHOD---------------------------------------------------------------------

    def check_doctor(self):

        self.menu_frame.destroy()
        self.check_d = tk.Menu(self.master)

        self.check_d_frame= tk.Frame(self.master)
        self.check_d_frame.pack()

        #LOGO
        self.image=Image.open("aa.jpg")
        self.photo=ImageTk.PhotoImage(self.image)
        self.l1=tk.Label(self.check_d_frame,image=self.photo)
        self.l1.grid(row=15, columnspan=3, padx=10, pady=10)

        #OLD DOCTOR ID
        self.check_d_id=tk.Label(self.check_d_frame,text="Doctor ID :")
        self.check_d_id.grid(row=30,column=0,padx=5,pady=5)
        self.check_d_id_entry=tk.Entry(self.check_d_frame)
        self.check_d_id_entry.grid(row=30,column=1,padx=5,pady=5)

        doctor_names=self.fetch_dr()
        # DOCTOR DROPDOWN MENU
        self.doctor_label = tk.Label(self.check_d_frame, text="Select Doctor:")
        self.doctor_label.grid(row=35, column=0, padx=5, pady=5)
        self.doctor_var = tk.StringVar(self.check_d_frame)
        self.doctor_var.set(doctor_names[0])
        self.doctor_dropdown = tk.OptionMenu(self.check_d_frame, self.doctor_var, *doctor_names)
        self.doctor_dropdown.grid(row=35 , column=1, padx=5, pady=5)

        #OLD DOCTOR DOB
        self.check_d_dob=tk.Label(self.check_d_frame,text="Doctor DOB :")
        self.check_d_dob.grid(row=40,column=0,padx=5,pady=5)
        self.check_d_dob_entry=tk.Entry(self.check_d_frame)
        self.check_d_dob_entry.grid(row=40,column=1,padx=5,pady=5)

        #OLD DOCTOR NUMBER
        self.check_d_num=tk.Label(self.check_d_frame,text="Phone Number :")
        self.check_d_num.grid(row=45,column=0,padx=5,pady=5)
        self.check_d_num_entry=tk.Entry(self.check_d_frame)
        self.check_d_num_entry.grid(row=45,column=1,padx=5,pady=5)

        #OLD DOCTOR SPECIALITY
        self.check_d_special=tk.Label(self.check_d_frame,text="Doctor Speciality :")
        self.check_d_special.grid(row=50,column=0,padx=5,pady=5)
        self.check_d_special_entry=tk.Entry(self.check_d_frame)
        self.check_d_special_entry.grid(row=50,column=1,padx=5,pady=5)

        #OLD DOCTOR SALARY AMOUNT
        self.check_d_salary=tk.Label(self.check_d_frame,text="SALARY :")
        self.check_d_salary.grid(row=55,column=0,padx=5,pady=5)
        self.check_d_salary_entry=tk.Entry(self.check_d_frame)
        self.check_d_salary_entry.grid(row=55,column=1,padx=5,pady=5)
        
        #OLD DOCTOR EXPERIENCE
        self.check_d_exp=tk.Label(self.check_d_frame,text="EXPERIENCE IN YEARS")
        self.check_d_exp.grid(row=60,column=0,padx=5,pady=5)
        self.check_d_exp_entry=tk.Entry(self.check_d_frame)
        self.check_d_exp_entry.grid(row=60,column=1,padx=5,pady=5)

        #OLD DOCTOR SEARCH BUTTON
        self.check_d_ser=tk.Button(self.check_d_frame,text="SEARCH Doctor",command=self.search_doctor)
        self.check_d_ser.grid(row=65,column=0,padx=5,pady=5)

        #OLD DOCTOR DELETE BUTTON
        self.check_d_del=tk.Button(self.check_d_frame,text="DELETE Doctor",command=self.delete_doctor)
        self.check_d_del.grid(row=65,column=1,padx=5,pady=5)

        #OLD DOCTOR UPDATE BUTTON
        self.check_d_upd=tk.Button(self.check_d_frame,text="UPDATE Doctor",command=self.update_doctor)
        self.check_d_upd.grid(row=65,column=2,padx=5,pady=5)

        #BACK BUTTON
        self.back = tk.Button(self.check_d_frame, text="BACK",command=self.destory_check_doctor)
        self.back.grid(row=70, columnspan=3, padx=5, pady=5)

#--------------------------------------------------------------------OLD DOCTOR SEARCH METHOD---------------------------------------------------------------------
    def search_doctor(self):
        dname = self.doctor_var.get()
        if dname=="":
            msg.showinfo("Search Status","Doctor Name Is Mandatory ")
        else:
            s =dname
            start = s.find("'") + 1
            end = s.rfind("'")
            extracted = s[start:end]
            print(extracted)
            self.conn=self.create_conn()
            self.cursor=self.conn.cursor()
            self.q="select * from doctor where dname=%s"
            self.args=(extracted,)
            self.cursor.execute(self.q,self.args)
            self.row=self.cursor.fetchall()
            if self.row:
                for i in self.row:
                    self.check_d_id_entry.insert(0,i[0])
                    #self.check_d_name_entry.insert(1,i[1])
                    self.check_d_dob_entry.insert(2,i[2])
                    self.check_d_num_entry.insert(3,i[3])
                    self.check_d_special_entry.insert(4,i[4])
                    self.check_d_salary_entry.insert(5,i[5])
                    self.check_d_exp_entry.insert(6,i[6])
            else:
                msg.showinfo("Search Status ","Mobile Number Is Not Found")
            self.conn.close()

#--------------------------------------------------------------------OLD DOCTOR DELETE METHOD---------------------------------------------------------------------
    def delete_doctor(self):
        dname = self.doctor_var.get()
        if dname=="":
            msg.showinfo("Search Status","Doctor Name Is Mandatory ")
        else:
            s =dname
            start = s.find("'") + 1
            end = s.rfind("'")
            extracted = s[start:end]
            #rint(extracted)
            self.conn=self.create_conn()
            self.cursor=self.conn.cursor()
            self.q="delete from doctor where dname=%s"
            self.args=(extracted,)
            self.cursor.execute(self.q,self.args)
            self.conn.commit()
            self.conn.close()
            msg.showinfo("Delete Status","Data Deleted Successfully")
            self.destory_check_doctor()
            
#------------------------------------------------------------------OLD DOCTOR UPDATE METHOD -----------------------------------------------------------------
    def update_doctor(self):
        if self.check_d_id_entry.get()=="" or self.check_d_name_entry.get()=="" or self.check_d_dob_entry.get()=="" or self.check_d_num_entry.get()=="" or self.check_d_special_entry.get()=="" or self.check_d_salary_entry.get()=="" or self.check_d_exp_entry.get()=="":
            msg.showinfo("Update Status","All Fields Are Mandatory")
        else:
            self.conn=self.create_conn()
            self.cursor=self.conn.cursor()
            self.q="update doctor set did=%s,dname=%s,ddob=%s,dnum=%s,dspe=%s,dsalary=%s,dexp=%s where dnum=%s"
            self.args=(self.check_d_id_entry.get(),self.check_d_name_entry.get(),self.check_d_dob_entry.get(),self.check_d_num_entry.get(),self.check_d_special_entry.get(),self.check_d_salary_entry.get(),self.check_d_exp_entry.get(),self.check_d_num_entry.get())
            self.cursor.execute(self.q,self.args)
            self.conn.commit()
            self.conn.close()
            msg.showinfo("Update Status","Data Updated Succesfully !")
            self.destory_check_doctor()
            
        

#--------------------------------------------------------------------OLD DOCTOR DESTROY METHOD---------------------------------------------------------------------        

    def destory_check_doctor(self):
        self.check_d_frame.destroy()
        self.create_main_menu()
        
#--------------------------------------------------------------Fetching All Doctors Name ------------------------------------------------------------
    
    def fetch_dr(self):
        self.conn=self.create_conn()
        self.cursor=self.conn.cursor()
        self.q="select dname from doctor"
        #self.args=(self.check_d_num_entry.get(),)
        self.cursor.execute(self.q)
        self.row=self.cursor.fetchall()
        return list(self.row)
    
#------------------------------------------------------Fetching All Numbers Of Paitents-----------------------------------------------

    def fetch_num_paitent(self):
        self.conn=self.create_conn()
        self.cursor=self.conn.cursor()
        self.q="select pnum from paitent"
        self.cursor.execute(self.q)
        self.num_paitent=self.cursor.fetchall()
        return list(self.num_paitent)

#------------------------------------------------------Fetching All Numbers Of Paitents-----------------------------------------------

    def fetch_num_dr(self):
        self.conn=self.create_conn()
        self.cursor=self.conn.cursor()
        self.q="select dnum from doctor"
        self.cursor.execute(self.q)
        self.num_dr=self.cursor.fetchall()
        return list(self.num_dr)

def main():
    root = tk.Tk()
    app = HospitalManagementSystem(root)
    root.mainloop()
    app.create_conn()

if __name__ == "__main__":
    main()

from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
import mysql.connector
import tkinter.messagebox as msg
import tkinter.font as tkFont
import webbrowser



class Automobile():
    def __init__(self,master):
        self.master=master
        self.master.title("CAR SALES")
        self.master['background']='#6AD4DD'
        self.master.geometry("1000x1000")
        self.master.resizable(width=False,height=False)
        self.frame_login()


    def create_conn(self):
        return mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="python_automobile"
            )

    #Signup to login
    def signupToLogin(self):
        self.signup_frame.destroy()
        self.frame_login()

    #Login to Signup
    def loginToSignup(self):
        self.login_frame.destroy()
        self.frame_signup()
   

    # Login Frame
    def frame_login(self):
        self.master.geometry("525x505")


        self.login_frame=tk.Frame(self.master, width=1000, height=1000)
        self.login_frame['background']='#6AD4DD'
        self.login_frame.pack()

        # Login Items
        self.fontObj = tkFont.Font(size=30) 
        self.login_label=tk.Label(self.login_frame,bg="#6AD4DD",text="LOGIN",font=self.fontObj)
        self.login_label.grid(row=1,column=1,columnspan=2,pady=50)
        self.username_label = tk.Label(self.login_frame,bg="#6AD4DD", text="UserName",font=(20))
        self.username_label.grid(row=3,column=1,padx=30,pady=40)
        self.username_entry = tk.Entry(self.login_frame,width=40)
        self.username_entry.grid(row=3,column=2,padx=50)
        self.password_label = tk.Label(self.login_frame,bg="#6AD4DD", text="Password",font=(20))
        self.password_label.grid(row=5,column=1)
        self.password_entry = tk.Entry(self.login_frame, show="*",width=40)
        self.password_entry.grid(row=5,column=2,pady=50)

        # Buttons
        self.signup_button = tk.Button(self.login_frame,font=(30), text="Sign Up",command=self.loginToSignup,width=10)
        self.signup_button.grid(row=6,column=1,pady=50,padx=40)
        self.signup_button.configure(overrelief="sunken")
        self.login_button = tk.Button(self.login_frame,font=(30), text="Login",command=self.login,width=10)
        self.login_button.grid(row=6,column=2,pady=50)
        self.login_button.configure(overrelief="sunken")


    # Signup Frame
    def frame_signup(self):
        self.master.geometry("1000x1000")

        self.signup_frame=tk.Frame(self.master,width=1200,height=1200,relief="groove",borderwidth=5)
        self.signup_frame['background']='#6AD4DD'
        self.signup_frame.pack()

        # Signup Items
        self.signup_label=tk.Label(self.signup_frame,bg='#6AD4DD',text="SIGN UP",font=self.fontObj)
        self.signup_label.place(x=400,y=50)
        self.fname_label=tk.Label(self.signup_frame,text="First Name",bg="#6AD4DD",font=(20))
        self.fname_label.place(x=320,y=150)
        self.fname_entry = tk.Entry(self.signup_frame,width=40)
        self.fname_entry.place(x=530,y=155)
        self.lname_label=tk.Label(self.signup_frame,text="Last Name",bg="#6AD4DD",font=(20))
        self.lname_label.place(x=320,y=200)
        self.lname_entry = tk.Entry(self.signup_frame,width=40)
        self.lname_entry.place(x=530,y=205)
        self.mobile_label=tk.Label(self.signup_frame,text="Mobile",bg="#6AD4DD",font=(20))
        self.mobile_label.place(x=320,y=250)
        self.mobile_entry = tk.Entry(self.signup_frame,width=40)
        self.mobile_entry.place(x=530,y=255)
        self.email_label=tk.Label(self.signup_frame,text="Email",bg="#6AD4DD",font=(20))
        self.email_label.place(x=320,y=300)
        self.email_entry = tk.Entry(self.signup_frame,width=40)
        self.email_entry.place(x=530,y=305)
        self.password_label=tk.Label(self.signup_frame,text="Password",bg="#6AD4DD",font=(20))
        self.password_label.place(x=320,y=350)
        self.password_entry = tk.Entry(self.signup_frame,width=40)
        self.password_entry.place(x=530,y=355)

        # Buttons
        self.signup_button = tk.Button(self.signup_frame,font=(30), text="Sign Up",command=self.signup,width=10)
        self.signup_button.place(x=600,y=500)
        self.login_button = tk.Button(self.signup_frame,font=(30), text="Login",command=self.signupToLogin,width=10)
        self.login_button.place(x=400,y=500)


    def frame_home(self):
        self.master.geometry("775x1000")
        # Home Frame
        self.home_frame=tk.Frame(self.master,width=1000,height=800,relief="groove",borderwidth=5)
        self.home_frame['background']='#6AD4DD'
        self.home_frame.pack()

        #Logout Button
        self.logout_label=tk.Button(self.home_frame,text="LOG OUT",command=self.homeToLogin)
        self.logout_label.grid(row=0,column=2,sticky=E)
        

        # Home Items
        self.image_paths = [
            "images\Sedan.jpg",
            "images\Suv.jpg",
            "images\Convertible.jpg",
            "images\Luxury.jpg",
            "images\Antique.jpg",
            "images\Muscle.jpg"]

        self.image_names = ["SEDAN","SUV","CONVERTABLE","LUXURY","ANTIQUE","MUSCLE"]
        self.image_frames = [self.homeToSedan,self.homeToSuv,self.homeToConvertible,self.homeToLuxury,self.homeToAntique,self.homeToMuscle]
        self.row_count = 1
        self.column_count = 1
        self.i = 0

        for image_path in self.image_paths:
            self.image = Image.open(image_path)
            self.photo = ImageTk.PhotoImage(self.image.resize((275,150)))
            self.label = tk.Label(self.home_frame, image=self.photo)
            self.label.image = self.photo
            self.label.grid(row=self.row_count, column=self.column_count, padx=10, pady=9)
            self.car_label=tk.Button(self.home_frame,text=self.image_names[self.i],command=self.image_frames[self.i])
            self.car_label.grid(row=self.row_count+1, column=self.column_count, padx=10, pady=9)

            self.i += 1
            self.column_count += 1
            if self.column_count == 3:
                self.column_count = 1
                self.row_count += 2

    # Home to Sedan
    def homeToSedan(self):
        self.home_frame.destroy()
        self.frame_sedan()

    # Sedan to Login
    def sedanToLogin(self):
        self.sedan_frame.destroy()
        self.frame_login()

    # Sedan to Home
    def sedanToHome(self):
        self.sedan_frame.destroy()
        self.frame_home()

    # Sedan Frame
    def frame_sedan(self):
        self.master.geometry("660x1000")

        self.sedan_frame=tk.Frame(self.master,width=1000,height=1000,relief="groove",borderwidth=5)
        self.sedan_frame['background']='#6AD4DD'
        self.sedan_frame.pack()

        #Logout Button
        self.logout_label=tk.Button(self.sedan_frame,text="LOG OUT",command=self.sedanToLogin)
        self.logout_label.grid(row=0,column=2,sticky=E)

        #Back Button
        self.back_label=tk.Button(self.sedan_frame,text="BACK",command=self.sedanToHome)
        self.back_label.grid(row=0,column=1,sticky=W)

        self.sedan_paths = [
            "Sedan\camry.jpg",
            "Sedan\ciaz.jpg",
            "Sedan\city.jpg",
            "Sedan\Verna.jpg",
            "Sedan\Vertus.jpg"]

        self.sedan_names = ["CAMRY","CIAZ","CITY","VERNA","VERTUS"]
        self.sedan_frames = [self.sedanToCamry,self.homeToSuv,self.homeToLuxury,self.homeToAntique,self.homeToMuscle]
        self.row_count = 1
        self.column_count = 1
        self.i = 0

        for sedan_path in self.sedan_paths:
            self.image = Image.open(sedan_path)
            self.photo = ImageTk.PhotoImage(self.image.resize((275,150)))
            self.label = tk.Label(self.sedan_frame, image=self.photo)
            self.label.grid(row=self.row_count, column=self.column_count, padx=10, pady=9)
            self.label.image = self.photo
            self.car_label=tk.Button(self.sedan_frame,text=self.sedan_names[self.i],command=self.sedan_frames[self.i])
            self.car_label.grid(row=self.row_count+1, column=self.column_count, padx=10, pady=9)

            self.i += 1
            self.column_count += 1
            if self.column_count == 3:
                self.column_count = 1
                self.row_count += 2

    # Sedan to Camry
    def sedanToCamry(self):
        self.sedan_frame.destroy()
        self.frame_camry()

    # Camry to Login
    def camryToLogin(self):
        self.camry_frame.destroy()
        self.frame_login()

    # Camry to Sedan
    def camryToSedan(self):
        self.camry_frame.destroy()
        self.frame_sedan()

    # BookTestDrive To Login
    def bookTestDriveToLogin(self):
        self.BookTestDrive_frame.destroy()
        self.frame_login()

    #BookTestDrive To Camry
    def BookTestDriveToCamryFrame(self):
        self.BookTestDrive_frame.destroy()
        self.frame_camry()

    # Camry To BookTestDrive
    def camryToBookTestDrive(self):
        self.camry_frame.destroy()
        self.frame_BookTestDrive()

    # Camry Frame
    def frame_camry(self):
        self.master.geometry("970x715")

        self.camry_frame=tk.Frame(self.master,width=1000,height=1000,relief="groove",borderwidth=5)
        self.camry_frame['background']='#6AD4DD'
        self.camry_frame.pack()

        #Logout Button
        self.logout_label=tk.Button(self.camry_frame,text="LOG OUT",command=self.camryToLogin)
        self.logout_label.grid(row=0,column=2,sticky=E)

        #Back Button
        self.back_label=tk.Button(self.camry_frame,text="BACK",command=self.camryToSedan)
        self.back_label.grid(row=0,column=1,sticky=W)

        self.image = Image.open("Sedan-cars\camry.webp")
        self.photo = ImageTk.PhotoImage(self.image.resize((700,500)))
        self.label = tk.Label(self.camry_frame, image=self.photo)
        self.label.grid(row=1, column=1,columnspan=2, padx=10, pady=9)
        self.label.image = self.photo
        self.brochure_label=tk.Button(self.camry_frame,text="BROCHURE",command=self.camryBrochure)
        self.brochure_label.grid(row=2, column=1, padx=10, pady=9)
        self.test_drive_label=tk.Button(self.camry_frame,text="BOOK TEST DRIVE",command=self.camryToBookTestDrive)
        self.test_drive_label.grid(row=2, column=2, padx=10, pady=9)
        
    #Camry Brochure
    def camryBrochure(self):
        webbrowser.open("Brochure\Toyota-camry-2.5-hybrid-brochure.pdf")    

    #Book A Test Drive
    def frame_BookTestDrive(self):
        self.master.geometry("700x520")
        self.fontObj = tkFont.Font(size=15)
        self.fontObj1 = tkFont.Font(size=30)

        self.BookTestDrive_frame=tk.Frame(self.master,width=1000,height=1000,relief="groove",borderwidth=5)
        self.BookTestDrive_frame['background']='#6AD4DD'
        self.BookTestDrive_frame.pack()

        #Logout Button
        self.logout_label=tk.Button(self.BookTestDrive_frame,text="LOG OUT",command=self.bookTestDriveToLogin)
        self.logout_label.grid(row=0,column=2,sticky=E)

        #Back Button
        self.back_label=tk.Button(self.BookTestDrive_frame,text="BACK",command=self.BookTestDriveToCamryFrame)
        self.back_label.grid(row=0,column=1,sticky=W)

        # Body 
        self.heading_label=tk.Label(self.BookTestDrive_frame,text="TEST DRIVE DETAILS",bg="#6AD4DD",font=self.fontObj1)
        self.heading_label.grid(row=1,column=1,columnspan=2,padx=5,pady=50)
        self.heading_label=tk.Label(self.BookTestDrive_frame,text="Get a Test Drive Scheduled of your favourite car at your nearest Dealership.",bg="#6AD4DD",font=self.fontObj)
        self.heading_label.grid(row=2,column=1,columnspan=2,padx=6,pady=35)
        self.submit_fname_label=tk.Label(self.BookTestDrive_frame,text="First Name ",bg="#6AD4DD",font=(10))
        self.submit_fname_label.grid(row=3,column=1,pady=10)
        self.submit_fname_entry=tk.Entry(self.BookTestDrive_frame,width=30)
        self.submit_fname_entry.grid(row=3,column=2,pady=10)
        self.submit_lname_label=tk.Label(self.BookTestDrive_frame,text="Last Name ",bg="#6AD4DD",font=(10))
        self.submit_lname_label.grid(row=4,column=1,pady=10)
        self.submit_lname_entry=tk.Entry(self.BookTestDrive_frame,width=30)
        self.submit_lname_entry.grid(row=4,column=2,pady=10)
        self.submit_mobile_label=tk.Label(self.BookTestDrive_frame,text="Mobile ",bg="#6AD4DD",font=(10))
        self.submit_mobile_label.grid(row=5,column=1,pady=10)
        self.submit_mobile_entry=tk.Entry(self.BookTestDrive_frame,width=30)
        self.submit_mobile_entry.grid(row=5,column=2,pady=10)
        self.submit_email_label=tk.Label(self.BookTestDrive_frame,text="Email ",bg="#6AD4DD",font=(10))
        self.submit_email_label.grid(row=6,column=1,pady=10)
        self.submit_email_entry=tk.Entry(self.BookTestDrive_frame,width=30)
        self.submit_email_entry.grid(row=6,column=2,pady=10)
        self.submit_button=tk.Button(self.BookTestDrive_frame,text="SUBMIT",command=self.submit)
        self.submit_button.grid(row=7,column=1,columnspan=2,pady=10)
        

    # Submit
    def submit(self):
        fname=self.submit_fname_entry.get()
        lname=self.submit_lname_entry.get()
        mobile=self.submit_mobile_entry.get()
        email=self.submit_email_entry.get()
        

        if fname=="" or lname=="" or mobile=="" or email=="" :
            msg.showwarning("Signup","All Fields Are Mandatory")
        else:
            if mobile.isalpha() == False:
                if len(mobile) == 10 :
                    if email.endswith("@gmail.com"):
                        msg.showinfo("BOOKING DETAILS","Book Successfully")
                        self.submitToHome()
                    else:
                        msg.showwarning("Signup", "Enter Proper Email")
                else:
                    msg.showwarning("Signup", "Mobile Number Must Be 10 digits")
            else:
                msg.showwarning("Signup", "Enter Numbers Only.")

    #Submit To Home
    def submitToHome(self):
        self.BookTestDrive_frame.destroy()
        self.frame_home()


    # Home to Suv
    def homeToSuv(self):
        self.home_frame.destroy()
        self.frame_suv()

    # Suv to Login
    def suvToLogin(self):
        self.suv_frame.destroy()
        self.frame_login()

    # Suv to Home
    def suvToHome(self):
        self.suv_frame.destroy()
        self.frame_home()

    # Suv Frame
    def frame_suv(self):
        self.master.geometry("680x1000")

        self.suv_frame=tk.Frame(self.master,width=1000,height=1000,relief="groove",borderwidth=5)
        self.suv_frame['background']='#6AD4DD'
        self.suv_frame.pack()

        #Logout Button
        self.logout_label=tk.Button(self.suv_frame,text="LOG OUT",command=self.suvToLogin)
        self.logout_label.grid(row=0,column=2,sticky=E)


        #Back Button
        self.back_label=tk.Button(self.suv_frame,text="BACK",command=self.suvToHome)
        self.back_label.grid(row=0,column=1,sticky=W)

        self.suv_paths = [
            "suv\Thar.jpg",
            "suv\scorpio.jpg",
            "suv\Fortuner.jpg",
            "suv\defender.jpg",
            "suv\Range rover.jpg",
            "suv\land cruiser.jpg"]

        self.suv_names = ["THAR","SCORPIO","FORTUNER","DEFENDER","RANGE ROVER","LAND CRUISER"]
        self.suv_frames = [self.homeToSedan,self.homeToSuv,self.homeToLuxury,self.homeToAntique,self.homeToMuscle,self.homeToMuscle]
        self.row_count = 1
        self.column_count = 1
        self.i = 0

        for suv_path in self.suv_paths:
            self.image = Image.open(suv_path)
            self.photo = ImageTk.PhotoImage(self.image.resize((275,150)))
            self.label = tk.Label(self.suv_frame, image=self.photo)
            self.label.image = self.photo
            self.label.grid(row=self.row_count, column=self.column_count, padx=10, pady=9)
            self.car_label=tk.Button(self.suv_frame,text=self.suv_names[self.i],command=self.suv_frames[self.i])
            self.car_label.grid(row=self.row_count+1, column=self.column_count, padx=10, pady=9)

            self.i += 1
            self.column_count += 1
            if self.column_count == 3:
                self.column_count = 1
                self.row_count += 2


    # Home to Convertible
    def homeToConvertible(self):
        self.home_frame.destroy()
        self.frame_convertible()

    # Convertible to Login
    def convertibleToLogin(self):
        self.convertible_frame.destroy()
        self.frame_login()

    # Convertible to Home
    def convertibleToHome(self):
        self.convertible_frame.destroy()
        self.frame_home()

    # Convertible Frame
    def frame_convertible(self):
        self.master.geometry("680x1000")

        self.convertible_frame=tk.Frame(self.master,width=1000,height=1000,relief="groove",borderwidth=5)
        self.convertible_frame['background']='#6AD4DD'
        self.convertible_frame.pack()

        #Logout Button
        self.logout_label=tk.Button(self.convertible_frame,text="LOG OUT",command=self.convertibleToLogin)
        self.logout_label.grid(row=0,column=2,sticky=E)

        #Back Button
        self.back_label=tk.Button(self.convertible_frame,text="BACK",command=self.convertibleToHome)
        self.back_label.grid(row=0,column=1,sticky=W)

        self.convertible_paths = [
            "convertible\porsche911.jpg",
            "convertible\Maserati GranCabrio.jpg",
            "convertible\Bmwz4.jpg",
            "convertible\Amg-e53.jpg",
            "convertible\Amg-sl.jpg"]

        self.convertible_names = ["PORSCHE 911","MASERATI GRAN CABRIO","BMW Z4","AMG-E53","AMG-SL"]
        self.convertible_frames = [self.homeToSedan,self.homeToSuv,self.homeToLuxury,self.homeToAntique,self.homeToMuscle]
        self.row_count = 1
        self.column_count = 1
        self.i = 0

        for convertible_path in self.convertible_paths:
            self.image = Image.open(convertible_path)
            self.photo = ImageTk.PhotoImage(self.image.resize((275,150)))
            self.label = tk.Label(self.convertible_frame, image=self.photo)
            self.label.image = self.photo
            self.label.grid(row=self.row_count, column=self.column_count, padx=10, pady=9)
            self.car_label=tk.Button(self.convertible_frame,text=self.convertible_names[self.i],command=self.convertible_frames[self.i])
            self.car_label.grid(row=self.row_count+1, column=self.column_count, padx=10, pady=9)

            self.i += 1
            self.column_count += 1
            if self.column_count == 3:
                self.column_count = 1
                self.row_count += 2


    # Home to Luxury
    def homeToLuxury(self):
        self.home_frame.destroy()
        self.frame_luxury()

    # Luxury to Login
    def luxuryToLogin(self):
        self.luxury_frame.destroy()
        self.frame_login()

    # Luxury to Home
    def luxuryToHome(self):
        self.luxury_frame.destroy()
        self.frame_home()

    # Luxury Frame
    def frame_luxury(self):
        self.master.geometry("680x1000")

        self.luxury_frame=tk.Frame(self.master,width=1000,height=1000,relief="groove",borderwidth=5)
        self.luxury_frame['background']='#6AD4DD'
        self.luxury_frame.pack()

        #Logout Button
        self.logout_label=tk.Button(self.luxury_frame,text="LOG OUT",command=self.luxuryToLogin)
        self.logout_label.grid(row=0,column=2,sticky=E)

        #Back Button
        self.back_label=tk.Button(self.luxury_frame,text="BACK",command=self.luxuryToHome)
        self.back_label.grid(row=0,column=1,sticky=W)

        self.luxury_paths = [
            "Luxury\Rolls-Royce Ghost.jpg",
            "Luxury\Mercedes-Benz Maybach S-Class.jpg",
            "Luxury\Bentley continaltal.jpg",
            "Luxury\BMW XM.jpg",
            "Luxury\Aston Martin DBX.jpg"]

        self.luxury_names = ["ROLLS-ROYCE","MERCEDES-BENZ MAYBACH S-CLASS","BENTLEY CONTINALTAL","BMW XM","ASTON MARTIN"]
        self.luxury_frames = [self.homeToSedan,self.homeToSuv,self.homeToLuxury,self.homeToAntique,self.homeToMuscle]
        self.row_count = 1
        self.column_count = 1
        self.i = 0

        for luxury_path in self.luxury_paths:
            self.image = Image.open(luxury_path)
            self.photo = ImageTk.PhotoImage(self.image.resize((275,150)))
            self.label = tk.Label(self.luxury_frame, image=self.photo)
            self.label.image = self.photo
            self.label.grid(row=self.row_count, column=self.column_count, padx=10, pady=9)
            self.car_label=tk.Button(self.luxury_frame,text=self.luxury_names[self.i],command=self.luxury_frames[self.i])
            self.car_label.grid(row=self.row_count+1, column=self.column_count, padx=10, pady=9)

            self.i += 1
            self.column_count += 1
            if self.column_count == 3:
                self.column_count = 1
                self.row_count += 2

    # Home to Antique
    def homeToAntique(self):
        self.home_frame.destroy()
        self.frame_antique()

    # Antique to Login
    def antiqueToLogin(self):
        self.antique_frame.destroy()
        self.frame_login()

    # Antique to Home
    def antiqueToHome(self):
        self.antique_frame.destroy()
        self.frame_home()

    # Antique Frame
    def frame_antique(self):
        self.master.geometry("820x1000")

        self.antique_frame=tk.Frame(self.master,width=1000,height=1000,relief="groove",borderwidth=5)
        self.antique_frame['background']='#6AD4DD'
        self.antique_frame.pack()

        #Logout Button
        self.logout_label=tk.Button(self.antique_frame,text="LOG OUT",command=self.antiqueToLogin)
        self.logout_label.grid(row=0,column=2,sticky=E)

        #Back Button
        self.back_label=tk.Button(self.antique_frame,text="BACK",command=self.antiqueToHome)
        self.back_label.grid(row=0,column=1,sticky=W)

        self.antique_paths = [
            "Antique\Shelby Cobra.jpg",
            "Antique\Rolls-Royce Dawn Drophead.jpg",
            "Antique\Mercedes SL 300 Gullwing.jpg",
            "Antique\McLaren F1.jpg",
            "Antique\Classic Ford Deluxe.jpg"]

        self.antique_names = ["SHELBY COBRA","ROLLS-ROYCE DAWN DROPHEAD","MERCEDES SL 300 GULLWING","MCLAREN F1","CLASSIC FORD DELUXE"]
        self.antique_frames = [self.homeToSedan,self.homeToSuv,self.homeToLuxury,self.homeToAntique,self.homeToMuscle]
        self.row_count = 1
        self.column_count = 1
        self.i = 0

        for antique_path in self.antique_paths:
            self.image = Image.open(antique_path)
            self.photo = ImageTk.PhotoImage(self.image.resize((275,150)))
            self.label = tk.Label(self.antique_frame, image=self.photo)
            self.label.image = self.photo
            self.label.grid(row=self.row_count, column=self.column_count, padx=10, pady=9)
            self.car_label=tk.Button(self.antique_frame,text=self.antique_names[self.i],command=self.antique_frames[self.i])
            self.car_label.grid(row=self.row_count+1, column=self.column_count, padx=10, pady=9)

            self.i += 1
            self.column_count += 1
            if self.column_count == 3:
                self.column_count = 1
                self.row_count += 2

    # Home to Muscle
    def homeToMuscle(self):
        self.home_frame.destroy()
        self.frame_muscle()

    # Muscle to Login
    def muscleToLogin(self):
        self.muscle_frame.destroy()
        self.frame_login()

    # Muscle to Home
    def muscleToHome(self):
        self.muscle_frame.destroy()
        self.frame_home()

    # Muscle Frame
    def frame_muscle(self):
        self.master.geometry("820x1000")

        self.muscle_frame=tk.Frame(self.master,width=1000,height=1000,relief="groove",borderwidth=5)
        self.muscle_frame['background']='#6AD4DD'
        self.muscle_frame.pack()

        #Logout Button
        self.logout_label=tk.Button(self.muscle_frame,text="LOG OUT",command=self.muscleToLogin)
        self.logout_label.grid(row=0,column=2,sticky=E)

        #Back Button
        self.back_label=tk.Button(self.muscle_frame,text="BACK",command=self.muscleToHome)
        self.back_label.grid(row=0,column=1,sticky=W)

        self.muscle_paths = [
            "muscle\Pontiac Catalina.jpg",
            "muscle\Oldsmobile 442 W-30 Convertible.jpg",
            "muscle\Dodge Coronet Super Bee A12.jpg",
            "muscle\dodge charger.jpg",
            "muscle\Chevy Chevelle.jpg"]

        self.muscle_names = ["PANTIAC CATALINA","OLDSMOBILE 442 W-30 CONVERTIBLE","DODGE CORONET SUPER BEE A12","DODGE CHARGER","CHEVY CHEVELLE"]
        self.muscle_frames = [self.homeToSedan,self.homeToSuv,self.homeToLuxury,self.homeToAntique,self.homeToMuscle]
        self.row_count = 1
        self.column_count = 1
        self.i = 0

        for muscle_path in self.muscle_paths:
            self.image = Image.open(muscle_path)
            self.photo = ImageTk.PhotoImage(self.image.resize((275,150)))
            self.label = tk.Label(self.muscle_frame, image=self.photo)
            self.label.image = self.photo
            self.label.grid(row=self.row_count, column=self.column_count, padx=10, pady=9)
            self.car_label=tk.Button(self.muscle_frame,text=self.muscle_names[self.i],command=self.muscle_frames[self.i])
            self.car_label.grid(row=self.row_count+1, column=self.column_count, padx=10, pady=9)

            self.i += 1
            self.column_count += 1
            if self.column_count == 3:
                self.column_count = 1
                self.row_count += 2

    #Home to Login(logout)
    def homeToLogin(self):
        self.home_frame.destroy()
        self.frame_login()
    
    #Login Method   
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
    
        if username == "" and password == "":
            msg.showwarning("Login", "All Fields Are Mandatory")
        else:
            self.login_frame.destroy()
            self.conn=self.create_conn()
            self.cursor=self.conn.cursor()
            self.query="select * from user where fname=%s"
            self.args=(username,)
            self.cursor.execute(self.query,self.args)
            self.row=self.cursor.fetchall()

            if self.row:
                for i in self.row:
                    print(i[5])           
                    if(i[1]==username)and(i[5]==password):
                        self.frame_home()
                        self.login_frame.destroy()

                    else:
                        msg.showerror("Login", "Invalid username or password")
                        self.__init__(self.master)

            else:
                msg.showerror("Login", "Invalid username or password")
                self.__init__(self.master)

            self.conn.close()
            
    #Signup Method   
    def signup(self):
        fname=self.fname_entry.get()
        lname=self.lname_entry.get()
        mobile=self.mobile_entry.get()
        email=self.email_entry.get()
        password=self.password_entry.get()

        if fname=="" or lname=="" or mobile=="" or email=="" or password=="":
            msg.showwarning("Signup","All Fields Are Mandatory")
        else:
            if mobile.isalpha() == False:
                if len(mobile) == 10 :
                    if email.endswith("@gmail.com"):
                        self.conn=self.create_conn()
                        self.cursor=self.conn.cursor()
                        self.query="insert into user(fname,lname,mobile,email,password) values(%s,%s,%s,%s,%s)"
                        self.args=(fname,lname,mobile,email,password)
                        self.cursor.execute(self.query,self.args)
                        self.conn.commit()
                        self.conn.close()
                        msg.showinfo("Sign Up","Signup Successfull")
                        self.signupToLogin()
                    else:
                        msg.showwarning("Signup", "Enter Proper Email")
                else:
                    msg.showwarning("Signup", "Mobile Number Must Be 10 digits")
            else:
                msg.showwarning("Signup", "Enter Numbers Only.")



        

def main():
    root = tk.Tk()
    app = Automobile(root)
    root.mainloop()
    app.create_conn()

if __name__== "__main__":
    main()

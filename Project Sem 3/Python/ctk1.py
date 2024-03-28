import customtkinter as ctk
import tkinter as tk
from PIL import ImageTk, Image

class ReceptionistLogin:
    def __init__(self, master):
        self.master = master
        self.master.title("Harmony Health Center")
        self.master.geometry("450x450")
        self.master.resizable(width=False, height=False)

        self.master.config(bg="#f1f1f1")

        # create a frame for the login window
        self.login_frame = ctk.CTkFrame(self.master)
        self.login_frame.pack(pady=20)

        # create a logo with a gradient background
        self.image=Image.open("aa.jpg")
        self.photo=ImageTk.PhotoImage(self.image)
        self.l1=ctk.CTkLabel(self.login_frame, image=self.photo, text="", compound="top")
        self.l1.grid(row=1, columnspan=2, padx=10, pady=(10, 30))

        # create a gradient label for the username
        self.username_label = ctk.CTkLabel(self.login_frame, text="Username:", font=ctk.CTkFont(size=18, weight="bold"))
        self.username_label.grid(row=2, column=0, padx=10, pady=20)
        self.username_entry = ctk.CTkEntry(self.login_frame, font=ctk.CTkFont(size=14))
        self.username_entry.grid(row=2, column=1, padx=10, pady=20)

        # create a gradient label for the password
        self.password_label = ctk.CTkLabel(self.login_frame, text="Password:", font=ctk.CTkFont(size=18, weight="bold"))
        self.password_label.grid(row=3, column=0, padx=10, pady=20)
        self.password_entry = ctk.CTkEntry(self.login_frame, font=ctk.CTkFont(size=14), show="*")
        self.password_entry.grid(row=3, column=1, padx=10, pady=20)

        # create a gradient login button
        self.login_button = ctk.CTkButton(self.login_frame, text="Login", font=ctk.CTkFont(size=18, weight="bold"), command=self.login)
        self.login_button.grid(row=4, columnspan=2, padx=10, pady=40)

    def login(self):
        # handle login button click here
        pass

def main():
    root = tk.Tk()
    app = ReceptionistLogin(root)
    root.mainloop()

if __name__ == "__main__":
    main()

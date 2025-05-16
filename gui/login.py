import tkinter as tk
from tkinter import ttk ,PhotoImage,messagebox

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database import db_connection
from gui import app

class RegistrationScreen:
    def __init__(self,reg_root):
        self.reg_root=reg_root
        self.icon=PhotoImage(file='D:\\StockPredictor\\assets\\icons\\logo_black.png')
        self.reg_root.title("Create Account-Stock Prices Predictor")
        self.reg_root.geometry("1200x700")
        self.reg_root.iconphoto(True,self.icon)
        self.reg_root.resizable(False, False)
        
        # Centering the window
        x = (self.reg_root.winfo_screenwidth() // 2) - (1200 // 2)
        y = (self.reg_root.winfo_screenheight() // 2) - (700 // 2)
        self.reg_root.geometry(f"1200x700+{x}+{y}")
        #left section
        self.left_frame=tk.Frame(self.reg_root,width=400,height=700)
        self.left_frame.place(x=-0,y=0)
        self.left_bg_image=PhotoImage(file="D:\\StockPredictor\\assets\\icons\\reg_bg.png")  
        self.left_bg_label = tk.Label(self.left_frame, image=self.left_bg_image)
        self.left_bg_label.place(x=0, y=0)

        #right section
        self.right_frame=tk.Frame(self.reg_root,bg='white',width=800,height=700)
        self.right_frame.place(x=400,y=0)
        #header
        header = tk.Label(self.right_frame, text="Create a New Account", font=("Arial", 22, "bold"), fg="Red", bg="white")
        header.place(x=200, y=40)
        #name
        tk.Label(self.right_frame,text="Full Name",font=('Arial',14),bg='white').place(x=20,y=120)
        self.name_entry=ttk.Entry(self.right_frame,width=30,font=('Aria',14))
        self.name_entry.place(x=20,y=160,height=50)
        #Phone
        tk.Label(self.right_frame,text="Phone No.",font=('Arial',14),bg='white').place(x=410,y=120)
        self.phone_entry=ttk.Entry(self.right_frame,width=30,font=('Arial',14))
        self.phone_entry.place(x=410,y=160,height=50)
        #Email
        tk.Label(self.right_frame,text='Email',font=('Arial',14),bg='white').place(x=20,y=240)
        self.email_entry=ttk.Entry(self.right_frame,width=30,font=('Arial',14))
        self.email_entry.place(x=20,y=280,height=50)
        #Password
        tk.Label(self.right_frame,text='Password',font=('Arial',14),bg='white').place(x=410,y=240)
        self.password_entry=ttk.Entry(self.right_frame,font=('Arial',14),width=30,show='x')
        self.password_entry.place(x=410,y=280,height=50)
        #Register Button
        tk.Button(self.right_frame, text="Register", bg='black', fg='white',activebackground='black',activeforeground='white',font=('Arial', 14), width=25, command=self.register_user).place(x=40, y=500)
        #Back to Login
        tk.Button(self.right_frame, text="Login Account", bg='black', fg='white',activebackground='black',activeforeground='white',font=('Arial', 14), width=25, command=self.back_to_login).place(x=420, y=500)
        
        copyright_label = tk.Label(self.right_frame, text="© 2025 Stock Prices Predictor. All rights reserved.",
                                   font=("Arial", 10), fg="gray", bg="white")
        copyright_label.place(x=200, y=650)
    #Method of Back to Login
    def back_to_login(self):
        self.reg_root.destroy()
        root=tk.Tk()
        LoginScreen(root)
        root.mainloop()
    #Register 
    def register_user(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        password = self.password_entry.get()

        if not all([name, email, phone, password]):
            messagebox.showerror("Error", "Please fill all fields.")
            return
        
        # Call database function to register
        success = db_connection.register_user(name, email, phone, password)
        if success=='User_Exist':
            messagebox.showerror("Error","Email has already been Registered!")
        elif success:
            messagebox.showinfo("Success", "Account created successfully!")
            self.reg_root.destroy()
            root = tk.Tk()
            LoginScreen(root)
            root.mainloop()
        else:
            messagebox.showerror("Error", "Something went wrong during registration.")

class LoginScreen:
    def __init__(self, root):
        self.root = root
        self.icon=PhotoImage(file="D:\\StockPredictor\\assets\\icons\\logo_black.png")
        self.root.title("Login-Stock Prices Predictor")
        self.root.geometry("1200x700") 
        self.root.iconphoto(True,self.icon) 
        self.root.resizable(False, False)  

        # Centering the window
        x = (self.root.winfo_screenwidth() // 2) - (1200 // 2)
        y = (self.root.winfo_screenheight() // 2) - (700 // 2)
        self.root.geometry(f"1200x700+{x}+{y}")

        self.left_frame = tk.Frame(self.root, width=400, height=700)
        self.left_frame.place(x=0, y=0)

        self.left_bg_image = PhotoImage(file="D:\\StockPredictor\\assets\\icons\\login_bg.png")  
        self.left_bg_label = tk.Label(self.left_frame, image=self.left_bg_image)
        self.left_bg_label.place(x=0, y=0)

        # Right Panel - White (Login Section)
        self.right_frame = tk.Frame(self.root, bg="white", width=800, height=700)
        self.right_frame.place(x=400, y=0)
    
        welcome_label=tk.Label(self.right_frame,text="Welcome  Back",font=('Ananda Black Personal Use',24,"bold"),fg='black',bg='White')
        welcome_label.place(x=50,y=50)

        login_label = tk.Label(self.right_frame, text="Login to your account", font=("Arial", 22, "bold"), fg="Red", bg="white")
        login_label.place(x=200, y=150)

        # Email Field
        email_label = tk.Label(self.right_frame, text="Email Address", font=("Arial", 14), bg="white")
        email_label.place(x=200, y=230)
        self.email_entry = ttk.Entry(self.right_frame, width=35, font=('Arial', 14))
        self.email_entry.place(x=200, y=270, height=50)

        # Password Field
        password_label = tk.Label(self.right_frame, text="Password", font=("Arial", 14), bg="white")
        password_label.place(x=200, y=330)
        self.password_entry = ttk.Entry(self.right_frame, width=35, show="x", font=('Arial', 14))
        self.password_entry.place(x=200, y=370, height=50)

        # Login Button
        login_button = tk.Button(self.right_frame, text="Login", bg='#191c24',fg='white',activebackground='#191c24',activeforeground='white',font=('Arial', 14),anchor='center',width=32,command=self.login)
        login_button.place(x=200, y=440)

        # "Don't have an account?" Label
        register_label = tk.Label(self.right_frame, text="Don't have an account? ", font=("Arial", 12), bg="white")
        register_label.place(x=210, y=500)

        # "Create a new account" Clickable Label
        create_account_label = tk.Label(self.right_frame, text="Create a new account", font=("Arial", 12, "bold"),
                                        fg="blue", bg="white", cursor="hand2")
        create_account_label.place(x=410, y=500)
        create_account_label.bind("<Button-1>", self.open_registration)

        # Copyright Text
        copyright_label = tk.Label(self.root, text="© 2025 Stock Prices Predictor. All rights reserved.",
                                   font=("Arial", 10), fg="gray", bg="white")
        copyright_label.place(x=600, y=650)
    
    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        if not email or not password:
            messagebox.showerror("Login Failed", "Please enter both email and password!")
            return
        user=db_connection.authenticate_user(email,password)
        if user:
            messagebox.showinfo("Info","Login Successful!")
            self.root.destroy()
            dashboard=tk.Tk()
            app.StockApp(dashboard,user[0],user[1])
            dashboard.mainloop()
        else:
            messagebox.showerror("Error","Invalid Email or Password!")
            
           
    def open_registration(self, event):
        self.root.destroy()
        reg_root=tk.Tk()
        RegistrationScreen(reg_root)
        reg_root.mainloop()



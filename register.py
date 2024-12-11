from tkinter import *
from tkinter import messagebox
import sqlite3

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False, False)

        # Right frame for registration
        Frame_register = Frame(root, bg="#F1D9D9")
        Frame_register.place(x=0, y=0, width=1500, height=600)
        Frame_MainRegister = Frame(root, bg="#F9F1F1")
        Frame_MainRegister.place(x=440, y=50, width=380, height=500)

        # Registration form elements
        Label(Frame_MainRegister, text="Create Account", font=("Goudy old style", 18, "bold"), fg="black", bg="#F9F1F1").place(relx=0.5,anchor="center", y=30)
        
        Label(Frame_MainRegister, text="Username", font=("Goudy old style", 15, "bold"), fg="black", bg="#F9F1F1").place(x=145, y=70)
        self.username = Entry(Frame_MainRegister, font=("Goudy old style", 15), bg="#FFF9F9", highlightcolor="#EA7676",
                            highlightbackground="#EA7676", highlightthickness=1)
        self.username.place(x=70, y=100, width=260, height=35)

        Label(Frame_MainRegister, text="Full Name", font=("Goudy old style", 15, "bold"), fg="black", bg="#F9F1F1").place(x=145, y=150)
        self.fullname = Entry(Frame_MainRegister, font=("Goudy old style", 15), bg="#FFF9F9", highlightcolor="#EA7676",
                            highlightbackground="#EA7676", highlightthickness=1)
        self.fullname.place(x=70, y=180, width=260, height=35)

        Label(Frame_MainRegister, text="Password", font=("Goudy old style", 15, "bold"), fg="black", bg="#F9F1F1").place(x=145, y=230)
        self.password = Entry(Frame_MainRegister, show="*", font=("Goudy old style", 15), bg="#FFF9F9", highlightcolor="#EA7676",
                            highlightbackground="#EA7676", highlightthickness=1)
        self.password.place(x=70, y=260, width=260, height=35)

        Label(Frame_MainRegister, text="Confirm Password", font=("Goudy old style", 15, "bold"), fg="black", bg="#F9F1F1").place(x=125, y=310)
        self.confirm_password = Entry(Frame_MainRegister, show="*", font=("Goudy old style", 15), bg="#FFF9F9", highlightcolor="#EA7676",
                                    highlightbackground="#EA7676", highlightthickness=1)
        self.confirm_password.place(x=70, y=340, width=260, height=35)

        register_button = Button(Frame_MainRegister, command=self.register_user, text="Register", bd=0, 
                               font=("Goudy old style", 15), bg="#CF2F2F", fg="#F9F1F1")
        register_button.place(relx=0.5,anchor="center", y=420, width=180, height=40)

        back_label = Label(Frame_MainRegister, text="Back to Login", font=("Goudy old style", 12, "underline"), 
                          fg="#CF2F2F", bg="#F9F1F1", cursor="hand2")
        back_label.place(relx=0.5,anchor="center", y=460)
        back_label.bind('<Button-1>', lambda e: self.back_to_login())

    def register_user(self):
        if self.username.get() == "" or self.password.get() == "" or self.fullname.get() == "" or self.confirm_password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.password.get() != self.confirm_password.get():
            messagebox.showerror("Error", "Password and Confirm Password should match", parent=self.root)
        else:
            try:
                db_connection = sqlite3.connect('db/inventory.db')
                connection = db_connection.cursor()
                
                # Check if username already exists
                connection.execute("SELECT * FROM user WHERE username=?", (self.username.get(),))
                if connection.fetchone() is not None:
                    messagebox.showerror("Error", "Username already exists", parent=self.root)
                else:
                    connection.execute("INSERT INTO user (username, password, name) VALUES (?, ?, ?)",
                                    (self.username.get(), self.password.get(), self.fullname.get()))
                    db_connection.commit()
                    db_connection.close()
                    messagebox.showinfo("Success", "Registration Successful", parent=self.root)
                    self.back_to_login()
                    
            except Exception as e:
                messagebox.showerror("Error", f"Error due to: {str(e)}", parent=self.root)

    def back_to_login(self):
        self.root.destroy()
        from login import Login
        Login(Tk())

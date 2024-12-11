from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import sqlite3
from mainmenu import MainPage


class Login:
    def __init__(self, root):
        global imgs
        self.root = root
        self.root.title("Login")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False, False)
        Frame_img = Frame(root, bg="#CF2F2F")
        Frame_img.place(x=0, y=0, width=500, height=600)
        image = Image.open("images/logos/olive.png")
        resize_image = image.resize((280, 280))
        imgs = ImageTk.PhotoImage(resize_image)
        label1 = Label(Frame_img, image=imgs)
        label1.place(x=100, y=150, width=280, height=280)
        label1.image = imgs
        Frame_login = Frame(root, bg="#F1D9D9")
        Frame_login.place(x=500, y=0, width=800, height=600)
        Frame_MainLogin = Frame(Frame_login, bg="#F9F1F1")
        Frame_MainLogin.place(x=180, y=80, width=380, height=450)
        Label(Frame_MainLogin, text="Welcome to login!", font=("Goudy old style", 15, "bold"), fg="black",
              bg="#F9F1F1").place(relx=0.5,anchor="center", y=70)
        Label(Frame_MainLogin, text="Username", font=("Goudy old style", 15, "bold"), fg="black", bg="#F9F1F1").place(
            x=145, y=120)
        self.username = Entry(Frame_MainLogin, font=("Goudy old style", 15), bg="#FFF9F9", highlightcolor="#EA7676",
                              highlightbackground="#EA7676", highlightthickness=1)
        self.username.place(x=70, y=150, width=260, height=50)
        Label(Frame_MainLogin, text="Password", font=("Goudy old style", 15, "bold"), fg="black", bg="#F9F1F1").place(
            x=145, y=220)
        self.password = Entry(Frame_MainLogin,show="*",font=("Goudy old style", 15), bg="#FFF9F9", highlightcolor="#EA7676",
                              highlightbackground="#EA7676", highlightthickness=1)
        self.password.place(x=70, y=250, width=260, height=50)
        login_button = Button(Frame_MainLogin, command=self.check_function, text="Login", bd=0, font=("Goudy old style", 15),
               bg="#CF2F2F", fg="#F9F1F1")
        login_button.place(relx=0.5, y=340,anchor="center", width=180, height=40)

        self.password.bind('<Return>', lambda event: self.check_function())
        register_label = Label(Frame_MainLogin, text="No account? Register!", font=("Goudy old style", 12, "underline"), 
                      fg="#CF2F2F", bg="#F9F1F1", cursor="hand2")
        register_label.place(relx=0.5, y=410, anchor="center")

        register_label.bind('<Button-1>', lambda e: self.open_register())

        


    def check_function(self):
        self.user_name=self.username.get()
        self.pass_word=self.password.get()
        db_connection=sqlite3.connect('db/inventory.db')
        connection=db_connection.cursor()
        connection.execute("select * from user where username=? and password=?",(self.user_name,self.pass_word))
        user_details=connection.fetchall()
        if(len(user_details)==1):
            self.close_window()
            MainPage(Tk(),self.user_name,user_details[0][3])

        else:
            messagebox.showerror("Error", "Invalid username or password", parent=self.root)

    def open_register(self):
        self.root.destroy()
        from register import Register
        Register(Tk())

    def close_window(self):
        self.root.destroy()
        
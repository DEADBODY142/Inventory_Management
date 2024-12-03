from tkinter import *
from tkinter import messagebox
import pandas as p
from datetime import datetime
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
        # photo = PhotoImage(file="../img/logo.png")
        # varun_label = Label(image=photo).place(x=80, y=150, width=280, height=280)
        image = Image.open("images/logos/logo.jpg")
        resize_image = image.resize((280, 280))
        imgs = ImageTk.PhotoImage(resize_image)
        label1 = Label(Frame_img, image=imgs)
        label1.place(x=80, y=150, width=280, height=280)
        label1.image = imgs
        Frame_login = Frame(root, bg="#F1D9D9")
        Frame_login.place(x=500, y=0, width=800, height=600)
        Frame_MainLogin = Frame(Frame_login, bg="#F9F1F1")
        Frame_MainLogin.place(x=180, y=80, width=380, height=450)
        Label(Frame_MainLogin, text="Welcome to login!", font=("Goudy old style", 15, "bold"), fg="black",
              bg="#F9F1F1").place(x=110, y=30)
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
        Button(Frame_MainLogin, command=self.check_function, text="Login", bd=0, font=("Goudy old style", 15),
               bg="#CF2F2F",
               fg="#F9F1F1").place(x=115, y=340, width=180, height=40)

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

    def close_window(self):
        self.root.destroy()
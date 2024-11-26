from tkinter import *
from tkinter import messagebox
import pandas as p
from datetime import datetime
from PIL import ImageTk,Image
import sqlite3

from mainmenu import MainPage
# from forgetpass import ForgetPass
# from MainPage import MainPage


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
    #     file = p.read_csv('../Data/login.csv')
    #     self.usrname = file.username
    #     self.passwrd = file.password
    #     self.length = len(file)
    #     self.flag = 0
    #     self.user = self.username.get()
    #     self.pas = self.password.get()
    #     self.loops()

    # def loops(self):
    #     for i in range(self.length):
    #         print(self.usrname[i],self.passwrd[i])
    #         # ans=self.user == self.usrname[i] or self.pas == self.passwrd[i]
    #         # print (ans)
    #         if self.user == self.usrname[i] and self.pas == self.passwrd[i]:
    #             self.flag = 1
    #         if self.user == "" or self.pas == "":
    #             self.flag = 2
    #     print(self.flag)
    #     print(self.user, self.pas)
    #     self.check()

    # def check(self):
    #     print(self.flag)
    #     if self.flag==2:
    #         messagebox.showerror("Error", "All field are required", parent=self.root)
    #         Login(self.root)
    #     if self.flag==0:
    #         messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)
    #         Login(self.root)
    #     if self.flag==1:
    #         self.close_window()
    #         self.markAttendence(self.user)
    #         with open('../Record/login.csv', 'w') as fi:
    #             fi.writelines('Username\n')
    #             fi.writelines(self.user)
    #             fi.close()
    #         MainPage(Tk(),self.user)

    # def markAttendence(self, name):
    #     with open('../Record/Attendence.csv', 'r+') as f:
    #         mydataList = f.readlines()
    #         namelist = []
    #         print(mydataList)
    #         for line in mydataList:
    #             entry = line.split(',')
    #             namelist.append(entry[0])
    #         if name not in namelist:
    #             now = datetime.now()
    #             dtString = now.strftime('%H:%M%S')
    #             f.writelines(f'\n{name},{dtString}')

    def close_window(self):
        self.root.destroy()

    # def camera(self):
    #     self.close_window()
    #     FaceReco(True)


    # def checkpass(self):
    #     # self.close_window()
    #     ForgetPass(True)
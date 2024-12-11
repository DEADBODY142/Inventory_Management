from time import strftime
from tkinter import *

from PIL import Image, ImageTk


def timeloop(self):
    Frame_photo = Frame(self.Frame_left, bg="#FFFFFF")
    Frame_photo.place(x=25, y=20, width=200, height=250)
    Frame_line = Frame(Frame_photo, bg="#F25125")
    Frame_line.place(x=0, y=40, width=200, height=2)
    image = Image.open("images/logos/profile.jpg")
    resize_image = image.resize((140, 140))
    img = ImageTk.PhotoImage(resize_image)
    label1 = Label(Frame_photo, image=img)
    label1.place(x=27, y=50)
    label1.image = img
    Label(Frame_photo, text=self.name, font=("Goudy old style", 15, "bold"), fg="#F25125",
          bg="#FFFFFF").place(
        relx=0.5,anchor="center", y=210)
    Label(Frame_photo, text=self.usr, font=("Goudy old style", 13, "bold"), fg="#F25125", bg="#FFFFFF").place(
        relx=0.5,anchor="center", y=235)
    if (int(strftime('%S')) % 2 == 0):
        time_string = strftime('%A  %I:%M %p')
    else:
        time_string = strftime('%A  %I %M %p')
    Label(Frame_photo, text=time_string, font=("Goudy old style", 15, "bold"), fg="#F25125",
          bg="#FFFFFF").place(
        x=10, y=10)
    self.Frame_left.after(1000, self.time)

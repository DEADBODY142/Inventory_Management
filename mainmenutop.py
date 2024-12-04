from tkinter import *

from PIL import Image, ImageTk


def topPanel(self):
    Frame_Top = Frame(self.Mainmenuroot, bg="#343434")
    Frame_Top.place(x=250, y=0, width=self.width, height=60)
    image = Image.open("images/logos/logo.jpg")
    resize_image = image.resize((60, 60))
    img = ImageTk.PhotoImage(resize_image)
    label1 = Label(Frame_Top, image=img)
    label1.place(x=885, y=0)
    label1.image = img

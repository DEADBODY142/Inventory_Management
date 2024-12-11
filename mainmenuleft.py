from tkinter import *
import sqlite3

def leftPanel(self):
    self.Frame_left = Frame(self.Mainmenuroot, bg="#343434")
    self.Frame_left.place(x=0, y=0, width=250, height=int(self.height))
    self.time()
    Button(self.Frame_left, text="Add Inventory", command=self.addinventory, bd=0, font=("Goudy old style", 18),
           fg="white",
           bg="#343434").place(x=35, y=300)
    Button(self.Frame_left, text="Inventory Details", command=self.showinventorydetail, bd=0, font=("Goudy old style", 18),
           fg="white",
           bg="#343434").place(x=35, y=350)
    Button(self.Frame_left, text="Sales", command=self.showsalesdetails, bd=0, font=("Goudy old style", 18),
           fg="white",
           bg="#343434").place(x=35, y=400)
    Button(self.Frame_left, text="OOS Inventory", bd=0, command=self.showoutofstockdetails, font=("Goudy old style", 18),
           fg="white",
           bg="#343434").place(x=35, y=450)
    if self.usr=="admin":
       Button(self.Frame_left, text="Inventory Price", command=self.showpricedetails, bd=0, font=("Goudy old style", 18),
              fg="white",
              bg="#343434").place(x=35, y=500)
    Button(self.Frame_left, text="Log Out", command=self.logout, bd=0, font=("Goudy old style", 15),
           bg="white",
           fg="red").place(x=40, y=580, width=150, height=40)

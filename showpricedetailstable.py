import sqlite3
from tkinter import *
from tkinter import ttk


def Pricedetailstable(self):
    Frame_Downs = Frame(self.Frame_ViewMemberDetails, bg="#FFFFFF")
    Frame_Downs.place(x=0, y=60, width=950, height=950)
    self.Frame_Down = LabelFrame(Frame_Downs, bg="#FFFFFF")
    self.Frame_Down.place(height=600)
    self.mycanvas = Canvas(self.Frame_Down, bg="#FFFFFF")
    self.mycanvas.pack(side=LEFT, fill="both", expand=1)
    self.myframe = Frame(self.mycanvas, bg="#FFFFFF")
    self.myframe.place(x=0, y=60, width=950, height=800)
    self.mycanvas.create_window((0, 0), window=self.myframe, anchor="nw")
    self.mycanvas.bind('<Configure>', lambda e: self.mycanvas.configure(scrollregion=self.mycanvas.bbox('all')))
    yscrollbar = ttk.Scrollbar(self.Frame_Down, orient="vertical", command=self.mycanvas.yview)
    yscrollbar.pack(fill="y", side=RIGHT)
    self.mycanvas.configure(yscrollcommand=yscrollbar.set)
    self.Frame_Down.pack(fill="both", padx=10, pady=10, ipady=120)
    Label(self.myframe, text="M_ID", anchor="center", background="#f98c6e",fg="white",
          font=("Goudy old style", 12, "bold"), bd=1, relief="solid").grid(
        row=0, column=1, sticky="ew", ipadx=50)
    Label(self.myframe, text="Name", anchor="center", background="#f98c6e",fg="white",
          font=("Goudy old style", 12, "bold"), bd=1, relief="solid").grid(
        row=0, column=2, sticky="ew", ipadx=120)
    Label(self.myframe, text="Price", anchor="center", background="#f98c6e",fg="white",
          font=("Goudy old style", 12, "bold"), bd=1, relief="solid").grid(
        row=0, column=3, sticky="ew", ipadx=70)
    Label(self.myframe, text="Action", anchor="center", background="#f98c6e",fg="white",
          font=("Goudy old style", 12, "bold"), bd=1, relief="solid").grid(row=0, column=5, columnspan=2,ipadx=120, sticky="ew")
    conn = sqlite3.connect('db/inventory.db')
    c = conn.cursor()
    c.execute("SELECT * FROM inventory_price")
    self.datambr = c.fetchall()
    self.lengthofdata = len(self.datambr)
    row = 1
    for k in range(self.lengthofdata):
        nr = self.datambr[k][0]
        self.inv_price_id = k+1
        self.inv_price_name = self.datambr[k][1]
        self.inv_price_price = self.datambr[k][2]
        nr_label = Label(self.myframe, text=self.inv_price_id, anchor="center", background="#FFFFFF",
                         font=("Goudy old style", 12))
        name_label = Label(self.myframe, text=self.inv_price_name, anchor="center", background="#FFFFFF",
                           font=("Goudy old style", 12))
        price_label = Label(self.myframe, text=self.inv_price_price, anchor="center",
                             background="#FFFFFF",
                             font=("Goudy old style", 12))
        action_button = Button(self.myframe, text="Edit",
                               background="#FFFFFF", command=lambda nr=nr: self.edit_price(nr))
        action_button.place(width=10)
        action_button1 = Button(self.myframe, text="Delete", command=lambda nr=nr: self.delete(nr),
                                background="#FFFFFF")
        action_button.place(width=10)
        nr_label.grid(row=row, column=1, sticky="ew", ipady=10,)
        name_label.grid(row=row, column=2, sticky="ew")
        price_label.grid(row=row, column=3, sticky="ew")
        action_button.grid(row=row, column=5, sticky="ew", padx=5)  # View button
        action_button1.grid(row=row, column=6, sticky="ew", padx=5,ipadx=5) 
        row = row + 1

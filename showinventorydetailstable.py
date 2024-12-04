import sqlite3
from tkinter import *
from tkinter import ttk


def Inventorydetailstable(self):
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
    Label(self.myframe, text="ID", anchor="center", background="#f98c6e",fg="white",
          font=("Goudy old style", 12, "bold"), bd=1, relief="solid").grid(
        row=0, column=1, sticky="ew", ipadx=20)
    Label(self.myframe, text="Item", anchor="center", background="#f98c6e",fg="white",
          font=("Goudy old style", 12, "bold"), bd=1, relief="solid").grid(
        row=0, column=2, sticky="ew", ipadx=100)
    Label(self.myframe, text="Quantity", anchor="center", background="#f98c6e",fg="white",
          font=("Goudy old style", 12, "bold"), bd=1, relief="solid").grid(
        row=0, column=3, sticky="ew", ipadx=55)
    Label(self.myframe, text="Price", anchor="center", background="#f98c6e",fg="white",
          font=("Goudy old style", 12, "bold"), bd=1, relief="solid").grid(
        row=0, column=4, sticky="ew", ipadx=55)
    Label(self.myframe, text="Action", anchor="center", background="#f98c6e",fg="white",
          font=("Goudy old style", 12, "bold"), bd=1, relief="solid").grid(row=0, column=5, columnspan=3,ipadx=120, sticky="ew")
    conn = sqlite3.connect('db/inventory.db')
    c = conn.cursor()
    c.execute("SELECT * FROM inventory_stock where quantity >0")
    self.datambr = c.fetchall()
    self.lengthofdata = len(self.datambr)
    row = 1
    for k in range(self.lengthofdata):
        nr = self.datambr[k][0]
        self.inv_id = k+1
        self.inv_name = self.datambr[k][1]
        self.inv_quantity = self.datambr[k][3]
        self.inv_price = self.datambr[k][4]
        nr_label = Label(self.myframe, text=self.inv_id, anchor="center", background="#FFFFFF",
                         font=("Goudy old style", 12))
        name_label = Label(self.myframe, text=self.inv_name, anchor="center", background="#FFFFFF",
                           font=("Goudy old style", 12))
        quantity_label = Label(self.myframe, text=self.inv_quantity, anchor="center",
                             background="#FFFFFF",
                             font=("Goudy old style", 12))
        price_label = Label(self.myframe, text=self.inv_price, anchor="center",
                             background="#FFFFFF",
                             font=("Goudy old style", 12))
        action_button = Button(self.myframe, text="Edit",
                               background="#FFFFFF", command=lambda nr=nr: self.edit_inventory(nr))
        action_button.place(width=5)
        action_button2 = Button(self.myframe, text="Purchase", command=lambda nr=nr, qty=self.inv_quantity: self.sales_inventory(nr,qty),
                                background="#FFFFFF")
        action_button.place(width=5)
        action_button1 = Button(self.myframe, text="Delete", command=lambda nr=nr: self.delete_inventory(nr),
                                background="#FFFFFF")
        action_button.place(width=5)
        nr_label.grid(row=row, column=1, sticky="ew", ipady=10,)
        name_label.grid(row=row, column=2, sticky="ew")
        quantity_label.grid(row=row, column=3, sticky="ew")
        price_label.grid(row=row, column=4, sticky="ew")
        action_button.grid(row=row, column=5, sticky="ew", padx=5)
        action_button2.grid(row=row, column=6, sticky="ew", padx=5,ipadx=5) 
        action_button1.grid(row=row, column=7, sticky="ew", padx=5,ipadx=5) 
        row = row + 1

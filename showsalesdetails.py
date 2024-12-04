import sqlite3
from tkinter import *
from tkinter import ttk

def SalesInventoryViewDetailsPanel(self):
    self.Frame_ViewMemberDetails = Frame(self.Mainmenuroot, bg="white")
    self.Frame_ViewMemberDetails.place(x=250, y=60, width=950, height=950)
    Frame_Top = Frame(self.Frame_ViewMemberDetails, bg="#F98C6E")
    Frame_Top.place(x=0, y=0, width=950, height=60)
    Label(Frame_Top, text="Sales Details", font=("Goudy old style", 15, "bold"), fg="#FFFFFF",
          bg="#F98C6E").place(
        x=10, y=15)

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
    Label(self.myframe, text="ID", anchor="center",background="#f98c6e",fg="white",
          font=("Goudy old style", 12, "bold"), bd=1, relief="solid").grid(
        row=0, column=1, sticky="ew", ipadx=70)
    Label(self.myframe, text="Item", anchor="center",background="#f98c6e",fg="white",
          font=("Goudy old style", 12, "bold"), bd=1, relief="solid").grid(
        row=0, column=2, sticky="ew", ipadx=70)
    Label(self.myframe, text="Quantity", anchor="center",background="#f98c6e",fg="white",
          font=("Goudy old style", 12, "bold"), bd=1, relief="solid").grid(
        row=0, column=3, sticky="ew", ipadx=70)
    Label(self.myframe, text="Price", anchor="center",background="#f98c6e",fg="white",
          font=("Goudy old style", 12, "bold"), bd=1, relief="solid").grid(
        row=0, column=4, sticky="ew", ipadx=70)
    Label(self.myframe, text="Date", anchor="center",background="#f98c6e",fg="white",
          font=("Goudy old style", 12, "bold"), bd=1, relief="solid").grid(
        row=0, column=5, sticky="ew", ipadx=70)
    conn = sqlite3.connect('db/inventory.db')
    c = conn.cursor()
    c.execute("SELECT * FROM inventory_purchase")
    self.datambr = c.fetchall()
    self.lengthofdata = len(self.datambr)
    row = 1
    for k in range(self.lengthofdata):
        # nr = self.datambr[k][0]
        self.inv_id = k+1
        self.inv_name = self.datambr[k][1]
        self.inv_quantity = self.datambr[k][2]
        self.inv_price = self.datambr[k][3]
        self.inv_date = self.datambr[k][4]
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
        date_label = Label(self.myframe, text=self.inv_date, anchor="center",
                             background="#FFFFFF",
                             font=("Goudy old style", 12))
        nr_label.grid(row=row, column=1, sticky="ew", ipady=10,)
        name_label.grid(row=row, column=2, sticky="ew")
        quantity_label.grid(row=row, column=3, sticky="ew")
        price_label.grid(row=row, column=4, sticky="ew")
        date_label.grid(row=row, column=5, sticky="ew")
        row = row + 1
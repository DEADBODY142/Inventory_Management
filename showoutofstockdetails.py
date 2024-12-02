import sqlite3
from tkinter import *

def OutofStockInventoryViewDetailsPanel(self):
    self.Frame_ViewMemberDetails = Frame(self.Mainmenuroot, bg="white")
    self.Frame_ViewMemberDetails.place(x=250, y=60, width=950, height=950)
    Frame_Top = Frame(self.Frame_ViewMemberDetails, bg="#F98C6E")
    Frame_Top.place(x=0, y=0, width=950, height=60)
    Label(Frame_Top, text="Out of Stock Inventory Details", font=("Goudy old style", 15, "bold"), fg="#FFFFFF",
          bg="#F98C6E").place(
        x=10, y=15)
    # Label(Frame_Top, text="Search", font=("Goudy old style", 12, "bold"), fg="#FFFFFF",
    #       bg="#F98C6E").place(
    #     x=300, y=15)
    self.search = Entry(Frame_Top, font=("Goudy old style", 15), bg="#FFF9F9", highlightcolor="#EA7676",
                        highlightbackground="#EA7676", highlightthickness=1)
    self.search.place(x=280, y=15, width=500, height=30)
    # Label(Frame_Top, text="Month", font=("Goudy old style", 12, "bold"), fg="#FFFFFF",
    #       bg="#F98C6E").place(
    #     x=600, y=15)
    self.search.bind("<KeyRelease>",NONE)

    
    # Table Frame
    Frame_Table = Frame(self.Frame_ViewMemberDetails, bg="white")
    Frame_Table.place(x=0, y=70, width=950, height=880)

    # Adding Canvas for Table
    canvas = Canvas(Frame_Table, bg="white", bd=0, highlightthickness=0)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Adding Table Header
    header = ["ID", "Item Name", "Price"]
    header_bg = "#F98C6E"
    header_fg = "#FFFFFF"
    for col, text in enumerate(header):
        Label(canvas, text=text, font=("Goudy old style", 12, "bold"), bg=header_bg, fg=header_fg,
              relief=GROOVE, padx=10, pady=5).grid(row=0, column=col, sticky="nsew")

    # Sample Data
    db_connection = sqlite3.connect('db/inventory.db')
    cursor = db_connection.cursor()
    cursor.execute("SELECT name,price FROM inventory_stock where quantity=?",(0,))
    inventory_details = cursor.fetchall()
    # data = [
    #     [1, "Laptop", 10, "$1200", "Electronics"],
    #     [2, "Table", 5, "$150", "Furniture"],
    #     [3, "Notebook", 50, "$2", "Stationery"],
    #     [4, "Smartphone", 25, "$800", "Electronics"],
    #     [5, "Chair", 15, "$50", "Furniture"]
    # ]
    
     # Adding Table Rows
    for row_idx, row_data in enumerate(inventory_details, start=1):
        bg_color = "#F9F9F9" if row_idx % 2 == 0 else "#FFFFFF"
        # First create the auto-increment column
        Label(canvas, text=str(row_idx), font=("Goudy old style", 12), bg=bg_color, fg="#333333",
            relief=GROOVE, padx=10, pady=5).grid(row=row_idx, column=0, sticky="nsew")
    
        for col_idx, cell_data in enumerate(row_data):
            Label(canvas, text=cell_data, font=("Goudy old style", 12), bg=bg_color, fg="#333333",
                relief=GROOVE, padx=10, pady=5).grid(row=row_idx, column=col_idx + 1, sticky="nsew")
    
    # Configuring column weights for uniform size
    for col in range(len(header)):
        canvas.grid_columnconfigure(col, weight=1)
    # todo: quantity 0 show
    # options = [
    #     "....",
    #     "1month",
    #     "3months",
    #     "6months"
    # ]
    # self.monthss = StringVar()
    # self.monthss.set("....")
    # self.setmonths = OptionMenu(Frame_Top, self.monthss, *options, command=None)
    # self.setmonths.configure(background="white")
    # self.setmonths.place(x=660, y=15, width=100)
    # Label(Frame_Top, text="Shift", font=("Goudy old style", 12, "bold"), fg="#FFFFFF",
    #       bg="#F98C6E").place(
    #     x=780, y=15)
    # options = [
    #     "....",
    #     "Morning",
    #     "Evening"
    # ]
    # self.shiftss = StringVar()
    # self.shiftss.set("....")
    # self.shifts = OptionMenu(Frame_Top, self.shiftss, *options, command=None)
    # self.shifts.configure(background="white")
    # self.shifts.place(x=820, y=15, width=100)
    # showmemberstable(self)

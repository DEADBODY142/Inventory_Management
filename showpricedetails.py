# from tkinter import *
# import sqlite3


# def PriceInventoryViewDetailsPanel(self):
#     # Initial Setup
#     self.Frame_ViewMemberDetails = Frame(self.Mainmenuroot, bg="white")
#     self.Frame_ViewMemberDetails.place(x=0, y=0, width=1199, height=650)

#     # Top Frame for Header
#     Frame_Top = Frame(self.Frame_ViewMemberDetails, bg="#F98C6E")
#     Frame_Top.place(x=0, y=0, width=1199, height=50)
#     Label(Frame_Top, text="Price Inventory Details", font=("Goudy old style", 15, "bold"), fg="#FFFFFF",
#           bg="#F98C6E").place(x=10, y=15)

#     self.search = Entry(Frame_Top, font=("Goudy old style", 15), bg="#FFF9F9", highlightcolor="#EA7676",
#                         highlightbackground="#EA7676", highlightthickness=1)
#     self.search.place(x=400, y=10, width=500, height=30)

#     # Table Frame
#     Frame_Table = Frame(self.Frame_ViewMemberDetails, bg="white")
#     Frame_Table.place(x=0, y=50, width=1199, height=550)

#     # Footer Frame for Pagination Buttons
#     Frame_Footer = Frame(self.Frame_ViewMemberDetails, bg="#F2F2F2", relief=RIDGE, bd=1)
#     Frame_Footer.place(x=0, y=600, width=1199, height=50)

#     # Fetch Data from Database
#     try:
#         db_connection = sqlite3.connect('db/inventory.db')
#         cursor = db_connection.cursor()
#         cursor.execute("SELECT * FROM inventory_price")
#         self.user_details = cursor.fetchall()
#     except sqlite3.Error as e:
#         print(f"Database Error: {e}")
#         self.user_details = []
#     finally:
#         db_connection.close()

#     # Variables for Pagination
#     self.current_page = 0
#     self.items_per_page = 15
#     self.total_pages = len(self.user_details) // self.items_per_page
#     if len(self.user_details) % self.items_per_page > 0:
#         self.total_pages += 1

#     # Function to Render Data on the Current Page
#     def render_table():
#         for widget in Frame_Table.winfo_children():
#             widget.destroy()

#         # Adding Table Header
#         header = ["ID", "Item Name", "Price"]
#         header_bg = "#F98C6E"
#         header_fg = "#FFFFFF"
#         for col, text in enumerate(header):
#             Label(Frame_Table, text=text, font=("Goudy old style", 12, "bold"), bg=header_bg, fg=header_fg,
#                   relief=GROOVE, padx=10, pady=5, width=25).grid(row=0, column=col, sticky="nsew")

#         # Calculate Start and End Indices for Current Page
#         start_idx = self.current_page * self.items_per_page
#         end_idx = start_idx + self.items_per_page

#         # Display Data Rows
#         for row_idx, row_data in enumerate(self.user_details[start_idx:end_idx], start=1):
#             bg_color = "#F9F9F9" if row_idx % 2 == 0 else "#FFFFFF"
#             for col_idx, cell_data in enumerate(row_data):
#                 Label(Frame_Table, text=cell_data, font=("Goudy old style", 12), bg=bg_color, fg="#333333",
#                       relief=GROOVE, padx=10, pady=5, width=25).grid(row=row_idx, column=col_idx, sticky="nsew")

#     # Function to Handle Pagination Buttons
#     def go_to_page(page):
#         if 0 <= page < self.total_pages:
#             self.current_page = page
#             render_table()
#             update_pagination_buttons()

#     # Update Pagination Buttons
#     def update_pagination_buttons():
#         for widget in Frame_Footer.winfo_children():
#             widget.destroy()

#         Button(Frame_Footer, text="Previous", font=("Goudy old style", 12), bg="#F98C6E", fg="white",
#                command=lambda: go_to_page(self.current_page - 1),
#                state=DISABLED if self.current_page == 0 else NORMAL).pack(side=LEFT, padx=10)

#         Label(Frame_Footer, text=f"Page {self.current_page + 1} of {self.total_pages}", font=("Goudy old style", 12),
#               bg="#F2F2F2", fg="black").pack(side=LEFT, padx=20)

#         Button(Frame_Footer, text="Next", font=("Goudy old style", 12), bg="#F98C6E", fg="white",
#                command=lambda: go_to_page(self.current_page + 1),
#                state=DISABLED if self.current_page == self.total_pages - 1 else NORMAL).pack(side=LEFT, padx=10)

#     # Initial Rendering
#     render_table()
#     update_pagination_buttons()


from tkinter import *
import sqlite3
def PriceInventoryViewDetailsPanel(self):
    self.Frame_ViewMemberDetails = Frame(self.Mainmenuroot, bg="white")
    self.Frame_ViewMemberDetails.place(x=250, y=60, width=950, height=950)
    
    # Top Frame for Inventory Details
    Frame_Top = Frame(self.Frame_ViewMemberDetails, bg="#F98C6E")
    Frame_Top.place(x=0, y=0, width=950, height=60)
    Label(Frame_Top, text="Inventory Price", font=("Goudy old style", 15, "bold"), fg="#FFFFFF",
          bg="#F98C6E").place(x=10, y=15)
    
    self.search = Entry(Frame_Top, font=("Goudy old style", 15), bg="#FFF9F9", highlightcolor="#EA7676",
                        highlightbackground="#EA7676", highlightthickness=1)
    self.search.place(x=250, y=15, width=500, height=30)
    self.search.bind("<KeyRelease>", NONE)
    
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
    cursor.execute("SELECT * FROM inventory_price")
    price = cursor.fetchall()
    # data = [
    #     [1, "Laptop", 10, "$1200", "Electronics"],
    #     [2, "Table", 5, "$150", "Furniture"],
    #     [3, "Notebook", 50, "$2", "Stationery"],
    #     [4, "Smartphone", 25, "$800", "Electronics"],
    #     [5, "Chair", 15, "$50", "Furniture"]
    # ]
    
    # Adding Table Rows
    for row_idx, row_data in enumerate(price, start=1):
        bg_color = "#F9F9F9" if row_idx % 2 == 0 else "#FFFFFF"
        for col_idx, cell_data in enumerate(row_data):
            Label(canvas, text=cell_data, font=("Goudy old style", 12), bg=bg_color, fg="#333333",
                  relief=GROOVE, padx=10, pady=5).grid(row=row_idx, column=col_idx, sticky="nsew")
    
    # Configuring column weights for uniform size
    for col in range(len(header)):
        canvas.grid_columnconfigure(col, weight=1)
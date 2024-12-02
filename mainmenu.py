from tkinter import *
from addinventory import AddInventoryPanel
from mainmenuleft import leftPanel
from mainmenushowtime import timeloop
from mainmenutop import topPanel
from showinventorydetails import InventoryViewDetailsPanel
from showoutofstockdetails import OutofStockInventoryViewDetailsPanel
# from showpricedetails import PriceInventoryViewDetailsPanel
from showpricedetails import PriceInventoryViewDetailsPanel
from showpricedetailstable import Pricedetailstable
from showpurchasedetails import PurchaseInventoryViewDetailsPanel
from tkinter import messagebox
import sqlite3




class MainPage:
    def __init__(self, Mainmenuroot, usr, name):
        Mainmenuroot.after(0, Mainmenuroot.deiconify)
        self.name = name
        self.usr = usr
        self.dateto = "Choose date"
        self.datefrom = "Choose date"
        self.updatedateto = "Choose date"
        self.updatedatefrom = "Choose date"
        self.updatedatefromabsnt= "Choose date"
        self.updatedatetoabsnt = "Choose date"
        self.Mainmenuroot = Mainmenuroot
        self.Mainmenuroot.title("Main")
        self.width = "1199"
        self.height = "650"
        self.mbmrid = ""
        self.lst=[]
        self.count=-1
        self.Mainmenuroot.geometry(self.width + "x" + self.height + "+100+30")
        self.Mainmenuroot.resizable(False, False)
        self.a = 0
        self.month = ""
        self.left()
        self.top()
        # self.deactivembr()
        # self.sendmain()
        # self.dashboard()


    def left(self):
        leftPanel(self)

    def time(self):
        timeloop(self)

    def top(self):
        topPanel(self)

    # def dashboard(self):
    #     DashBoardPanel(self)

    def logout(self):
        self.close_window_mainmenu()
        from login import Login
        Login(Tk())

    # def myprofile(self):
    #     ProfilePanel(self)

    # def addmembers(self):
    #     AddMemberPanel(self)

    # def inputvalidation(self):
    #     memberformvalidation(self)

    # def addpaymentdetails(self):
    #     AddMemberPaymentPanel(self)

    # def getdatefrom(self):
    #     getdatefrommember(self)

    # def getdateto(self):
    #     getdatetomember(self)

    # def getmemberinfo(self):
    #     GetfullInfo(self)

    def addinventory(self):
        AddInventoryPanel(self)
    def showinventorydetail(self):
        InventoryViewDetailsPanel(self)
    def showoutofstockdetails(self):
        OutofStockInventoryViewDetailsPanel(self)
    def showpricedetails(self):
        PriceInventoryViewDetailsPanel(self)
    def showpurchasedetails(self):
        PurchaseInventoryViewDetailsPanel(self)
    def showpricedetailstable(self):
         Pricedetailstable(self)
    
    def add(self):
        add_window = Toplevel()
        add_window.title("Add Price Details")
        add_window.geometry("300x200")
        add_window.configure(bg="#FFFFFF")
        
        # Create entry fields
        Label(add_window, text="Name:", bg="#FFFFFF", font=("Goudy old style", 12)).pack(pady=5)
        name_entry = Entry(add_window)
        name_entry.pack(pady=5)
        
        Label(add_window, text="Price:", bg="#FFFFFF", font=("Goudy old style", 12)).pack(pady=5)
        price_entry = Entry(add_window)
        price_entry.pack(pady=5)

        def save_new_record():
            new_name = name_entry.get()
            new_price = price_entry.get()
            
            conn = sqlite3.connect('db/inventory.db')
            c = conn.cursor()
            c.execute("INSERT INTO inventory_price (name, price) VALUES (?, ?)", 
                    (new_name, new_price))
            conn.commit()
            conn.close()
            
            messagebox.showinfo("Success", "Record added successfully!")
            add_window.destroy()
            
            # Refresh the table
            for widget in self.myframe.winfo_children():
                widget.destroy()
            self.showpricedetailstable()

        # Save button
        Button(add_window, text="Save", command=save_new_record, 
                bg="#4CAF50", fg="white", font=("Goudy old style", 12)).pack(pady=20)
        
    def delete(self, nr):
        response = messagebox.askyesno("Delete", "Are you sure you want to delete this record?")
        if response:
            conn = sqlite3.connect('db/inventory.db')
            c = conn.cursor()
            c.execute("DELETE FROM inventory_price WHERE id=?", (nr,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Record deleted successfully!")
            
            # Clear existing widgets in myframe
            for widget in self.myframe.winfo_children():
                widget.destroy()
                
            # Reload the table
            self.showpricedetailstable()
    def edit_price(self, nr):
    # Create edit dialog window
        edit_window = Toplevel()
        edit_window.title("Edit Price Details")
        edit_window.geometry("300x200")
        edit_window.configure(bg="#FFFFFF")
        
        # Get current values from database
        conn = sqlite3.connect('db/inventory.db')
        c = conn.cursor()
        c.execute("SELECT * FROM inventory_price WHERE id=?", (nr,))
        current_data = c.fetchone()
        conn.close()
        
        # Create entry fields
        Label(edit_window, text="Name:", bg="#FFFFFF", font=("Goudy old style", 12)).pack(pady=5)
        name_entry = Entry(edit_window)
        name_entry.insert(0, current_data[1])
        name_entry.pack(pady=5)
        
        Label(edit_window, text="Price:", bg="#FFFFFF", font=("Goudy old style", 12)).pack(pady=5)
        price_entry = Entry(edit_window)
        price_entry.insert(0, current_data[2])
        price_entry.pack(pady=5)
    
        def save_changes():
            new_name = name_entry.get()
            new_price = price_entry.get()
            
            conn = sqlite3.connect('db/inventory.db')
            c = conn.cursor()
            c.execute("UPDATE inventory_price SET name=?, price=? WHERE id=?", 
                    (new_name, new_price, nr))
            conn.commit()
            conn.close()
            
            messagebox.showinfo("Success", "Record updated successfully!")
            edit_window.destroy()
            
            # Refresh the table
            for widget in self.myframe.winfo_children():
                widget.destroy()
            self.showpricedetailstable()
    
    # Save button
        Button(edit_window, text="Save", command=save_changes, 
                bg="#4CAF50", fg="white", font=("Goudy old style", 12)).pack(pady=20)

    
    # def showmemberinformation(self, monthsss):
    #     showmemberinfo(self, 1, self.monthss.get(), self.shiftss.get())

    # def fulldetailss(self, num):
    #     fulldetails(self, num)
    # def sendmain(self):
    #     sendmail(self)
    # def delete(self, num):
    #     memberdelete(self, num)

    # def paymentdetials(self):
    #     PaymentPanel(self)

    # def updtepayment(self, num):
    #     UpdatePayments(self, num)

    # def updatedb(self):
    #     updateintodb(self)

    # def updategetdatefrom(self):
    #     updategetdatefrommember(self)

    # def updategetdateto(self):
    #     updategetdatetomember(self)

    # def attendnce(self):
    #     AttendencePanel(self)

    # def showattendence(self, monthsss):
    #     showmemberattendence(self, 1, self.shiftsss.get())

    # def presentmemberss(self, num):
    #     presentmembers(self, num)

    # def deactivembr(self):
    #     deactivatemember(self)

    # def makesearch(self,event):
    #     SearchMember(self,event)
    #     SerchMemberDetials(self,self.lst)
    # def updateaftrasbnt(self,num):
    #     UpdatePaymentAfterAbsent(self, num)

    # def updatedbs(self):
    #     updateintodbss(self)
    # def updategetdatefromabsnts(self):
    #     updategetdatefrommemberabsnt(self)

    # def updategetdatetoabsnts(self):
    #     updategetdatetomemberabsnt(self)

    def close_window_mainmenu(self):
        self.Mainmenuroot.destroy()



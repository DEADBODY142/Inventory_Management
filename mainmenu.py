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



from tkinter import *

def PurchaseInventoryViewDetailsPanel(self):
    self.Frame_ViewMemberDetails = Frame(self.Mainmenuroot, bg="white")
    self.Frame_ViewMemberDetails.place(x=250, y=60, width=950, height=950)
    Frame_Top = Frame(self.Frame_ViewMemberDetails, bg="#F98C6E")
    Frame_Top.place(x=0, y=0, width=950, height=60)
    Label(Frame_Top, text="Purchase Inventory Details", font=("Goudy old style", 15, "bold"), fg="#FFFFFF",
          bg="#F98C6E").place(
        x=10, y=15)
    # Label(Frame_Top, text="Search", font=("Goudy old style", 12, "bold"), fg="#FFFFFF",
    #       bg="#F98C6E").place(
    #     x=300, y=15)
    # self.search = Entry(Frame_Top, font=("Goudy old style", 15), bg="#FFF9F9", highlightcolor="#EA7676",
    #                     highlightbackground="#EA7676", highlightthickness=1)
    # self.search.place(x=250, y=15, width=500, height=30)
    # # Label(Frame_Top, text="Month", font=("Goudy old style", 12, "bold"), fg="#FFFFFF",
    # #       bg="#F98C6E").place(
    # #     x=600, y=15)
    # self.search.bind("<KeyRelease>",NONE)

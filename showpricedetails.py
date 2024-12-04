from tkinter import *

def PriceInventoryViewDetailsPanel(self):
    self.Frame_ViewMemberDetails = Frame(self.Mainmenuroot, bg="white")
    self.Frame_ViewMemberDetails.place(x=250, y=60, width=950, height=950)
    Frame_Top = Frame(self.Frame_ViewMemberDetails, bg="#F98C6E")
    Frame_Top.place(x=0, y=0, width=950, height=60)
    Label(Frame_Top, text="Price Inventory Details", font=("Goudy old style", 15, "bold"), fg="#FFFFFF",
          bg="#F98C6E").place(
        x=10, y=15)

 # Add this after the search bar placement
    search_button = Button(Frame_Top, text="Add", font=("Goudy old style", 12), 
                          bg="#FFFFFF", fg="#F98C6E",
                          cursor="hand2",command=self.add)
    search_button.place(x=850, y=15, width=80, height=30)

    self.showpricedetailstable()
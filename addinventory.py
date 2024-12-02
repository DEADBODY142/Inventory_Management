from tkinter import *
import subprocess

def AddInventoryPanel(self):
    self.Frame_ViewMemberDetails = Frame(self.Mainmenuroot, bg="white")
    self.Frame_ViewMemberDetails.place(x=250, y=60, width=950, height=950)
    label = Label(self.Frame_ViewMemberDetails, text="Scan Your Inventory", font=("Bodoni 72 Smallcaps", 20, "bold"),
                  bg="white", fg="#343434")
    label.place(y=-30,relx=0.5, rely=0.4, anchor=CENTER)
    scan_button = Button(self.Frame_ViewMemberDetails, text="Click Here for Scan", font=("Goudy old style", 15, "bold"),
                         bg="#F98C6E", fg="white", padx=20, pady=10, command=lambda: run_snapshot())
    scan_button.place(x=-12,y=-200,relx=0.5, rely=0.5, anchor=CENTER)

def run_snapshot():
    try:
            # subprocess.run(["python", "Login.py"], check=True)  
        # subprocess.run(["python", "snapshot.py"], check=True)  
        
        subprocess.run(["python", "add.py"], check=True)  
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
    except FileNotFoundError as e:
        print(f"Script not found: {e}")



    # Frame_Top = Frame(self.Frame_ViewMemberDetails, bg="#F98C6E")
    # Frame_Top.place(x=0, y=0, width=950, height=60)
    # Label(Frame_Top, text="Out of Stock Inventory Details", font=("Goudy old style", 15, "bold"), fg="#FFFFFF",
    #       bg="#F98C6E").place(
    #     x=10, y=15)
    # Label(Frame_Top, text="Search", font=("Goudy old style", 12, "bold"), fg="#FFFFFF",
    #       bg="#F98C6E").place(
    #     x=300, y=15)
    # self.search = Entry(Frame_Top, font=("Goudy old style", 15), bg="#FFF9F9", highlightcolor="#EA7676",
    #                     highlightbackground="#EA7676", highlightthickness=1)
    # self.search.place(x=280, y=15, width=500, height=30)
    # Label(Frame_Top, text="Month", font=("Goudy old style", 12, "bold"), fg="#FFFFFF",
    #       bg="#F98C6E").place(
    #     x=600, y=15)
    # self.search.bind("<KeyRelease>",NONE)

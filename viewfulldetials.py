from tkinter import *

from Modules.Controller.showmemberdetials.getmemberderials import memberdetaialsdisplay


def fulldetails(self, num):
    self.Frame_Memberprofile = Frame(self.Mainmenuroot, bg="white")
    self.Frame_Memberprofile.place(x=250, y=60, width=950, height=950)
    Button(self.Frame_Memberprofile, text="Back", command=self.showmemberdetails, bd=0,
           font=("Goudy old style", 15),
           bg="#F25125",
           fg="#F9F1F1").place(x=40, y=10, width=80, height=40)
    Label(self.Frame_Memberprofile, text="Details of Member", font=("Goudy old style", 20, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=300, y=10)
    Label(self.Frame_Memberprofile, text="M_Id :", font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=40, y=80)
    Label(self.Frame_Memberprofile, text="Name :", font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=40, y=130)
    Label(self.Frame_Memberprofile, text="Blood Group :", font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=480, y=130)
    Label(self.Frame_Memberprofile, text="Age :", font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=480, y=180)
    Label(self.Frame_Memberprofile, text="Address :", font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=40, y=180)
    Label(self.Frame_Memberprofile, text="Mobile_No :", font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=480, y=230)
    Label(self.Frame_Memberprofile, text="Email :", font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=40, y=230)
    Label(self.Frame_Memberprofile, text="Gender :", font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=480, y=280)
    Label(self.Frame_Memberprofile, text="Member Details :", font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=40, y=280)
    Label(self.Frame_Memberprofile, text="MembershipPaymentDate :", font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=40, y=330)
    Label(self.Frame_Memberprofile, text="Membership Expiry Date :", font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=480, y=330)
    Label(self.Frame_Memberprofile, text="Membership Package :", font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=40, y=380)
    Label(self.Frame_Memberprofile, text="Member Paid :", font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=480, y=380)
    Label(self.Frame_Memberprofile, text="Membership ApprovedBy :", font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=480, y=430)
    Label(self.Frame_Memberprofile, text="Memership Status:", font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=40, y=430)
    Label(self.Frame_Memberprofile, text="Memership Shift:", font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=40, y=480)
    memberdetaialsdisplay(self, num)

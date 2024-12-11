from tkinter import *

from login import Login


class Welcome:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome")
        self.root.geometry("1199x600+100+50")
        # Disable resizing
        self.root.resizable(False, False)


        # Welcome frame
        Frame_Welcome = Frame(self.root, bg="#F1D9D9")
        Frame_Welcome.place(x=0, y=0, width=1199, height=600)

        # Title
        title = Label(
            Frame_Welcome, 
            text="OLIVE MART\nInventory Management Software", 
            font=("Goudy Old Style", 45), 
            fg="black", 
            bg="#F1D9D9"
        )
        title.place(relx=0.5, anchor=CENTER, y=220)

        # Get Started button
        Button(
            Frame_Welcome,
            command=self.login_function,
            # command='',  # Call function to run snapshot.py and object.py
                # Call function to run snapshot.py and object.py
            text="Go to Login",
            bd=0,
            font=("Goudy Old Style", 15, "bold"),
            fg="white",
            bg="#CF2F2F"
        ).place(x=500, y=350, width=200, height=50)
        
    def login_function(self):
        self.close_window()
        Login(Tk())

    def close_window(self):
        welcome_root.destroy()



# Create the Tkinter root window and run the application
welcome_root = Tk()
obj = Welcome(welcome_root)
welcome_root.mainloop()

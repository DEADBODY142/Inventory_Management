from tkinter import *

from login import Login
# from PIL import ImageTk
# import subprocess  # For running external scripts
# from Login import Login


class Welcome:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome Page")
        self.root.geometry("1199x600+100+50")
        # Disable resizing
        self.root.resizable(False, False)

        # Uncomment and use the following lines if you have a background image:
        # self.bg = ImageTk.PhotoImage(file="path_to_your_image.jpg")  # Replace with your image path
        # Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # Welcome frame
        Frame_Welcome = Frame(self.root, bg="#F1D9D9")
        Frame_Welcome.place(x=0, y=0, width=1199, height=600)

        # Title
        title = Label(
            Frame_Welcome, 
            text="Inventory Management Software", 
            font=("Goudy Old Style", 45), 
            fg="black", 
            bg="#F1D9D9"
        )
        title.place(x=210, y=200)

        # Get Started button
        Button(
            Frame_Welcome,
            command=self.login_fuction,
            # command='',  # Call function to run snapshot.py and object.py
                # Call function to run snapshot.py and object.py
            text="Go to Login",
            bd=0,
            font=("Goudy Old Style", 15, "bold"),
            fg="white",
            bg="#CF2F2F"
        ).place(x=500, y=350, width=200, height=50)
        
    def login_fuction(self):
        self.close_window()
        Login(Tk())

    def close_window(self):
        welcome_root.destroy()


    # def run_scripts(self):
    #     # Function to execute snapshot.py followed by object.py
    #     try:
    #         # subprocess.run(["python", "Login.py"], check=True)  
    #         subprocess.run(["python", "snapshot.py"], check=True)  
            
    #         subprocess.run(["python", "build_scratch.py"], check=True)  
    #     except subprocess.CalledProcessError as e:
    #         print(f"An error occurred: {e}")
    #     except FileNotFoundError as e:
    #         print(f"Script not found: {e}")

# Create the Tkinter root window and run the application
welcome_root = Tk()
obj = Welcome(welcome_root)
welcome_root.mainloop()

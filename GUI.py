from tkinter import *

class Gui:
    def __init__(self, master):
        self.master = master        # The master attribute gives access to the root window (Tk)
        master.title("Dashboard")
        master.geometry("1280x720")

        # make mainframe
        self.mainframe=Frame(root,bg="red")
        self.mainframe.pack(fill="both",expand=True)
        # give mainframe grid layout
        self.mainframe.grid_rowconfigure(0, weight=1)
        self.mainframe.grid_columnconfigure(1, weight=1)

        # make Frames (container) that go into mainframe
        self.right_frame = Frame(self.mainframe, bg="lightblue")
        self.left_frame = Frame(self.mainframe, bg="grey", width=100)
        self.left_frame.grid(row=0, column=0, sticky="ns")
        self.right_frame.grid(row=0, column=1, sticky="nsew")

        # make buttons
        self.makeBtns()

    def makeBtns(self):
        self.btn_temp = Button(self.left_frame, text="Temperatuur", fg="black", width=25, height=5)
        self.btn_licht = Button(self.left_frame, text="Licht", fg="black", width=25, height=5)
        self.btn_home = Button(self.left_frame, text="Home", fg="black", width=5, height=1)

        # pack buttons in window
        self.btn_temp.pack(side=TOP, padx=(30,30), pady=(40,0))
        self.btn_licht.pack(side=TOP, padx=(30,30), pady=(20,0))
        self.btn_home.pack(side=LEFT, anchor="sw", padx=(30,30), pady=(20,20))

root = Tk()         # make instance of tkinter
gui = Gui(root)
root.mainloop()     # infinite loop to keep gui running
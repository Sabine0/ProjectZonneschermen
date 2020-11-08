from tkinter import *


class Gui:
    def __init__(self, master):
        self.master = master  # The master attribute gives access to the root window (Tk)
        master.title("Dashboard")
        master.geometry("1280x720")

        # make mainframe
        self.mainframe = Frame(root, bg="red")
        self.mainframe.pack(fill="both", expand=True)
        # give mainframe grid layout
        self.mainframe.grid_rowconfigure(0, weight=1)
        self.mainframe.grid_columnconfigure(1, weight=1)

        # make Frames (container) that go into mainframe
        self.right_frame_temperatuur = Frame(self.mainframe, bg="red")
        self.right_frame = Frame(self.mainframe, bg="lightgrey")
        self.left_frame = Frame(self.mainframe, bg="white", width=100)
        self.left_frame.grid(row=0, column=0, sticky="ns")
        self.right_frame_temperatuur.grid(row=0, column=1, sticky="nsew")
        self.right_frame.grid(row=0, column=1, sticky="nsew")

        # make text
        self.makeLeftFrame()

        # make buttons
        self.makeBtns()

    def raiseTemperatuur(self):
        self.right_frame_temperatuur.tkraise()

    def makeBtns(self):
        self.btn_temp = Button(self.left_frame, text="Temperatuur / Licht", fg="black", width=25, height=5)
        self.btn_licht = Button(self.left_frame, text="Rolluik", fg="black", width=25, height=5)
        self.btn_home = Button(self.left_frame, text="Home", fg="black", width=5, height=1,
                               command=self.raiseTemperatuur)

        # pack buttons in window
        self.btn_temp.pack(side=TOP, padx=(30, 30), pady=(10, 0))
        self.btn_licht.pack(side=TOP, padx=(30, 30), pady=(20, 0))
        self.btn_home.pack(side=LEFT, anchor="sw", padx=(30, 30), pady=(20, 20))

    def makeLeftFrame(self):
        self.label_instellingen = Label(self.left_frame, text="Instellingen", bg="white", font=("DejaVu Sans", 20, "bold"))

        # Home label
        self.homebutton = PhotoImage(file="home.gif")
        self.button_home = Button(self.right_frame, image=self.homebutton, bg="lightgrey", command=self.raiseTemperatuur)
        self.button_home.homebutton = self.homebutton


        # pack labels
        self.label_instellingen.pack(side=TOP, padx=(30, 30), pady=(20, 0))
        self.button_home.pack(side=BOTTOM, padx=(950, 30), pady=(20, 20))

root = Tk()  # make instance of tkinter
gui = Gui(root)
root.mainloop()  # infinite loop to keep gui running

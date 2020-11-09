from tkinter import *


# fg="#F2AA4C",bg="#101820",
#old bg #E3F2FD

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
        # right side frames
        self.right_frame = Frame(self.mainframe, bg="white")
        self.right_frame_rolluik = Frame(self.mainframe, bg="white")
        self.right_frame_temperatuur = Frame(self.mainframe, bg="white")
        self.right_frame.grid(row=0, column=1, sticky="nsew")
        self.right_frame_rolluik.grid(row=0, column=1, sticky="nsew")
        self.right_frame_temperatuur.grid(row=0, column=1, sticky="nsew")

        # left side frames
        self.left_frame = Frame(self.mainframe, bg="#101820", width=100)
        self.left_frame.grid(row=0, column=0, sticky="ns")




        # make frames
        self.makeRolluikFrame()
        self.makeLeftFrame()
        self.makeRightHomeFrame()
        self.makeRightTemperatuurFrame()
        self.raiseHome()

    def raiseTemperatuur(self):
        self.right_frame_temperatuur.tkraise()

    def raiseHome(self):
        self.right_frame.tkraise()

    def raiseRolluikFrame(self):
        self.right_frame_rolluik.tkraise()

    def makeLeftFrame(self):
        # Buttons
        self.btn_temp = Button(self.left_frame, text="Temperatuur / Licht", fg="#101820", width=25, height=5, command=self.raiseTemperatuur)
        self.btn_rolluik = Button(self.left_frame, text="Rolluik", fg="black", width=25, height=5,command=self.raiseRolluikFrame)
        self.btn_test = Button(self.left_frame, text=".", fg="black", width=1, height=1)

        # labels
        self.label_instellingen = Label(self.left_frame, text="Instellingen", fg="#F2AA4C", bg="#101820", relief=FLAT,font=("DejaVu Sans", 20, "bold"))
        self.label_instellingen = Label(self.left_frame, text="Instellingen", fg="#F2AA4C", bg="#101820", relief=FLAT,font=("DejaVu Sans", 20, "bold"))

        # packs
        self.label_instellingen.pack(side=TOP, padx=(30, 30), pady=(20, 0))
        self.btn_temp.pack(side=TOP, padx=(30, 30), pady=(10, 0))
        self.btn_rolluik.pack(side=TOP, padx=(30, 30), pady=(20, 0))
        self.btn_test.pack(side=TOP, padx=(30, 30), pady=(1000, 0))

    def makeRightHomeFrame(self):
        # testlabel
        self.label_homepage = Label(self.right_frame, text="Homepage", fg="black", bg="white", font=("DejaVu Sans", 40, "bold"))

        # packs
        self.label_homepage.pack(side=TOP, padx=(30, 30), pady=(20, 0))

    def makeRightTemperatuurFrame(self):
        # Homebutton
        self.homebutton = PhotoImage(file="home.gif")
        self.button_home = Button(self.right_frame_temperatuur, image=self.homebutton, bg="white",anchor="e", command=self.raiseHome)
        self.button_home.homebutton = self.homebutton

        # Label
        self.label_temp = Label(self.right_frame_temperatuur, text="Instellingen Temperatuur", fg="black",anchor='w', bg="white", font=("DejaVu Sans", 20, "bold"))

        # Packs
        self.label_temp.pack(side=TOP, padx=(30, 30), pady=(20, 0), fill='both')
        self.button_home.pack(side=BOTTOM, padx=(950, 30), pady=(20, 20))

    def makeRolluikFrame(self):
        self.label_rolluik = Label(self.right_frame_rolluik, text="Instellingen Rolluik", fg="black", anchor='w', bg="white", font=("DejaVu Sans", 20, "bold"))

        # Homebutton
        self.homebutton = PhotoImage(file="home.gif")
        self.button_home = Button(self.right_frame_rolluik, image=self.homebutton, bg="white",anchor="e", command=self.raiseHome)
        self.button_home.homebutton = self.homebutton

        #packs
        self.label_rolluik.pack(side=TOP, padx=(30, 30), pady=(20, 0), fill='both')
        self.button_home.pack(side=BOTTOM, padx=(950, 30), pady=(20, 20))







root = Tk()  # make instance of tkinter
gui = Gui(root)
root.mainloop()  # infinite loop to keep gui running

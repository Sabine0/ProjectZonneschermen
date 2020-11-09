from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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
        self.left_frame_buttons = Frame(self.mainframe, bg="#101820", width=100)
        self.left_frame_buttons.grid(row=0, column=0, sticky="ns")
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

    def raiseButtons(self):
        self.left_frame_buttons.tkraise()

    def raiseHome(self):
        self.right_frame.tkraise()

    def raiseRolluikFrame(self):
        self.right_frame_rolluik.tkraise()

    def makeLeftFrame(self):
        # Buttons
        self.btn_temp = Button(self.left_frame, text="Temperatuur / Licht", fg="#101820", width=25, height=5, command=self.raiseTemperatuur)
        self.btn_rolluik = Button(self.left_frame, text="Rolluik", fg="black", width=25, height=5,command=self.raiseRolluikFrame)
        self.btn_uitrollen = Button(self.left_frame, text="Uitrollen", fg="black", width=10, height=2)
        self.btn_inrollen = Button(self.left_frame, text="Inrollen", fg="black", width=10, height=2)

        # labels
        self.label_instellingen = Label(self.left_frame, text="Instellingen", fg="#F2AA4C", bg="#101820",font=("DejaVu Sans", 20, "bold"))
        self.label_handmatig = Label(self.left_frame, text="Handmatig", fg="#F2AA4C", bg="#101820",font=("DejaVu Sans", 20, "bold"))

        # packs
        self.label_instellingen.pack(side=TOP, padx=(30, 30), pady=(20, 0))
        self.btn_temp.pack(side=TOP, padx=(30, 30), pady=(10, 0))
        self.btn_rolluik.pack(side=TOP, padx=(30, 30), pady=(20, 0))
        self.label_handmatig.pack(side=TOP, padx=(30, 30), pady=(100, 100))
        self.btn_uitrollen.place(x=30,y=420)
        self.btn_inrollen.place(x=140, y=420)

    def makeRightHomeFrame(self):
        # Matplotlib grafiek temperatuur
        x = [1,2,3,4,5,6]
        y = [100,101,75,90,104,105]
        figure2 = plt.Figure(figsize=(5, 4), dpi=100)
        ax2 = figure2.add_subplot(111)
        ax2.plot(x,y)
        ax2.set_ylabel("Temperatuur in C°")
        ax2.set_xlabel("Verlopen tijd in seconden")
        line2 = FigureCanvasTkAgg(figure2, self.right_frame)

        # Matplotlib grafiek licht
        x1 = [400,500,600,700,800,900]
        y1 = [0.5,0.6,0.8,0.9,1,1.1]
        figure1 = plt.Figure(figsize=(5, 4), dpi=100)
        ax1 = figure1.add_subplot(111)
        ax1.plot(x1,y1)
        ax1.set_ylabel("Lichtinval in lumen")
        ax1.set_xlabel("Verlopen tijd in seconden")
        line1 = FigureCanvasTkAgg(figure1, self.right_frame)

        # labels
        self.label_homepage = Label(self.right_frame, text="Visualisatie van temperatuursensor", fg="black", bg="white", anchor='w', font=("DejaVu Sans", 20, "bold"))


        # Dropdown voor grafiek
        self.grafiekvariable = StringVar(self.master)
        self.grafiekvariable.set("Temperatuur")  # default value

        self.grafiek = OptionMenu(self.right_frame, self.grafiekvariable,"Temperatuur","Licht")
        self.grafiek["menu"].config(bg="white",relief="raised")
        self.grafiek.config(bg="white",relief="raised")

        # packs
        self.label_homepage.pack(side=TOP, padx=(30, 30), pady=(20, 0),fill='both')
        line2.get_tk_widget().pack(side=TOP, fill=BOTH,padx=(30, 30), pady=(20, 0))
        self.grafiek.place(x=600, y=25)

    def makeRightTemperatuurFrame(self):
        # Homebutton
        self.homebutton = PhotoImage(file="home.gif")
        self.button_home = Button(self.right_frame_temperatuur, image=self.homebutton,relief="flat", bg="white",anchor="e", command=self.raiseHome)
        self.button_home.homebutton = self.homebutton

        # Label
        self.label_temp = Label(self.right_frame_temperatuur, text="Instellingen Temperatuur", fg="black",anchor='w', bg="white", font=("DejaVu Sans", 20, "bold"))
        self.label_licht = Label(self.right_frame_temperatuur, text="Instellingen Licht", fg="black", anchor='w',bg="white", font=("DejaVu Sans", 20, "bold"))
        self.label_tempondergrens = Label(self.right_frame_temperatuur, text="Ondergrens (C°):", fg="black", anchor='w', bg="white")
        self.label_tempbovengrens = Label(self.right_frame_temperatuur, text="Bovengrens (C°):", fg="black", anchor='w', bg="white")
        self.label_lichtondergrens = Label(self.right_frame_temperatuur, text="Ondergrens:", fg="black", anchor='w',bg="white")
        self.label_lichtbovengrens = Label(self.right_frame_temperatuur, text="Bovengrens:", fg="black", anchor='w',bg="white")

        # dropdown menu voor temperatuur
        self.ondergrenstempvariable = StringVar(self.master)
        self.ondergrenstempvariable.set(3)  # default value

        self.ondergrenstemp = OptionMenu(self.right_frame_temperatuur, self.ondergrenstempvariable,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,)
        self.ondergrenstemp["menu"].config(bg="white",relief="raised")
        self.ondergrenstemp.config(bg="white",relief="raised")

        self.bovengrenstempvariable = StringVar(self.master)
        self.bovengrenstempvariable.set(20)  # default value

        self.bovengrenstemp = OptionMenu(self.right_frame_temperatuur, self.bovengrenstempvariable, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, )
        self.bovengrenstemp["menu"].config(bg="white", relief="raised")
        self.bovengrenstemp.config(bg="white", relief="raised")

        # dropdown menu voor licht
        self.ondergrenslichtvariable = StringVar(self.master)
        self.ondergrenslichtvariable.set(3)  # default value

        self.ondergrenslicht = OptionMenu(self.right_frame_temperatuur, self.ondergrenslichtvariable,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,)
        self.ondergrenslicht["menu"].config(bg="white",relief="raised")
        self.ondergrenslicht.config(bg="white",relief="raised")

        self.bovengrenslichtvariable = StringVar(self.master)
        self.bovengrenslichtvariable.set(20)  # default value

        self.bovengrenslicht = OptionMenu(self.right_frame_temperatuur, self.bovengrenslichtvariable, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, )
        self.bovengrenslicht["menu"].config(bg="white", relief="raised")
        self.bovengrenslicht.config(bg="white", relief="raised")


        # Packs
        self.label_temp.pack(side=TOP, padx=(30, 30), pady=(20, 0), fill='both')
        self.button_home.pack(side=BOTTOM, padx=(950, 30), pady=(20, 20))
        self.label_tempondergrens.pack(side=TOP, padx=(30, 30), pady=(20, 20),fill='both')
        self.ondergrenstemp.place(x=150, y=75)
        self.bovengrenstemp.place(x=150, y=135)
        self.label_tempbovengrens.pack(side=TOP, padx=(30, 30), pady=(20, 20), fill='both')
        self.label_licht.pack(side=TOP, padx=(30, 30), pady=(20, 0), fill='both')
        self.label_lichtondergrens.pack(side=TOP, padx=(30, 30), pady=(20, 20), fill='both')
        self.label_lichtbovengrens.pack(side=TOP, padx=(30, 30), pady=(20, 20), fill='both')
        self.ondergrenslicht.place(x=150, y=255)
        self.bovengrenslicht.place(x=150, y=315)

    def makeRolluikFrame(self):
        # labels
        self.label_rolluik = Label(self.right_frame_rolluik, text="Instellingen Rolluik", fg="black", anchor='w',
                                   bg="white", font=("DejaVu Sans", 20, "bold"))
        self.label_rolluikondergrens = Label(self.right_frame_rolluik, text="Minimale uitrol (m):", fg="black",
                                             anchor='w', bg="white")
        self.label_rolluikbovengrens = Label(self.right_frame_rolluik, text="Maximale uitrol (m):", fg="black",
                                             anchor='w', bg="white")
        # Homebutton
        self.homebutton = PhotoImage(file="home.gif")
        self.button_home = Button(self.right_frame_rolluik, image=self.homebutton,relief="flat", bg="white",anchor="e", command=self.raiseHome)
        self.button_home.homebutton = self.homebutton

        # dropdown menu voor rolluik
        self.ondergrensrolluikvariable = StringVar(self.master)
        self.ondergrensrolluikvariable.set(0.05)  # default value

        self.ondergrensrolluik = OptionMenu(self.right_frame_rolluik, self.ondergrensrolluikvariable,0.05,0.10)
        self.ondergrensrolluik["menu"].config(bg="white",relief="raised")
        self.ondergrensrolluik.config(bg="white",relief="raised")

        self.bovengrensrolluikvariable = StringVar(self.master)
        self.bovengrensrolluikvariable.set(1.65)  # default value

        self.bovengrensrolluik = OptionMenu(self.right_frame_rolluik, self.bovengrensrolluikvariable, 1.65,1.60)
        self.bovengrensrolluik["menu"].config(bg="white", relief="raised")
        self.bovengrensrolluik.config(bg="white", relief="raised")

        # packs
        self.label_rolluik.pack(side=TOP, padx=(30, 30), pady=(20, 0), fill='both')
        self.button_home.pack(side=BOTTOM, padx=(950, 30), pady=(20, 20))
        self.label_rolluikondergrens.pack(side=TOP, padx=(30, 30), pady=(20, 20), fill='both')
        self.label_rolluikbovengrens.pack(side=TOP, padx=(30, 30), pady=(20, 20), fill='both')
        self.ondergrensrolluik.place(x=150, y=75)
        self.bovengrensrolluik.place(x=150, y=135)






root = Tk()  # make instance of tkinter
gui = Gui(root)
root.mainloop()  # infinite loop to keep gui running

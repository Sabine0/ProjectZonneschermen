from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# fg="#F2AA4C",bg="#101820",
# old bg #E3F2FD

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
        self.btn_rolluik = Button(self.left_frame, text="Rolluik", fg="black", width=25, height=5, command=self.raiseRolluikFrame)
        self.btn_uitrollen = Button(self.left_frame, text="Uitrollen", fg="black", width=10, height=2)
        self.btn_inrollen = Button(self.left_frame, text="Inrollen", fg="black", width=10, height=2)

        # labels
        self.label_instellingen = Label(self.left_frame, text="Instellingen", fg="#F2AA4C", bg="#101820", font=("DejaVu Sans", 20, "bold"))
        self.label_handmatig = Label(self.left_frame, text="Handmatig", fg="#F2AA4C", bg="#101820", font=("DejaVu Sans", 20, "bold"))

        # packs
        self.label_instellingen.pack(side=TOP, padx=(30, 30), pady=(20, 0))
        self.btn_temp.pack(side=TOP, padx=(30, 30), pady=(10, 0))
        self.btn_rolluik.pack(side=TOP, padx=(30, 30), pady=(20, 0))
        self.label_handmatig.pack(side=TOP, padx=(30, 30), pady=(100, 100))
        self.btn_uitrollen.place(x=30, y=420)
        self.btn_inrollen.place(x=140, y=420)

    def makeRightHomeFrame(self):
        # Matplotlib grafiek temperatuur
        self.x = ["10:00", "11:00", "12:00", "13:00", "14:00", "15:00"]
        self.y = [21, 20, 21, 19, 23, 22]
        self.figure2 = plt.Figure(figsize=(5, 4), dpi=100)
        self.ax2 = self.figure2.add_subplot(111)
        self.ax2.plot(self.x, self.y)
        self.ax2.set_ylabel("Temperatuur in C°")
        self.ax2.set_xlabel("Verlopen tijd in uren")
        self.line2 = FigureCanvasTkAgg(self.figure2, self.right_frame)

        # Matplotlib grafiek licht
        self.x1 = [400, 500, 600, 700, 800, 900]
        self.y1 = [0.5, 0.6, 0.8, 0.9, 1, 1.1]
        self.figure1 = plt.Figure(figsize=(5, 4), dpi=100)
        self.ax1 = self.figure1.add_subplot(111)
        self.ax1.plot(self.x1, self.y1)
        self.ax1.set_ylabel("Lichtinval in lumen")
        self.ax1.set_xlabel("Verlopen tijd in seconden")
        self.line1 = FigureCanvasTkAgg(self.figure1, self.right_frame)
        # labels
        self.label_homepage = Label(self.right_frame, text="Visualisatie van temperatuur en lichtsensor", fg="black", bg="white", anchor='w', font=("DejaVu Sans", 20, "bold"))

        # # Dropdown voor grafiek
        self.comboGrafiek = ttk.Combobox(self.right_frame, values=["Temperatuur", "Licht"], state="readonly", width=13)
        self.comboGrafiek.current(0)
        self.comboGrafiek.bind('<<ComboboxSelected>>', self.changeHomeGrafiek)

        # packs
        self.label_homepage.pack(side=TOP, padx=(30, 30), pady=(20, 0), fill='both')
        self.line2.get_tk_widget().pack(side=TOP, fill=BOTH, padx=(30, 30), pady=(20, 0))
        self.comboGrafiek.place(x=700, y=30)

    def changeHomeGrafiek(self, another_parameter):
        if self.comboGrafiek.get() == "Licht":
            self.line2.get_tk_widget().pack_forget()
            self.line1.get_tk_widget().pack(side=TOP, fill=BOTH, padx=(30, 30), pady=(20, 0))
        if self.comboGrafiek.get() == "Temperatuur":
            self.line1.get_tk_widget().pack_forget()
            self.line2.get_tk_widget().pack(side=TOP, fill=BOTH, padx=(30, 30), pady=(20, 0))

    def callbackFunc(event):
        print("New Element Selected")

    def makeRightTemperatuurFrame(self):
        # Homebutton
        self.homebutton = PhotoImage(file="home.gif")
        self.button_home = Button(self.right_frame_temperatuur, image=self.homebutton, relief="flat", bg="white", anchor="e", command=self.raiseHome)
        self.button_home.homebutton = self.homebutton

        # Label
        self.label_temp = Label(self.right_frame_temperatuur, text="Instellingen Temperatuur", fg="black", anchor='w', bg="white", font=("DejaVu Sans", 20, "bold"))
        self.label_licht = Label(self.right_frame_temperatuur, text="Instellingen Licht", fg="black", anchor='w', bg="white", font=("DejaVu Sans", 20, "bold"))
        self.label_tempondergrens = Label(self.right_frame_temperatuur, text="Ondergrens (C°):", fg="black", anchor='w', bg="white")
        self.label_tempbovengrens = Label(self.right_frame_temperatuur, text="Bovengrens (C°):", fg="black", anchor='w', bg="white")
        self.label_lichtondergrens = Label(self.right_frame_temperatuur, text="Ondergrens:", fg="black", anchor='w', bg="white")
        self.label_lichtbovengrens = Label(self.right_frame_temperatuur, text="Bovengrens:", fg="black", anchor='w', bg="white")

        # dropdown menu voor temperatuur
        self.ondergrenstemp = ttk.Combobox(self.right_frame_temperatuur, state="readonly", width=4, height=50,
                                           values=[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ])
        self.ondergrenstemp.current(0)

        self.bovengrenstemp = ttk.Combobox(self.right_frame_temperatuur, state="readonly", width=4, height=50,
                                           values=[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ])
        self.bovengrenstemp.current(17)

        # dropdown menu voor licht
        self.ondergrenslicht = ttk.Combobox(self.right_frame_temperatuur, state="readonly", width=4, height=50,
                                            values=[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ])
        self.ondergrenslicht.current(0)

        self.bovengrenslicht = ttk.Combobox(self.right_frame_temperatuur, state="readonly", width=4, height=50,
                                            values=[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ])
        self.bovengrenslicht.current(17)

        # Packs
        self.label_temp.pack(side=TOP, padx=(30, 30), pady=(20, 0), fill='both')
        self.button_home.pack(side=BOTTOM, padx=(950, 30), pady=(20, 20))
        self.label_tempondergrens.pack(side=TOP, padx=(30, 30), pady=(20, 20), fill='both')
        self.ondergrenstemp.place(x=150, y=80)
        self.bovengrenstemp.place(x=150, y=140)
        self.label_tempbovengrens.pack(side=TOP, padx=(30, 30), pady=(20, 20), fill='both')
        self.label_licht.pack(side=TOP, padx=(30, 30), pady=(20, 0), fill='both')
        self.label_lichtondergrens.pack(side=TOP, padx=(30, 30), pady=(20, 20), fill='both')
        self.label_lichtbovengrens.pack(side=TOP, padx=(30, 30), pady=(20, 20), fill='both')
        self.ondergrenslicht.place(x=150, y=260)
        self.bovengrenslicht.place(x=150, y=320)

    def makeRolluikFrame(self):
        # labels
        self.label_rolluik = Label(self.right_frame_rolluik, text="Instellingen Rolluik", fg="black", anchor='w', bg="white", font=("DejaVu Sans", 20, "bold"))
        self.label_rolluikondergrens = Label(self.right_frame_rolluik, text="Minimale uitrol (m):", fg="black", anchor='w', bg="white")
        self.label_rolluikbovengrens = Label(self.right_frame_rolluik, text="Maximale uitrol (m):", fg="black", anchor='w', bg="white")
        # Homebutton
        self.homebutton = PhotoImage(file="home.gif")
        self.button_home = Button(self.right_frame_rolluik, image=self.homebutton, relief="flat", bg="white", anchor="e", command=self.raiseHome)
        self.button_home.homebutton = self.homebutton

        # dropdown menu voor rolluik
        self.ondergrensrolluik = ttk.Combobox(self.right_frame_rolluik, state="readonly", width=10, height=50,
                                              values=[0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6,
                                                      0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0, 1.05, 1.1, 1.15, 1.2,
                                                      1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.60])
        self.ondergrensrolluik.current(0)
        self.bovengrensrolluik = ttk.Combobox(self.right_frame_rolluik, state="readonly", width=10, height=50,
                                              values=[0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65,
                                                      0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0, 1.05, 1.1, 1.15, 1.2, 1.25,
                                                      1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.60])
        self.bovengrensrolluik.current(30)

        # packs
        self.label_rolluik.pack(side=TOP, padx=(30, 30), pady=(20, 0), fill='both')
        self.button_home.pack(side=BOTTOM, padx=(950, 30), pady=(20, 20))
        self.label_rolluikondergrens.pack(side=TOP, padx=(30, 30), pady=(20, 20), fill='both')
        self.label_rolluikbovengrens.pack(side=TOP, padx=(30, 30), pady=(20, 20), fill='both')
        self.ondergrensrolluik.place(x=150, y=80)
        self.bovengrensrolluik.place(x=150, y=140)


root = Tk()  # make instance of tkinter
gui = Gui(root)
root.mainloop()  # infinite loop to keep gui running

# import time
import tkinter as tk
import subprocess
from datetime import datetime
from tkinter import messagebox, ttk, font, PhotoImage
import os


class Tastatur(tk.Tk):

    # Tastatur test Taste gedrückt
    def key_pressed(self, event):
        self.keyp = event.keycode
        print(event.keycode)
        if int(self.keyp) == 0:
            self.tasteex = True
        for x, a in enumerate(self.lCodes):
            if a == self.keyp:
                self.labels[x].config(bg="red")
                self.labelLastKey.config(fg="green")
                self.labelLastKey.config(text="Letzte Taste: " + self.lindex[x])
                if self.keyp == 36:
                    self.labelEnter.config(bg="red")

    # Tastatur test Taste wieder losgelassen
    def key_released(self, event):
        self.keyp = event.keycode
        for x, a in enumerate(self.lCodes):
            if a == self.keyp:
                self.labels[x].config(bg="green")
                self.labelLastKey.config(fg="white")
                self.labelLastKey.config(text="Letzte Taste: " + self.lindex[x])
                if self.keyp == 36:
                    self.labelEnter.config(bg="green")

        if self.tabtaste:
            self.labels[37].config(bg="green")
        if self.tasteex:
            self.labels[16].config(bg="green")

            

    # Tastatur Tab Taste wieder losgelassen
    def key_tab(self, event):
        self.keyp = event.keycode
        x = 37
        self.labels[x].config(bg="red")
        self.labelLastKey.config(fg="white")
        self.labelLastKey.config(text="Letzte Taste: " + self.lindex[x])
        self.tabtaste = True


    # Tastatur Tab Taste wieder losgelassen
    def key_tab_release(self, event):
        self.keyp = event.keycode
        x = 37
        self.labels[x].config(bg="green")
        self.labelLastKey.config(fg="white")
        self.labelLastKey.config(text="Letzte Taste: " + self.lindex[x])




# >>>>> Hauptprogramm  <<<<<<<
    def __init__(self):
        super().__init__()

        # region variablen
        # Daten einlesen Variablen
        self.lastevent = ""
        self.toolname = "TastaturTest Linux"
        # region keyboard variablen
        self.tasteex = False
        self.tabtaste = False
        self.keyp = 0
        self.did = 0
        self.loop = "true"
        self.labels = []
        self.lindex = []
        self.lCodes = []
        self.color1 = "black"
        self.color2 = "white"
        self.color4 = "#ffffff"
        self.color3 = "yellow"
        self.keycode1 = [9, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 95, 96, 107, 78, 127]
        self.keyLine1 = ["Esc", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12", "Druck",
                         "Rollen", "Pause"]
        self.keycode2 = [0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 118, 110, 112, 77, 106, 63, 82]
        self.keyLine2 = ["^", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "ß", "´", "<-", "Einfg", "Pos1",
                         "Bild↑",
                         "Num", "/", "*", "-"]
        self.keycode3 = [255, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 119, 115, 117, 79, 80, 81]
        self.keyLine3 = ["|<->|", "Q", "W", "E", "R", "T", "Z", "U", "I", "O", "P", "Ü", "*", "Enter", "Entf",
                         "Ende", "Bild↓", "7", "8", "9"]
        self.keycode4 = [66, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 51, 83, 84, 85]
        self.keyLine4 = ["Sh.Lock", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Ö", "Ä", "#", "4", "5", "6"]
        self.keycode5 = [50, 94, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 111, 87, 88, 89]
        self.keyLine5 = ["Shift", "<", "Y", "X", "C", "V", "B", "N", "M", ";", ":", "-", "Shift", "↑", "1", "2", "3"]
        self.keycode6 = [37, 133, 64, 65, 108, 134, 135, 105, 113, 116, 114, 90, 91]
        self.keyLine6 = ["Strg", "Logo", "Alt", "LEER", "Alt Gr", "Logo", "Menü", "Strg", "←", "↓", "→", "0", ","]
        self.keycode7 = [86, 104]
        self.keyLine7 = ["+", "Enter"]
        # endregion keyboard variablen

        # endregion

        # configure the root window
        self.color3 = "#005800"   # "#0808a8"
        self.color4 = "#003100"   # "#282868"
        self.defaultFont = font.nametofont("TkDefaultFont")
        self.defaultFont.configure(family="Inter",size=8,weight=font.BOLD)
        self.fensterwidth = "994"
        self.fensterheight = "210"
        self.fensterposx = str(int((int(self.winfo_screenwidth()) - int(self.fensterwidth)) / 2)-120)
        self.fensterposy = str(int(int(self.winfo_screenheight()) - int(self.fensterheight)-100))
        self.geometry(self.fensterwidth + "x" + self.fensterheight + "+" + self.fensterposx + "+" + self.fensterposy)
        self.resizable(0, 0)
        self.title(self.toolname)
        self.iconphoto(True, PhotoImage(file="/home/user/tools/images/logo.png"))
        # region Tastatur erstellen
        # Frames definieren
        self.frame_bg = tk.Frame(height=220, width=1300, bg=self.color3)
        self.frame_bg1 = tk.Frame(height=190, width=983, bg=self.color4)
        self.frame_a = tk.Frame(height=270, width=250, bg=self.color4)
        self.frame_b = tk.Frame(height=270, width=250, bg=self.color4)
        self.frame_c = tk.Frame(height=270, width=250, bg=self.color4)
        self.frame_d = tk.Frame(height=270, width=250, bg=self.color4)
        self.frame_e = tk.Frame(height=270, width=250, bg=self.color4)
        self.frame_f = tk.Frame(height=270, width=250, bg=self.color4)
        self.frame_g = tk.Frame(height=270, width=50, bg=self.color4)


        # Keycodes einlesen
        for code in self.keycode1:
            self.lCodes.append(code)
        for code in self.keycode2:
            self.lCodes.append(code)
        for code in self.keycode3:
            self.lCodes.append(code)
        for code in self.keycode4:
            self.lCodes.append(code)
        for code in self.keycode5:
            self.lCodes.append(code)
        for code in self.keycode6:
            self.lCodes.append(code)
        for code in self.keycode7:
            self.lCodes.append(code)


        # FTasten Reihe
        for name in self.keyLine1:
            if name == "F12" or name == "Esc" or name == "F4" or name == "F8":
                self.labelKey = tk.Label(master=self.frame_a, text=name, fg=self.color2, bg=self.color1, width=5)
                self.labelKey.pack(padx=(4, 12), side="left")
            elif name == "Druck":
                self.labelKey = tk.Label(master=self.frame_a, text=name, fg=self.color2, bg=self.color1, width=5)
                self.labelKey.pack(padx=(12, 4), side="left")
            else:
                self.labelKey = tk.Label(master=self.frame_a, text=name, fg=self.color2, bg=self.color1, width=5)
                self.labelKey.pack(padx=4, side="left")
            self.labels.append(self.labelKey)
            self.lindex.append(name)

        # Reihe 1 mit zahlen
        for name in self.keyLine2:
            if name == "<-":
                self.labelKey = tk.Label(master=self.frame_b, text=name, fg=self.color2, bg=self.color1, width=10)
                self.labelKey.pack(padx=(2, 18), side="left")
            elif name == "Einfg" or name == "Pos1" or name == "Bild↑":
                self.labelKey = tk.Label(master=self.frame_b, text=name, fg=self.color2, bg=self.color1, width=5)
                self.labelKey.pack(padx=4, side="left")
            elif name == "Num":
                self.labelKey = tk.Label(master=self.frame_b, text=name, fg=self.color2, bg=self.color1, width=5)
                self.labelKey.pack(padx=(7, 2), side="left")
            elif name == "-":
                self.labelKey = tk.Label(master=self.frame_b, text=name, fg=self.color2, bg=self.color1, width=5)
                self.labelKey.pack(padx=3, side="left")
            else:
                self.labelKey = tk.Label(master=self.frame_b, text=name, fg=self.color2, bg=self.color1, width=5)
                self.labelKey.pack(padx=2, side="left", )
            self.labels.append(self.labelKey)
            self.lindex.append(name)

        # Reihe 2 mit qwertz
        for name in self.keyLine3:
            if name == "Enter":
                self.labelKey = tk.Label(master=self.frame_c, text=name, fg=self.color2, bg=self.color1, width=7)
                self.labelKey.pack(padx=(2, 15), side="left")
            elif name == "Entf" or name == "Ende" or name == "Bild↓":
                self.labelKey = tk.Label(master=self.frame_c, text=name, fg=self.color2, bg=self.color1, width=5)
                self.labelKey.pack(padx=4, side="left")
            elif name == "7":
                self.labelKey = tk.Label(master=self.frame_c, text=name, fg=self.color2, bg=self.color1, width=5)
                self.labelKey.pack(padx=(7, 2), side="left")
            elif name == "|<->|":
                self.labelKey = tk.Label(master=self.frame_c, text=name, fg=self.color2, bg=self.color1, width=8)
                self.labelKey.pack(padx=(3, 4), side="left")
            else:
                self.labelKey = tk.Label(master=self.frame_c, text=name, fg=self.color2, bg=self.color1, width=5)
                self.labelKey.pack(padx=2, side="left", )
            self.labels.append(self.labelKey)
            self.lindex.append(name)

        # Reihe 3 mit asd
        for name in self.keyLine4:
            if name == "#":
                self.labelKey = tk.Label(master=self.frame_d, text=name, fg=self.color2, bg=self.color1, width=5)
                self.labelKey.pack(padx=(2, 204), side="left")
            elif name == "Sh.Lock":
                self.labelKey = tk.Label(master=self.frame_d, text=name, fg=self.color2, bg=self.color1, width=10)
                self.labelKey.pack(padx=(3, 4), side="left")
            else:
                self.labelKey = tk.Label(master=self.frame_d, text=name, fg=self.color2, bg=self.color1, width=5)
                self.labelKey.pack(padx=2, side="left", )
            self.labels.append(self.labelKey)
            self.lindex.append(name)

        # Reihe 4 mit shift <yxc
        for name in self.keyLine5:
            if name == "↑":
                self.labelKey = tk.Label(master=self.frame_e, text=name, fg=self.color2, bg=self.color1, width=5)
                self.labelKey.pack(padx=(68, 57), side="left")
            elif name == "Shift":
                self.labelKey = tk.Label(master=self.frame_e, text=name, fg=self.color2, bg=self.color1, width=10)
                self.labelKey.pack(padx=(3, 4), side="left")
            else:
                self.labelKey = tk.Label(master=self.frame_e, text=name, fg=self.color2, bg=self.color1, width=5)
                self.labelKey.pack(padx=2, side="left", )
            self.labels.append(self.labelKey)
            self.lindex.append(name)

        # Reihe 5 mit Strg logo alt und leer
        for name in self.keyLine6:
            if name == "LEER":
                self.labelKey = tk.Label(master=self.frame_f, text=name, fg=self.color2, bg=self.color1, width=35)
                self.labelKey.pack(padx=4, side="left")
            elif name == "0":
                self.labelKey = tk.Label(master=self.frame_f, text=name, fg=self.color2, bg=self.color1, width=11)
                self.labelKey.pack(padx=(12, 5), side="left")
            elif name == "←":
                self.labelKey = tk.Label(master=self.frame_f, text=name, fg=self.color2, bg=self.color1, width=5)
                self.labelKey.pack(padx=(13, 2), side="left")
            elif name == "Strg":
                self.labelKey = tk.Label(master=self.frame_f, text=name, fg=self.color2, bg=self.color1, width=11)
                self.labelKey.pack(padx=(3, 4), side="left")
            else:
                self.labelKey = tk.Label(master=self.frame_f, text=name, fg=self.color2, bg=self.color1, width=5)
                self.labelKey.pack(padx=2, side="left", )
            self.labels.append(self.labelKey)
            self.lindex.append(name)

        # extratasten num + und enter
        for name in self.keyLine7:
            self.labelKey = tk.Label(master=self.frame_g, text=name, fg=self.color2, bg=self.color1, width=5, height=3)
            self.labelKey.pack(pady=8, side="top", )
            self.labels.append(self.labelKey)
            self.lindex.append(name)
        self.labelEnter = tk.Label(text="", width=4, height=2, fg=self.color2, bg=self.color1)
        self.labelEnter.place(x=611, y=96)
        self.labelLastKey = tk.Label(text="Letzte Taste:", width=24, fg=self.color2, bg=self.color1)
        self.labelLastKey.place(x=808, y=10)
        # endregion Tastatur erstellen

        # Frames platzieren
        self.frame_bg.place(x=0, y=0)
        self.frame_bg1.place(x=5, y=5)
        self.frame_a.place(x=5, y=10)
        self.frame_b.place(x=5, y=50)
        self.frame_c.place(x=5, y=80)
        self.frame_d.place(x=5, y=110)
        self.frame_e.place(x=5, y=140)
        self.frame_f.place(x=5, y=170)
        self.frame_g.place(x=936, y=72)

        self.bind("<Key>", self.key_pressed)
        self.bind("<KeyRelease>", self.key_released)
        self.bind("<F10>", self.key_pressed)
        self.bind("<Tab>", self.key_tab)
        self.bind("<Control-Key-q>", self.destroy)

        self.label1 = tk.Label(text="", width=340, height=1, bg=self.color3, font="Courier 4")
        self.label1.place(x=0, y=33)

        self.lcolor1 = "#0FCCEE"
        self.lcolor2 = "#2BF918"
        self.lcolorhl = "#D04141"
        self.lcolorbg = "#181818"
        self.font = "Courier 14 bold"



if __name__ == "__main__":
    app = Tastatur()
    app.mainloop()

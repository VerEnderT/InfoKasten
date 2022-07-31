import subprocess
import tkinter
import tkinter as tk
from tkinter import font
# import os
# from PIL import ImageTk, Image  # python3 -m pip install pillow


class SystemInfo(tk.Tk):

    @staticmethod
    def com(cmd):
        command = cmd.split(" ")
        complete = subprocess.run(command, capture_output=True)
        ergebnis = str(complete.stdout)  # .split("\\n")
        return ergebnis

    def comm(self,cmd,eintrag):
        ergebnis = []
        command = cmd.split(" ")
        complete = subprocess.run(command, capture_output=True)
        ergebnis = str(complete.stdout).split("\\n")
        ergebnisse = []
        for x in ergebnis:
            if x.find(eintrag)>-1:
                ergebnisse.append(self.reduce(x.split(":")[1]))
        return ergebnisse


    @staticmethod
    def reduce(xin):
        while xin[0] == " ":
            xin = xin[1:]
        return xin

    def xfind(self, array, suche):
        kom = array.split("\n")
        for x in kom:
            if x.find(suche)>-1:
                ergebnis = x.split(":")[1]
                return ergebnis
        return " N/A "

    def daten_einlesen(self):
        self.sysdatenholen()
        self.abfragesystem()
        self.abfragecpu()
        self.abfrageram()
        self.abfragenetwork()
        self.abfragedisplay()
        self.abfragedisk()

    def sysdatenholen(self):
        cmd = "sudo lshw"
        command = cmd.split(" ")
        complete = subprocess.run(command, capture_output=True)
        ergebnis = str(complete.stdout).replace("\\n", "\n")

        #System
        p1 = ergebnis.find("*")
        self.infosystem = ergebnis[:p1]

        #CPU
        p1 = ergebnis.find("*-cpu")
        p2 = ergebnis[p1+1:].find("*-")
        self.infocpu = ergebnis[p1:p1+p2]

        #Ram
        check=False
        p0=0
        p1=0
        p2=0
        self.infomemory = []
        while not check:
            p1 = ergebnis[p0:].find("*-bank")
            if p1 >= 0:
                p2 = ergebnis[p0+p1+1:].find("*")
                if p2 >= 0:
                    self.infomemory.append(self.reduce(ergebnis[p0+p1+1:p0+p1+p2+1]))
                    p0 = p0 + p1 + p2 + 1
                else:
                    self.infomemory.append(self.reduce(ergebnis[p0+p1:]))
                    check=True
            else:
                check=True
                if len(self.infomemory) == 0:
                    self.infomemory = [" N/A "]

        #Netzwerk
        p1 = ergebnis.find("*-network")
        p2 = ergebnis[p1+1:].find("*-")
        self.infonetwork = ergebnis[p1:p1+p2]
        if p2 == -1:
            self.infonetwork = ergebnis[p1:]

        #Festplatten
        p0=0
        p1=0
        p2=0
        dtext = ""
        self.infodisk = []
        check=False
        while not check:
            p1 = ergebnis[p0:].find("*-disk")
            if p1 > 0:
                p2 = ergebnis[p0+p1+1:].find("*")
                if p2 >= 0:
                    dtext = ergebnis[p0+p1+1:p0+p1+p2+1]
                    if dtext.find("removable")==-1:
                        self.infodisk.append(ergebnis[p0+p1+1:p0+p1+p2+1])
                    p0 = p0 + p1 + p2 + 1
                else:
                    dtext=ergebnis[p0+p1:]
                    if dtext.find("removable")==-1:
                        self.infodisk.append(ergebnis[p0+p1:])
                    check=True
            else:
                check=True
                if len(self.infodisk) == 0:
                    self.infodisk = [" N/A "]


        # Grafik
        p1 = ergebnis.find("*-display")
        p2 = ergebnis[p1+1:].find("*-")
        self.infodisplay = ergebnis[p1:p1+p2]


    def abfragesystem(self):
        self.ltext1 = ""
        self.ltext2 = ""
        kom = self.infosystem
        print(self.xfind(kom,"Hersteller"))
        self.ltext1 = self.ltext1 + "Hersteller"
        self.ltext2 = self.ltext2 + self.xfind(kom,"Hersteller")
        self.ltext1 = self.ltext1 + "\nProdukt"
        self.ltext2 = self.ltext2 + "\n" + self.xfind(kom,"Produkt")
        self.ltext1 = self.ltext1 + "\nSeriennummer\n\n"
        self.ltext2 = self.ltext2 + "\n" + self.xfind(kom,"Seriennummer") + "\n\n"
        self.labelhw2.config(text = self.ltext1)
        self.labelhw3.config(text = self.ltext2)

    def abfragecpu(self):
        self.ltext1 = ""
        self.ltext2 = ""
        kom = self.infocpu.replace("\\xc3\\xb6\\xc3\\x9f","oess")
        self.ltext1 = self.ltext1 + "Hersteller"
        self.ltext2 = self.ltext2 + self.xfind(kom,"Hersteller")
        self.ltext1 = self.ltext1 + "\nModel"
        self.ltext2 = self.ltext2 + "\n" + self.xfind(kom,"Produkt")
        self.ltext1 = self.ltext1 + "\nTyp\n\n"
        self.ltext2 = self.ltext2 + "\n" + self.xfind(kom,"Breite")[:-1] + "\n\n"
        self.labelhw5.config(text = self.ltext1)
        self.labelhw6.config(text = self.ltext2)


    def abfrageram(self):
        self.ltext1 = ""
        self.ltext2 = ""
        komms = self.infomemory
        for kom in komms:
            kom = kom.replace("\\xc3\\xb6\\xc3\\x9f","oess")
            self.ltext1 = self.ltext1 + "Steckplatz"
            self.ltext2 = self.ltext2 + self.xfind(kom,"Steckplatz")
            self.ltext1 = self.ltext1 + "\nTyp"
            self.ltext2 = self.ltext2 + "\n" + self.xfind(kom,"Beschreibung")
            self.ltext1 = self.ltext1 + "\nGröße\n\n"
            self.ltext2 = self.ltext2 + "\n" + self.xfind(kom,"Groesse") + "\n\n"
        self.labelhw8.config(text = self.ltext1)
        self.labelhw9.config(text = self.ltext2)


    def abfragenetwork(self):
        self.ltext1 = ""
        self.ltext2 = ""
        kom = self.infonetwork
        self.ltext1 = self.ltext1 + "Hersteller"
        self.ltext2 = self.ltext2 + self.xfind(kom,"Hersteller") + "\n"
        self.ltext1 = self.ltext1 + "\nModel"
        self.ltext2 = self.ltext2 + self.xfind(kom,"Produkt") + "\n"
        self.ltext1 = self.ltext1 + "\nSpeed\n\n"
        self.ltext2 = self.ltext2 + self.xfind(kom,"Kapazit") + "\n\n"
        self.labelhw11.config(text = self.ltext1)
        self.labelhw12.config(text = self.ltext2)

    def abfragedisk(self):
        self.ltext1 = ""
        self.ltext2 = ""
        komms = self.infodisk
        for kom in komms:
            kom = kom.replace("\\xc3\\xb6\\xc3\\x9f","oess")
            # print(kom)
            self.ltext1 = self.ltext1 + "Hersteller"
            self.ltext2 = self.ltext2 + self.xfind(kom,"Hersteller")
            self.ltext1 = self.ltext1 + "\nProdukt"
            self.ltext2 = self.ltext2 + "\n" + self.xfind(kom,"Produkt")
            self.ltext1 = self.ltext1 + "\nGröße\n\n"
            self.ltext2 = self.ltext2 + "\n" + self.xfind(kom,"Groesse") + "\n\n"
        self.labelhw17.config(text = self.ltext1)
        self.labelhw18.config(text = self.ltext2)


    def abfragedisplay(self):
        self.ltext1 = ""
        self.ltext2 = ""
        kom = self.infodisplay
        self.ltext1 = self.ltext1 + "Model"
        self.ltext2 = self.ltext2 + self.xfind(kom,"Produkt")
        self.ltext1 = self.ltext1 + "\nHersteller"
        self.ltext2 = self.ltext2 + "\n" + self.xfind(kom,"Hersteller")
        self.ltext1 = self.ltext1 + "\nAuflösung"
        self.ltext2 = self.ltext2 + "\n " + str(self.winfo_screenwidth())+" x " + str(self.winfo_screenheight())

        self.labelhw14.config(text = self.ltext1)
        self.labelhw15.config(text = self.ltext2)



    # Hauptprogramm initialisierung
    def __init__(self):
        super().__init__()

        self.x = []
        self.ltext = ""
        self.ltext0 = []
        self.ltext1 = ""
        self.ltext2 = ""
        # fenster konifurieren
        self.title("SystemInfo")
        self.fensterwidth = "840"
        self.fensterheight = "500"
        self.fensterposx = str(int((int(self.winfo_screenwidth()) - int(self.fensterwidth)) / 2))
        self.fensterposy = "34"
        self.geometry(self.fensterwidth + "x" + self.fensterheight + "+" + self.fensterposx + "+" + self.fensterposy)
        self.resizable(0, 1)
        # Standart schrift
        self.H1font="Courier 18 bold"
        self.defaultFont = font.nametofont("TkDefaultFont")
        self.defaultFont.configure(family="Inter",size=9,weight=font.BOLD)
        self.config(background="black")
        # Buttons
        self.lastevent = ""

        # Create a photoimage object of the image in the path

        # Position image



        self.colorbg="black"
        self.colorhw1="#a00000"
        self.colorhw2="#18d6ba"
        self.colorhw3="#0aa32b"

        #System
        self.labelhw1 = tk.Label(text="System",fg=self.colorhw1, bg=self.colorbg, font=self.H1font)
        self.labelhw1.place(y=10,x=20)
        self.labelhw2 = tk.Label(text="", fg=self.colorhw2, bg=self.colorbg, justify=tk.LEFT)
        self.labelhw2.place(y=40,x=20)
        self.labelhw3 = tk.Label(text="", fg=self.colorhw3, bg=self.colorbg, justify=tk.LEFT)
        self.labelhw3.place(y=40,x=120)

        # CPU
        self.labelhw4 = tk.Label(text="Prozessor",fg=self.colorhw1, bg=self.colorbg, font=self.H1font)
        self.labelhw4.place(y=110,x=20)
        self.labelhw5 = tk.Label(text="", fg=self.colorhw2, bg=self.colorbg, justify=tk.LEFT)
        self.labelhw5.place(y=140,x=20)
        self.labelhw6 = tk.Label(text="", fg=self.colorhw3, bg=self.colorbg, justify=tk.LEFT)
        self.labelhw6.place(y=140,x=120)


        # Ram
        self.labelhw7 = tk.Label(text="Arbeitsspeicher",fg=self.colorhw1, bg=self.colorbg, font=self.H1font)
        self.labelhw7.place(y=210,x=20)
        self.labelhw8 = tk.Label(text="", fg=self.colorhw2, bg=self.colorbg, justify=tk.LEFT)
        self.labelhw8.place(y=240,x=20)
        self.labelhw9 = tk.Label(text="", fg=self.colorhw3, bg=self.colorbg, justify=tk.LEFT)
        self.labelhw9.place(y=240,x=120)


        # Netzwerk
        self.labelhw10 = tk.Label(text="Netzwerk",fg=self.colorhw1, bg=self.colorbg, font=self.H1font)
        self.labelhw10.place(y=10,x=420)
        self.labelhw11 = tk.Label(text="", fg=self.colorhw2, bg=self.colorbg, justify=tk.LEFT)
        self.labelhw11.place(y=40,x=420)
        self.labelhw12 = tk.Label(text="", fg=self.colorhw3, bg=self.colorbg, justify=tk.LEFT)
        self.labelhw12.place(y=40,x=520)


        # Grafik
        self.labelhw13 = tk.Label(text="Grafik",fg=self.colorhw1, bg=self.colorbg, font=self.H1font)
        self.labelhw13.place(y=110,x=420)
        self.labelhw14 = tk.Label(text="", fg=self.colorhw2, bg=self.colorbg, justify=tk.LEFT)
        self.labelhw14.place(y=140,x=420)
        self.labelhw15 = tk.Label(text="", fg=self.colorhw3, bg=self.colorbg, justify=tk.LEFT)
        self.labelhw15.place(y=140,x=520)


        # Festplatte
        self.labelhw16 = tk.Label(text="Festplatten",fg=self.colorhw1, bg=self.colorbg, font=self.H1font)
        self.labelhw16.place(y=210,x=420)
        self.labelhw17 = tk.Label(text="", fg=self.colorhw2, bg=self.colorbg, justify=tk.LEFT)
        self.labelhw17.place(y=240,x=420)
        self.labelhw18 = tk.Label(text="", fg=self.colorhw3, bg=self.colorbg, justify=tk.LEFT)
        self.labelhw18.place(y=240,x=520)



        self.daten_einlesen()
        #print(self.infocpu)
        print(self.infodisk)
        #print(self.infomemory)
        #print(self.infonetwork)
        #print(self.infosystem)
        #print(self.infodisplay)



if __name__ == "__main__":
    app = SystemInfo()
    app.mainloop()


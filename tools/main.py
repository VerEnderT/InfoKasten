import sys
import os
import libnfs # sudo apt install libnfs-dev && sudo pip3 install libnfs
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtCore import *
import subprocess

 

class Fenster(QWidget):


    # Daten speichern
    def save(self):

        # region Datei öffnen
        dateiname = "/home/user/tools/atk"
        datei = open(dateiname, 'w')
        # endregion


        # region Prozessor
        datei.write(self.cpuModel + "\n")
        # endregion Prozessor

        # region Arbeitsspeicher
        datei.write(str(self.ramGesamt) + "\n")
        datei.write(str(self.ramSlot) + "\n")
        datei.write(str(self.ramTyp) + "\n")
        datei.write(str(self.ramSize) + "\n")
        # endregion Arbeitsspeicher
        
        # region Grafik
        datei.write(self.gpuHersteller + "\n")
        datei.write(self.gpuModel + "\n")
        datei.write(self.gpuDisplay + "\n")
        # endregion Grafik

        # region Festplatten
        datei.write(str(self.diskHersteller) + "\n")
        datei.write(str(self.diskProdukt) + "\n")
        datei.write(str(self.diskSize) + "\n")
        # endregion Festplatten


        datei.close()


        self.doneMsg=QMessageBox.information(self,"","{ color: white }Die Datei " + str(self.sysSerial) + ".csv\nwurde gespeichert !")
            



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

    @staticmethod
    def revreduce(xin):
        while xin[-1:] == " ":
            xin = xin[:-1]
        return xin

    def xfind(self, array, suche):
        kom = array.split("\n")
        for x in kom:
            if x.find(suche)>-1:
                ergebnis = self.revreduce(self.reduce(x.split(":")[1]))
                return ergebnis
        return " N/A "

    def xfindmac(self, array, suche):
        kom = array.split("\n")
        for x in kom:
            if x.find(suche)>-1:
                pos1=x.find(":")
                ergebnis = self.revreduce(self.reduce(x[pos1 + 1:]))
                return ergebnis
        return " N/A "

    def daten_einlesen(self):
        self.sysdatenholen()
        self.abfragesystem()
        self.abfragecpu()
        self.abfrageram()
        self.abfragebattery()
        self.abfragenetwork()
        self.abfragedisplay()
        self.abfragedisk()



    def sysdatenholen(self): 
        cmd = "sudo brightnessctl s 100% -q"
        command = cmd.split(" ")
        cmd1 = subprocess.Popen(['echo',self.passwd], stdout=subprocess.PIPE)
        cmd2 = subprocess.run(['sudo','-S'] + command, stdin=cmd1.stdout, stdout=subprocess.PIPE)
        cmd = "lshw"
        command = cmd.split(" ")
        cmd1 = subprocess.Popen(['echo',self.passwd], stdout=subprocess.PIPE)
        cmd2 = subprocess.run(['sudo','-S'] + command, stdin=cmd1.stdout, stdout=subprocess.PIPE)
        output = cmd2.stdout
        ergebnis = str(output).replace("\\n", "\n")
        self.ergebnis = ergebnis

        #System
        p1 = ergebnis.find("*")
        self.infosystem = ergebnis[:p1]

        #CPU
        p1 = ergebnis.find("*-cpu")
        p2 = ergebnis[p1+1:].find("*-")
        self.infocpu = ergebnis[p1:p1+p2]

        #memory
        p1 = ergebnis.find("*-memory")
        p2 = ergebnis[p1+1:].find("*-")
        self.infomemoryfull = ergebnis[p1:p1+p2]

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
        check=False
        p0=0
        p1=0
        p2=0
        self.infonetwork = []
        while not check:
            p1 = ergebnis[p0:].find("*-network")
            if p1 >= 0:
                p2 = ergebnis[p0+p1+1:].find("*")
                if p2 >= 0:
                    self.infonetwork.append(self.reduce(ergebnis[p0+p1+1:p0+p1+p2+1]))
                    p0 = p0 + p1 + p2 + 1
                else:
                    self.infonetwork.append(self.reduce(ergebnis[p0+p1:]))
                    check=True
            else:
                check=True
                if len(self.infonetwork) == 0:
                    self.infonetwork = [" N/A "]

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

        # Batterie
        self.batterie = self.com("acpi -i")
        self.acadapter = self.com("acpi -a")

    def abfragesystem(self):
        self.ltext1 = ""
        self.ltext2 = ""
        kom = self.infosystem

        self.ltext1 = self.ltext1 + "Hersteller"
        self.sysHersteller = self.xfind(kom,"vendor")
        self.ltext2 = self.ltext2 + self.sysHersteller

        self.sysProdukt = self.xfind(kom,"product")
        self.ltext1 = self.ltext1 + "\nProdukt"
        self.ltext2 = self.ltext2 + "\n" + self.sysProdukt

        self.ltext1 = self.ltext1 + "\nSeriennr.\n"
        self.sysSerial = self.xfind(kom,"serial")
        self.ltext2 = self.ltext2 + "\n" + self.sysSerial + "\n"
        self.label11.setText(self.ltext1[:-1])
        self.label12.setText(self.ltext2[:-1])

    def abfragecpu(self):
        self.ltext1 = ""
        self.ltext2 = ""
        kom = self.infocpu
        self.ltext1 = self.ltext1 + "Hersteller"
        self.cpuHersteller = self.xfind(kom,"vendor")
        self.ltext2 = self.ltext2 + self.cpuHersteller

        self.ltext1 = self.ltext1 + "\nModel"
        self.cpuModel = self.xfind(kom,"product")
        self.ltext2 = self.ltext2 + "\n" + self.cpuModel

        self.ltext1 = self.ltext1 + "\nTyp\n"
        self.cpuTyp = self.xfind(kom,"width")[:-1]
        self.ltext2 = self.ltext2 + "\n" + self.cpuTyp +"\n"

        self.label21.setText(self.ltext1[:-1])
        self.label22.setText(self.ltext2[:-1])

    def abfrageram(self):
        self.ltext1 = ""
        self.ltext2 = ""
        self.ramGesamt = ""
        self.ramSlot = []
        self.ramTyp = []
        kom = self.infomemoryfull
        self.ltext1 = self.ltext1 + "Gesamt\n\n"
        self.ramGesamt = self.xfind(kom,"size") 
        self.ltext2 = self.ltext2 + self.ramGesamt + "\n\n"
        komms = self.infomemory
        for kom in komms:
            self.ltext1 = self.ltext1 + "Slot"
            self.ramSlot.append(self.xfind(kom,"slot"))
            self.ltext2 = self.ltext2 + self.xfind(kom,"slot")

            self.ltext1 = self.ltext1 + "\nTyp"
            self.ramTyp.append(self.xfind(kom,"description"))
            self.ltext2 = self.ltext2 + "\n" + self.xfind(kom,"description")   
   
            self.ltext1 = self.ltext1 + "\nGröße\n\n"
            self.ramSize.append(self.xfind(kom,"size"))
            self.ltext2 = self.ltext2 + "\n" + self.xfind(kom,"size") + "\n\n"
        self.label31.setText(self.ltext1[:-2])
        self.label32.setText(self.ltext2[:-2])

    def abfragebattery(self):
        self.ltext1 = ""
        self.ltext2 = ""
        if self.acadapter[2:].find(":")>=0:
            self.ltext1 = self.ltext1 + self.acadapter[2:].split(":")[0]+"\n"
            self.batAdapter = self.reduce(self.acadapter.split(":")[1].replace("\\n", "")[:-1])
            self.ltext2 = self.ltext2 + self.reduce(self.acadapter.split(":")[1].replace("\\n", "")[:-1])+"\n"
        x = self.batterie[2:].split("\\n")
        self.batBat = []
        self.batNr = []        
        for a in x:
            if a.find(":")>=0:
                self.batNr.append(self.reduce(a.split(":")[0]))
                self.ltext1 = self.ltext1 + self.reduce(a.split(":")[0])+"\n"  
                self.batBat.append(self.ltext2 + self.reduce(a.split(":")[1]))
                self.ltext2 = self.ltext2 + self.reduce(a.split(":")[1])+"\n"
        self.label41.setText(self.ltext1)
        self.label42.setText(self.ltext2)

    def abfragenetwork(self):
        self.ltext1 = ""
        self.ltext2 = ""
        komms = self.infonetwork
        self.netHersteller = []
        self.netModel = []
        self.netSpeed = []

        for kom in komms:
            self.ltext1 = self.ltext1 + "Hersteller"
            self.netHersteller.append(self.xfind(kom,"vendor"))
            self.ltext2 = self.ltext2 + self.xfind(kom,"vendor") + "\n"

            self.ltext1 = self.ltext1 + "\nModel"
            self.netModel.append(self.xfind(kom,"product"))
            self.ltext2 = self.ltext2 + self.xfind(kom,"product") + "\n"

            self.ltext1 = self.ltext1 + "\nMAC:"
            self.netMac.append(self.xfindmac(kom,"serial"))
            self.ltext2 = self.ltext2 + self.xfindmac(kom,"serial") + "\n"

            self.ltext1 = self.ltext1 + "\nSpeed\n\n"
            self.netSpeed.append(self.xfind(kom,"capacity"))
            self.ltext2 = self.ltext2 + self.xfind(kom,"capacity") + "\n\n"

        self.label51.setText(self.ltext1[:-2])
        self.label52.setText(self.ltext2[:-2])

    def abfragedisplay(self):
        self.ltext1 = ""
        self.ltext2 = ""
        kom = self.infodisplay
        self.ltext1 = self.ltext1 + "Model"
        self.gpuModel = self.xfind(kom,"product")
        self.ltext2 = self.ltext2 + self.gpuModel

        self.ltext1 = self.ltext1 + "\nHersteller"
        self.gpuHersteller = self.xfind(kom,"vendor")
        self.ltext2 = self.ltext2 + "\n" + self.gpuHersteller

        self.ltext1 = self.ltext1 + "\nAuflösung\n"
        self.gpuDisplay = self.reduce(str(app.desktop().width())+" x " + str(app.desktop().height()))
        self.ltext2 = self.ltext2 + "\n " + self.gpuDisplay +"\n"
        self.label61.setText(self.ltext1[:-1])
        self.label62.setText(self.ltext2[:-1])

    def abfragedisk(self):
        self.ltext1 = ""
        self.ltext2 = ""
        komms = self.infodisk

        for kom in komms:
            self.ltext1 = self.ltext1 + "Hersteller"
            self.diskHersteller.append(self.xfind(kom,"vendor"))
            self.ltext2 = self.ltext2 + self.xfind(kom,"vendor")

            self.ltext1 = self.ltext1 + "\nProdukt"
            self.diskProdukt.append(self.xfind(kom,"product"))
            self.ltext2 = self.ltext2 + "\n" + self.xfind(kom,"product")

            self.ltext1 = self.ltext1 + "\nSeriennr."
            self.diskSerial.append(self.xfind(kom,"serial"))
            self.ltext2 = self.ltext2 + "\n" + self.xfind(kom,"serial")

            self.ltext1 = self.ltext1 + "\nGröße\n\n"
            self.diskSize.append(self.xfind(kom,"size"))
            self.ltext2 = self.ltext2 + "\n" + self.xfind(kom,"size") + "\n\n"
        self.label71.setText(self.ltext1[:-2])
        self.label72.setText(self.ltext2[:-2])
        

    # Hauptprogramm
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        self.passwd = "user"
        self.path = "/freigabe/"
        self.toolname = "Alien-TestKasten 22.10"

        self.sysHersteller = ""
        self.sysProdukt = ""
        self.sysSerial = ""

        self.cpuHersteller = ""
        self.cpuModel = ""
        self.cpuTyp = ""

        self.ramGesamt = ""
        self.ramSlot = []
        self.ramTyp = []
        self.ramSize = []

        self.batAdapter = ""
        self.batNr = []
        self.batBat = []

        self.netHersteller = []
        self.netModel = []
        self.netSpeed = []
        self.netMac = []

        self.gpuHersteller = ""
        self.gpuModel = ""
        self.gpuDisplay = ""

        self.diskHersteller = []
        self.diskProdukt = []
        self.diskSerial = []
        self.diskSize = []

        breite = 650
        bts=18
        sts=13
        if app.desktop().width()>=1920:
            bts=24
            sts=18
            breite = 850

        x = int(app.desktop().width())/2-int(breite/2)
      
        # Stylesheets 
        ss1= str(
            "background: rgba(0, 200, 0, 150);" +
            "font-size: " + str(bts) + "px;" +
            "color: #00e500;" +
            "border: 2px solid '#f0f0f0';" +
            "border-radius: 10px;" +
            "color: #ffffff;"
            )
        ss2= str(
            "background: rgba(250, 250, 250, 30);" +
            "font-size: " + str(sts) + "px;" +
            "color: #0ff0ff;" 
            "padding-top: 2px;"+
            "padding-bottom: 0px;"
            )
        ss3= str(
            "background: rgba(200, 200,200, 50);" +
            "font-size: " + str(sts) + "px;" +
            "color: #ffff0f;" +
            "padding-top: 2px;"+
            "padding-left: 5px;"+
            "padding-right: 5px;"+
            "padding-bottom: 0px;"
            )
        ssf= str(
            "background: rgba(200, 0, 0, 180);" +
            "font-size: " + str(bts) + "px;" +
            "color: #00e500;" +
            "border: 2px solid '#f0f0f0';" +
            "border-radius: 10px;" +
            "color: #ffffff;"
            )
        ssf2= str(
            "background: rgba(200, 0, 0, 150);" +
            "font-size: " + str(sts) + "px;" +
            "color: #ffff0f;" +
            "padding-top: 2px;"+
            "padding-left: 5px;"+
            "padding-right: 5px;"+
            "padding-bottom: 0px;"
            )

        # self.label definieren
        self.label1 = QLabel("System")
        self.label1.setStyleSheet(ss1)
        self.label11 = QLabel("N/A\nN/A\nN/A")
        self.label11.setStyleSheet(ss2)
        self.label11.setAlignment(Qt.AlignTop)
        self.label12 = QLabel("N/A\nN/A\nN/A")
        self.label12.setStyleSheet(ss3)
        self.label12.setAlignment(Qt.AlignTop)
        self.label2 = QLabel("Prozessor")
        self.label2.setStyleSheet(ss1)
        self.label21 = QLabel("N/A\nN/A\nN/A")
        self.label21.setStyleSheet(ss2)
        self.label21.setAlignment(Qt.AlignTop)
        self.label22 = QLabel("N/A\nN/A\nN/A")
        self.label22.setStyleSheet(ss3)
        self.label22.setAlignment(Qt.AlignTop)
        self.label3 = QLabel("Arbeitsspeicher")
        self.label3.setStyleSheet(ss1)
        self.label31 = QLabel("N/A\nN/A\nN/A")
        self.label31.setStyleSheet(ss2)
        self.label31.setAlignment(Qt.AlignTop)
        self.label32 = QLabel("N/A\nN/A\nN/A")
        self.label32.setStyleSheet(ss3)
        self.label32.setAlignment(Qt.AlignTop)
        self.label4 = QLabel("Batterie")
        self.label4.setStyleSheet(ss1)
        self.label41 = QLabel("N/A\nN/A\nN/A")
        self.label41.setStyleSheet(ss2)
        self.label41.setAlignment(Qt.AlignTop)
        self.label42 = QLabel("N/A\nN/A\nN/A")
        self.label42.setStyleSheet(ss3)
        self.label42.setAlignment(Qt.AlignTop)
        self.label5 = QLabel("Netzwerk")
        self.label5.setStyleSheet(ss1)
        self.label51 = QLabel("N/A\nN/A\nN/A")
        self.label51.setStyleSheet(ss2)
        self.label51.setAlignment(Qt.AlignTop)
        self.label52 = QLabel("N/A\nN/A\nN/A")
        self.label52.setStyleSheet(ss3)
        self.label52.setAlignment(Qt.AlignTop)
        self.label6 = QLabel("Grafik")
        self.label6.setStyleSheet(ss1)
        self.label61 = QLabel("N/A\nN/A\nN/A")
        self.label61.setStyleSheet(ss2)
        self.label61.setAlignment(Qt.AlignTop)
        self.label62 = QLabel("N/A\nN/A\nN/A")
        self.label62.setStyleSheet(ss3)
        self.label62.setAlignment(Qt.AlignTop)
        self.label7 = QLabel("Festplatten")
        self.label7.setStyleSheet(ss1)
        self.label71 = QLabel("N/A\nN/A\nN/A")
        self.label71.setStyleSheet(ss2)
        self.label71.setAlignment(Qt.AlignTop)
        self.label72 = QLabel("N/A\nN/A\nN/A")
        self.label72.setStyleSheet(ss3)
        self.label72.setAlignment(Qt.AlignTop)

        
        self.saveBtn = QPushButton(" Daten als vorlage Speichern ")
        self.saveBtn.setStyleSheet(ss1)
        self.saveBtn.clicked.connect(self.save)
       
        fw = 64
        fh = 28

        if app.desktop().width()>=1920:
            fw=110
            fh=42

        # box 1 horizontal
        hboxlayout1 = QHBoxLayout()
        hboxlayout1.addWidget(self.label11)
        self.label11.setFixedWidth(fw)
        hboxlayout1.addWidget(self.label12)
        # box 1 vertical
        vboxlayout1 = QVBoxLayout()
        vboxlayout1.addWidget(self.label1)
        self.label1.setFixedHeight(fh)
        vboxlayout1.addLayout(hboxlayout1)


        # box 2 horizontal
        hboxlayout2 = QHBoxLayout()
        hboxlayout2.addWidget(self.label21)
        self.label21.setFixedWidth(fw)
        hboxlayout2.addWidget(self.label22)
        # box 2 vertical
        vboxlayout2 = QVBoxLayout()
        vboxlayout2.addWidget(self.label2)
        self.label2.setFixedHeight(fh)
        vboxlayout2.addLayout(hboxlayout2)

        # box 3 horizontal
        hboxlayout3 = QHBoxLayout()
        hboxlayout3.addWidget(self.label31)
        self.label31.setFixedWidth(fw)
        hboxlayout3.addWidget(self.label32)
        # box 3 vertical
        vboxlayout3 = QVBoxLayout()
        vboxlayout3.addWidget(self.label3)
        self.label3.setFixedHeight(fh)
        vboxlayout3.addLayout(hboxlayout3)

        # box 4 horizontal
        hboxlayout4 = QHBoxLayout()
        hboxlayout4.addWidget(self.label41)
        self.label41.setFixedWidth(fw)
        hboxlayout4.addWidget(self.label42)
        # box 4 vertical
        vboxlayout4 = QVBoxLayout()
        vboxlayout4.addWidget(self.label4)
        self.label4.setFixedHeight(fh)
        vboxlayout4.addLayout(hboxlayout4)

        # box 5 horizontal
        hboxlayout5 = QHBoxLayout()
        hboxlayout5.addWidget(self.label51)
        self.label51.setFixedWidth(fw)
        hboxlayout5.addWidget(self.label52)
        # box 5 vertical
        vboxlayout5 = QVBoxLayout()
        vboxlayout5.addWidget(self.label5)
        self.label5.setFixedHeight(fh)
        vboxlayout5.addLayout(hboxlayout5)

        # box 6 horizontal
        hboxlayout6 = QHBoxLayout()
        hboxlayout6.addWidget(self.label61)
        self.label61.setFixedWidth(fw)
        hboxlayout6.addWidget(self.label62)
        # box 6 vertical
        vboxlayout6 = QVBoxLayout()
        vboxlayout6.addWidget(self.label6)
        self.label6.setFixedHeight(fh)
        vboxlayout6.addLayout(hboxlayout6)

        # box 7 horizontal
        hboxlayout7 = QHBoxLayout()
        hboxlayout7.addWidget(self.label71)
        self.label71.setFixedWidth(fw)
        hboxlayout7.addWidget(self.label72)
        # box 7 vertical
        vboxlayout7 = QVBoxLayout()
        vboxlayout7.addWidget(self.label7)
        self.label7.setFixedHeight(fh)
        vboxlayout7.addLayout(hboxlayout7)
        

        # vvbox1
        vvboxlayout1 = QVBoxLayout()
        vvboxlayout1.addLayout(vboxlayout1)
        vvboxlayout1.addLayout(vboxlayout2)
        vvboxlayout1.addLayout(vboxlayout3)
        # vvbox2
        vvboxlayout2 = QVBoxLayout()
        vvboxlayout2.addLayout(vboxlayout5)
        vvboxlayout2.addLayout(vboxlayout6)
        vvboxlayout2.addLayout(vboxlayout7)
        # hhbox
        hhboxlayout = QHBoxLayout()
        hhboxlayout.addLayout(vvboxlayout1)
        hhboxlayout.addLayout(vvboxlayout2)
        # vvvbox
        vvvboxlayout = QVBoxLayout()
        vvvboxlayout.addLayout(hhboxlayout)
        vvvboxlayout.addLayout(vboxlayout4)
        if os.path.isfile('/home/user/atk'):
            print("true")     
            vvvboxlayout.addWidget(self.saveBtn)
        else:
            print("false")

        # Fenster anzeigen
        self.setLayout(vvvboxlayout)
        self.setGeometry(int(x), 80, breite, 30)
        self.setWindowTitle("System-Informationen")
        self.setWindowIcon(QIcon("/home/user/tools/images/logo.png"))
        self.setStyleSheet(
            "background: rgba(0, 0, 0, 0);" 
            )

        self.daten_einlesen()
        width = self.frameGeometry().width()
        height = self.frameGeometry().height()
        # self.setGeometry(0 , 0 ,app.desktop().width(),app.desktop().height())
        # Randloses Fenster
        #flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        #flags = QtCore.Qt.WindowFlags(QtCore.Qt.WindowShadeButtonHint)
        #flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnBottomHint | Qt.X11BypassWindowManagerHint)
        #self.setWindowFlags(flags)



        if os.path.isfile('/home/user/tools/atk'):
            vvvboxlayout.addWidget(self.saveBtn)
            dateiname = '/home/user/tools/atk'
            datei = open(dateiname, 'r')
            x = datei.read()
            q = x.split("\n")
            if len(q)>=10:
                if q[0] != self.cpuModel:
                    self.label2.setStyleSheet(ssf)
                    self.label22.setStyleSheet(ssf2)
                if q[1] != self.ramGesamt or q[2] != str(self.ramSlot) or q[3] != str(self.ramTyp) or q[4] != str(self.ramSize):
                    self.label3.setStyleSheet(ssf)
                    self.label32.setStyleSheet(ssf2) 
                if q[5] != self.gpuHersteller or q[6] != self.gpuModel or q[7] != self.gpuDisplay:
                    self.label6.setStyleSheet(ssf)
                    self.label62.setStyleSheet(ssf2)
                if q[8] != str(self.diskHersteller) or q[9] != str(self.diskProdukt) or q[10] != str(self.diskSize):
                    self.label7.setStyleSheet(ssf)
                    self.label72.setStyleSheet(ssf2)




        self.show()
        
        # System
        #print(self.sysHersteller)
        #print(self.sysProdukt)
        #print(self.sysSerial)

        # CPU
        #print(self.cpuHersteller)
        #print(self.cpuModel)
        #print(self.cpuTyp)

        # Ram
        #print(self.ramGesamt)
        #print(self.ramSlot)
        #print(self.ramTyp)
        #print(self.ramSize)

        # Batterie
        #print(self.batAdapter)
        #print(self.batBat)

        # Netzwerk
        #print(self.netHersteller)
        #print(self.netModel)
        #print(self.netSpeed)

        # Grafik
        #print(self.gpuHersteller)
        #print(self.gpuModel)
        #print(self.gpuDisplay)

        # Disk
        #print(self.diskHersteller)
        #print(self.diskProdukt)
        #print(self.diskSize)

app = QApplication(sys.argv)
w = Fenster()
sys.exit(app.exec())


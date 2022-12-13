from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, \
    QSlider, QStyle, QSizePolicy, QFileDialog, QProgressBar
import sys
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette, QPixmap
from PyQt5.QtCore import Qt, QUrl
import subprocess
import os
import pyaudio
import numpy as np
# für multimedia wiedergabe
# sudo apt install python3-pyqt5.qtmultimedia



class Window(QWidget):

    def aufnahme(self):
        cmd ='arecord -f cd -d 3 -r 16000 /tmp/test-mic.wav'
        os.system(cmd)
        self.playBtn.setEnabled(True)

    def abspielen(self):
        cmd ='aplay /tmp/test-mic.wav'
        os.system(cmd)


    def slider_update(self, position):
        self.slider.setMaximum(40000)
        self.slider.setValue(position)

    def stop(self):
        self.stream.stop_stream()
        self.stream.close()
        self.slider_update(0)
        self.stopBtn.setEnabled(False)
        self.liveBtn.setEnabled(True)

    def callback(self, in_data, frame_count, time_info, status):
        #print(in_data)
        data = np.frombuffer(in_data, dtype=np.int16)
        # print(np.amax(data))
        #_VARS['window']['-PROG-'].update(np.amax(data))
        self.slider_update(np.amax(data))
        return (in_data, pyaudio.paContinue)



    def listen(self):
        self.stopBtn.setEnabled(True)
        self.liveBtn.setEnabled(False)
        self.stream = self.pAud.open(format=pyaudio.paInt16,
                               channels=1,
                               rate=self.RATE,
                               input=True,
                               frames_per_buffer=self.CHUNK,
                               stream_callback=self.callback)

        self.stream.start_stream()

    def __init__(self):
        

        # PyAudio INIT:
        self.CHUNK = 1024  # Samples: 1024,  512, 256, 128
        self.RATE = 44100  # Equivalent to Human Hearing at 40 kHz
        self.INTERVAL = 1  # Sampling Interval in Seconds ie Interval to listen

        self.pAud = pyaudio.PyAudio()


        super().__init__()

        self.setWindowTitle("Microfontest")

        logopm ='/usr/share/xtk/images/tuxmic-64.png'
        logow = 64
        bts = 18
        sts = 13
        xlx = 0
        xly = 0
        
        # änderungen bei hoher auflösung
        if app.desktop().width()>=1920:
            bts = 24
            sts = 22
            logopm = '/usr/share/xtk/images/tuxmic-128.png'
            logow = 128
            xlx = 50 
            xly = 50
        
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
            "font-size: " + str(sts) + "px;"
            )

        sslogo = str("background: rgba(200, 200, 200, 150);" +
            "font-size: 18px;" +
            "color: #00e500;" +
            "border: 2px solid '#f0f0f0';" +
            "border-radius: 10px;" +
            "color: #ffffff;"
            )

        sspegel =  str("QProgressBar {" +
            "font: 1px;" +
            "background-color: #004000;" +
            "border: solid grey;" +
            "max-height: 8px;" +
            "border-radius: 3px;" +
            "color: black; }"+
            "QProgressBar::chunk {"+
            "background-color: #00c800;" +
            "border-radius :15px; }"
            )    



        x = int(app.desktop().width()-350 - xlx)
        y = int(app.desktop().height()-250 - xly)
        
        self.setGeometry(x, y, 250, 50)
        self.setWindowIcon(QIcon('/usr/share/xtk/images/tuxmic.png'))

        p =self.palette()
        p.setColor(QPalette.Window, Qt.black)
        self.setPalette(p)

        #create Picture 
        self.labell = QLabel()
        myPixmap = QPixmap(logopm)
        self.labell.setPixmap(myPixmap)
        self.labell.setScaledContents(False)
        self.labell.setFixedWidth(logow)
        self.labell.setStyleSheet(ss1)

        #create button for stop
        self.stopBtn = QPushButton(" Pegel beenden ")
        self.stopBtn.setStyleSheet(ss2)
        self.stopBtn.setEnabled(False)
        self.stopBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self.stopBtn.clicked.connect(self.stop)

        #create button for live
        self.liveBtn = QPushButton(" Pegel anzeigen ")
        self.liveBtn.setStyleSheet(ss2)
        self.liveBtn.setEnabled(True)
        self.liveBtn.setIcon(QIcon('/usr/share/xtk/images/rec.png'))
        self.liveBtn.clicked.connect(self.listen)

        #create button for wiedergabe
        self.playBtn = QPushButton(" Wiedergabe ")
        self.playBtn.setStyleSheet(ss2)
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.clicked.connect(self.abspielen)

        #create button for Aufnahme
        self.recBtn = QPushButton(" Aufnahme ")
        self.recBtn.setStyleSheet(ss2)
        self.recBtn.setEnabled(True)
        self.recBtn.setIcon(QIcon('/usr/share/xtk/images/rec.png'))
        self.recBtn.clicked.connect(self.aufnahme)

        #create label
        self.label = QLabel()
        self.label.setStyleSheet(ss1)
        self.label.setText("Microfontest")
        self.label.setAlignment(Qt.AlignCenter)


        # Pegel
        self.slider = QProgressBar(self)       
        self.slider.setStyleSheet(sspegel)    

        #create vbox1 layout
        vbox1Layout = QVBoxLayout()
        vbox1Layout.setContentsMargins(0,0,0,0)
        vbox1Layout.addWidget(self.liveBtn)
        vbox1Layout.addWidget(self.slider)
        vbox1Layout.addWidget(self.stopBtn)

        #create hbox1 layout
        hbox1Layout = QHBoxLayout()
        hbox1Layout.addWidget(self.labell, Qt.AlignCenter)
        hbox1Layout.addLayout(vbox1Layout)

        hbox2Layout = QHBoxLayout()
        hbox2Layout.addWidget(self.recBtn, Qt.AlignCenter)
        hbox2Layout.addWidget(self.playBtn, Qt.AlignCenter)

        #create vbox layout
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(self.label)
        vboxLayout.addLayout(hbox1Layout)
        vboxLayout.addLayout(hbox2Layout)

        self.setLayout(vboxLayout)
        self.stopBtn.setEnabled(False)
        self.show()

        

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())

sys.exit(print("beendet"))


from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, \
    QSlider, QStyle, QSizePolicy, QFileDialog
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


    def slider_update(self, position):
        self.slider.setMaximum(40000)
        self.slider.setValue(position)

    def stop(self):
        self.stream.stop_stream()
        self.stream.close()
        self.slider_update(0)
        self.stopBtn.setEnabled(False)
        self.recBtn.setEnabled(True)

    def callback(self, in_data, frame_count, time_info, status):
        #print(in_data)
        data = np.frombuffer(in_data, dtype=np.int16)
        # print(np.amax(data))
        #_VARS['window']['-PROG-'].update(np.amax(data))
        self.slider_update(np.amax(data))
        return (in_data, pyaudio.paContinue)



    def listen(self):
        self.stopBtn.setEnabled(True)
        self.recBtn.setEnabled(False)
        self.stream = self.pAud.open(format=pyaudio.paInt16,
                               channels=1,
                               rate=self.RATE,
                               input=True,
                               frames_per_buffer=self.CHUNK,
                               stream_callback=self.callback)

        self.stream.start_stream()

    def __init__(self):
        

        # PyAudio INIT:
        self.CHUNK = 256  # Samples: 1024,  512, 256, 128
        self.RATE = 44100  # Equivalent to Human Hearing at 40 kHz
        self.INTERVAL = 1  # Sampling Interval in Seconds ie Interval to listen

        self.pAud = pyaudio.PyAudio()


        super().__init__()

        self.setWindowTitle("Microfontest")

        x = int(app.desktop().width()-250)
        y = int(app.desktop().height()-220)
        
        self.setGeometry(x, y, 250, 50)
        self.setWindowIcon(QIcon('/home/user/tools/images/tuxmic.png'))

        p =self.palette()
        p.setColor(QPalette.Window, Qt.black)
        self.setPalette(p)

        #create Picture 320, 240
        self.labell = QLabel()
        myPixmap = QPixmap('/home/user/tools/images/tuxmic-64.png')
        self.labell.setPixmap(myPixmap)
        self.labell.setScaledContents(False)
        self.labell.setFixedWidth(64)
        self.labell.setStyleSheet(
            "background: rgba(200, 200, 200, 150);" +
            "font-size: 18px;" +
            "color: #00e500;" +
            "border: 2px solid '#f0f0f0';" +
            "border-radius: 10px;" +
            "color: #ffffff;"
            )

        #create videowidget object

        videowidget = QVideoWidget()

        #create button for stop
        self.stopBtn = QPushButton(" Stop ")
        #self.stopBtn.setFixedWidth(170)
        self.stopBtn.setEnabled(False)
        self.stopBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self.stopBtn.clicked.connect(self.stop)

        #create button for Aufnahme
        self.recBtn = QPushButton(" LiveTest starten ")
        self.recBtn.setEnabled(True)
        self.recBtn.setIcon(QIcon('/home/user/tools/images/rec.png'))
        self.recBtn.clicked.connect(self.listen)

        #create label
        self.label = QLabel()
        self.label.setStyleSheet(
            "background: rgba(0, 200, 0, 150);" +
            "font-size: 18px;" +
            "color: #00e500;" +
            "border: 2px solid '#f0f0f0';" +
            "border-radius: 10px;" +
            "color: #ffffff;"
            )
        self.label.setText("Microfontest")
        self.label.setAlignment(Qt.AlignCenter)


        self.slider = QSlider(Qt.Horizontal)
        #self.slider.setRange(4000,0)
        #self.slider.sliderMoved.connect(self.set_position)

        #create vbox1 layout
        vbox1Layout = QVBoxLayout()
        vbox1Layout.setContentsMargins(0,0,0,0)
        vbox1Layout.addWidget(self.recBtn)
        vbox1Layout.addWidget(self.slider)
        vbox1Layout.addWidget(self.stopBtn)

        #create hbox1 layout
        hbox1Layout = QHBoxLayout()
        hbox1Layout.addWidget(self.labell, Qt.AlignCenter)
        hbox1Layout.addLayout(vbox1Layout)

        #create vbox layout
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(self.label)
        vboxLayout.addLayout(hbox1Layout)

        self.setLayout(vboxLayout)
        self.stopBtn.setEnabled(False)
        self.show()

        

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())

sys.exit(print("beendet"))


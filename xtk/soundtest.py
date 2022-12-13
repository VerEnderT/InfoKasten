from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, \
    QSlider, QStyle, QSizePolicy, QFileDialog
import sys
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette, QPixmap
from PyQt5.QtCore import Qt, QUrl
# für multimedia wiedergabe
# sudo apt install python3-pyqt5.qtmultimedia



class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Soundtest")

        x = int(app.desktop().width()-380)




        self.setGeometry(x, 100, 250, 150)
        self.setWindowIcon(QIcon('/usr/share/xtk/images/tuxmusik.png'))

        p =self.palette()
        p.setColor(QPalette.Window, Qt.black)
        self.setPalette(p)

        self.init_ui()


        self.show()


    def init_ui(self):

        #create media player object
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)


        #create Picture 320, 240
        self.labell = QLabel()
        myPixmap = QPixmap('/usr/share/xtk/images/tuxmusik.png')
        self.labell.setPixmap(myPixmap)
        self.labell.setScaledContents(False)
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


        #create open button
        openBtn = QPushButton('Open Video')
        openBtn.clicked.connect(self.open_file)



        #create button for playing
        self.playBtn = QPushButton(" Pause")
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        self.playBtn.clicked.connect(self.play_video)



        #create slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,0)
        self.slider.sliderMoved.connect(self.set_position)



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
        self.label.setText("Musik: Kalimba von Mr. Scruff")

        #create hbox layout
        hboxLayout = QHBoxLayout()
        hboxLayout.setContentsMargins(0,0,0,0)

        #set widgets to the hbox layout
        #hboxLayout.addWidget(openBtn)
        hboxLayout.addWidget(self.playBtn)
        hboxLayout.addWidget(self.slider)



        #create vbox layout
        vboxLayout = QVBoxLayout()
        #vboxLayout.addWidget(videowidget)
        vboxLayout.addWidget(self.labell)
        vboxLayout.addWidget(self.label)
        vboxLayout.addLayout(hboxLayout)


        self.setLayout(vboxLayout)
        filename = "/usr/share/xtk/musik/Kalimba.mp3"
        #self.mediaPlayer.setVideoOutput(videowidget)
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
        self.playBtn.setEnabled(True)
        self.mediaPlayer.play()
        #media player signals

        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)


    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")

        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)


    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()

        else:
            self.mediaPlayer.play()


    def mediastate_changed(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause)

            )
            self.playBtn.setText(" Pause")

        else:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay)

            )
            self.playBtn.setText(" Start")

    def position_changed(self, position):
        self.slider.setValue(position)


    def duration_changed(self, duration):
        self.slider.setRange(0, duration)


    def set_position(self, position):
        self.mediaPlayer.setPosition(position)


    def handle_errors(self):
        self.playBtn.setEnabled(False)
        # self.label.setText("Error: " + self.mediaPlayer.errorString())





app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())

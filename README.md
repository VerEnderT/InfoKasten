# InfoKasten
Deutsche Laptop / PC Test Programme und Linux live system

![Screenshot_20220801_004113](https://user-images.githubusercontent.com/53666253/182047044-4e84cf05-3284-470f-bfb6-04562f4dcad4.png)

um sich ein eigenes Linux Live System daraus zu bauen empfehle ich ein auf ubuntu oder debian basierendes Linux zu installieren.
als Benutzer habe ich user mit passwort user verwendet. der auch sudo rechte haben muss. Name und password müssen sonst in start.py 
und menu.py angepasst werden. Am besten auch automatisches einlogen.

wichtig für start.py und menu.py oder muss in den Dateien geändert werden. 
In näherer zukunft wird das noch vereinfachter vielleicht mit config datei.
Benutzer: user
Passwort: user
Verzeichnis /home/user/tools/

wenn system installiert ist sollten so wenig wie möglich an anderen programmen drauf sein,
das mach das image später schlanker und kann startzeiten verbessern.
für die tools benötigte software muss installiert sein:\n

python3 getestet 3.8.10

python3-tk

vlc

cheese


für die installation von Systemback empfehle ich folgende befehle.

Mit Systemback kann man eigene Kopien vom installierten system machen und live cd bzw usb sticks erstellen.


#Systemback installieren

git clone https://github.com/fconidi/systemback-install_pack-1.9.4.git

cd systemback-install_pack-1.9.4

chmod +x install.sh

sudo ./install.sh


TestTools :
tastaturtest.py <-- ist ein programm zum Testen der Tastatur unter linux. nicht mit windows kompatible da die keycodes anders sind.
soundtest <-- startet nur eine test mp3 in einem Vlc player und wird direkt von der menu.py gestartet.
displaytest.py <-- wechselt bei mouse-knopf druck die farbe des kompletten bildschirm um monitore oder laptop displays auf Fehler zu überprüfen.
main.py <-- zeigt informationen des system ab wird von der start.py oder der menu.py mit sudo rechten gestartet
menu.py <-- positioniert unten am bildschirmrand eine leiste mit den Druckknöpfen zu den einzelnen Testprogrammen.
kameratest <-- startet cheese welches als webcam tool unter linux bekannt ist. 

Es wird noch weiter dran gebastelt das ist erstmal der erste Entwurf.



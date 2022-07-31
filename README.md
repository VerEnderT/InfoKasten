# InfoKasten
Deutsche Laptop / PC test tools und Linux live system

![Screenshot_20220801_004113](https://user-images.githubusercontent.com/53666253/182047044-4e84cf05-3284-470f-bfb6-04562f4dcad4.png)

um sich ein eigenes Linux Live System daraus zu bauen empfehle ich ein auf ubuntu oder debian basierendes Linux zu installieren.
als Benutzer habe ich user mit passwort user verwendet. der auch sudo rechte haben muss. Name und password müssen sonst in start.py 
und menu.py angepasst werden. Am besten auch automatisches einlogen.

# wichtig für start.py und menu.py oder muss in den Dateien geändert werden. in näherer zukunft wird das noch vereinfachter vielleicht mit config datei.
benutzer: user
passwort: user
verzeichnis /home/user/tools/

wenn system installiert ist sollten so wenig wie möglich an anderen programmen drauf sein,
das mach das image später schlanker und kann startzeiten verbessern.
für die tools benötigte software muss installiert sein:

python3 getestet 3.8.10
python3-tk
vlc
cheese

für die installation von Systemback empfehle ich folgende befehle.
Mit Systemback kann man eigene Kopien vom installierten system machen und live cd bzw usb sticks erstellen-

#Systemback installieren
git clone https://github.com/fconidi/systemback-install_pack-1.9.4.git
cd systemback-install_pack-1.9.4/
chmod +x install.sh
sudo ./install.sh

import tkinter as tk
import subprocess
import os

class Menu(tk.Tk):

    def cam(self):
        cmd = "cheese".split(" ")
        subprocess.Popen(cmd, shell=False)
    def sound(self):
        cmd ="vlc /home/user/tools/Kalimba.mp3"
        os.system(cmd)
        subprocess.Popen(cmd, shell=False)
    def systeminfo(self):
        command = "sudo python3 /home/user/tools/main.py".split(" ")
        cmd1 = subprocess.Popen(['echo','user'], stdout=subprocess.PIPE)
        cmd2 = subprocess.Popen(['sudo','-S'] + command, stdin=cmd1.stdout, stdout=subprocess.PIPE)
        output = cmd2.stdout.read
    def tastaturtest(self):
        cmd = "python3 /home/user/tools/tastaturtest.py".split(" ")
        subprocess.Popen(cmd, shell=False)
    def displaytest(self):
        cmd = "python3 /home/user/tools/displaytest.py".split(" ")
        subprocess.Popen(cmd, shell=False)
    def beenden(self):
        cmd = "python3 /home/user/tools/beenden.py".split(" ")
        subprocess.Popen(cmd, shell=False)
        self.destroy()




    # Hauptprogramm initialisierung
    def __init__(self):
        super().__init__()
        y = str(self.winfo_screenheight()-34)
        print(y)
        self.attributes('-fullscreen', True)
        self.geometry(str(self.winfo_screenwidth())+"x34+0+"+y)
        self.overrideredirect(True)
        self.config(background="#020202")
        # keybindings
        self.button1 = tk.Button(text="SystemInfo",fg="white",bg="black", command=self.systeminfo)
        self.button1.pack(side="left", expand=True, fill='x')
        self.button1 = tk.Button(text="Tastaturtest",fg="white",bg="black", command=self.tastaturtest)
        self.button1.pack(side="left", expand=True, fill='x')
        self.button1 = tk.Button(text="Displaytest",fg="white",bg="black", command=self.displaytest)
        self.button1.pack(side="left", expand=True, fill='x')
        self.button1 = tk.Button(text="Soundtest",fg="white", bg="black", command=self.sound)
        self.button1.pack(side="left", expand=True, fill='x')
        self.button1 = tk.Button(text="Kameratest",fg="white",bg="black", command=self.cam)
        self.button1.pack(side="left", expand=True, fill='x')
        self.button1 = tk.Button(text="Ausschalten",fg="white",bg="black", command=self.beenden)
        self.button1.pack(side="left", expand=True, fill='x')


if __name__ == "__main__":
    app = Menu()
    app.mainloop()

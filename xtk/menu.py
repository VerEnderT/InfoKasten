import tkinter as tk
import subprocess
import os

class Menu(tk.Tk):

    def sound(self):
        cmd = "pkill -9 -f soundtest.py"
        os.system(cmd)
        cmd = "python3 /home/user/tools/soundtest.py"
        subprocess.Popen(cmd.split(" "), shell=False)
        #cmd = "pkill -9 -f ffplay"
        #os.system(cmd)
        #cmd = "ffplay -x 200 -y 100 -window_title Soundtest -showmode waves /home/user/tools/Kalimba.mp3"
        #subprocess.Popen(cmd.split(" "), shell=False)
    def rec(self):
        cmd = "pkill -9 -f rectest.py"
        os.system(cmd)
        cmd = "python3 /home/user/tools/rectest.py"
        subprocess.Popen(cmd.split(" "), shell=False)
    def mic(self):
        cmd = "pkill -9 -f mictest.py"
        os.system(cmd)
        cmd = "python3 /home/user/tools/mictest.py"
        subprocess.Popen(cmd.split(" "), shell=False)
    def systeminfo(self):
        cmd = "pkill -9 -f main.py"
        os.system(cmd)
        cmd = "python3 /home/user/tools/main.py".split(" ")
        subprocess.Popen(cmd, shell=False)
    def tastaturtest(self):
        cmd = "pkill -9 -f tastaturtest.py"
        os.system(cmd)
        cmd = "python3 /home/user/tools/tastaturtest.py".split(" ")
        subprocess.Popen(cmd, shell=False)
    def cam(self):
        cmd = "pkill -9 -f cam.py"
        os.system(cmd)
        cmd = "python3 /home/user/tools/cam.py".split(" ")
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
        #print(y)
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
        self.button1 = tk.Button(text="Microfontest",fg="white", bg="black", command=self.mic)
        self.button1.pack(side="left", expand=True, fill='x')
        #self.button1 = tk.Button(text="Aufnahmetest",fg="white", bg="black", command=self.rec)
        #self.button1.pack(side="left", expand=True, fill='x')
        self.button1 = tk.Button(text="Kameratest",fg="white",bg="black", command=self.cam)
        self.button1.pack(side="left", expand=True, fill='x')
        self.button1 = tk.Button(text="Ausschalten",fg="white",bg="black", command=self.beenden)
        self.button1.pack(side="left", expand=True, fill='x')


if __name__ == "__main__":
    app = Menu()
    app.mainloop()

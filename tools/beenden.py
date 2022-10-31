import tkinter as tk
import subprocess
import os

class Beenden(tk.Tk):

    def beenden(self):
        cmd = "shutdown now".split(" ")
        subprocess.Popen(cmd, shell=False)
        self.destroy()

    def nein (self):
        cmd = "sh /home/user/tools/start.sh".split(" ")
        subprocess.Popen(cmd, shell=False)
        self.destroy()

    # Hauptprogramm initialisierung
    def __init__(self):
        super().__init__()

        cmd = "pkill -9 -f cheese"
        os.system(cmd)
        cmd = "pkill -9 -f soundtest"
        os.system(cmd)
        cmd = "pkill -9 -f ffplay"
        os.system(cmd)
        cmd = "pkill -9 -f rectest.py"
        os.system(cmd)
        cmd = "pkill -9 -f mictest.py"
        os.system(cmd)
        cmd = "pkill -9 -f main.py"
        os.system(cmd)
        cmd = "pkill -9 -f tastaturtest.py"
        os.system(cmd)

        y = str(self.winfo_screenheight()-234)
        x = str(int(self.winfo_screenwidth()/2-200))
        self.title("Herunterfahren ??")
        self.resizable(0, 0)
        self.geometry(str("400x34+"+x+"+"+y))
        self.config(background="#020202")
        # keybindings
        self.button1 = tk.Button(text="Ja",fg="white",bg="Red", command=self.beenden)
        self.button1.pack(side="left", expand=True, fill='x')
        self.button2 = tk.Button(text="Nein",fg="white",bg="Green", command=self.nein)
        self.button2.pack(side="left", expand=True, fill='x')

if __name__ == "__main__":
    app = Beenden()
    app.mainloop()

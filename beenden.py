import tkinter as tk
import subprocess

class Beenden(tk.Tk):

    def beenden(self):
        cmd = "shutdown now".split(" ")
        self.destroy()
        subprocess.Popen(cmd, shell=False)

    def nein (self):
        self.destroy()

    # Hauptprogramm initialisierung
    def __init__(self):
        super().__init__()

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

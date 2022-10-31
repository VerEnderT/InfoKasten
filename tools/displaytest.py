import tkinter as tk

class Displaytest(tk.Tk):

    def key_pressed(self, event):
        self.color = self.color + 1
        if self.color >= len(self.colors) - 1:
            self.color = 0
        self.config(background=self.colors[self.color])
        self.lastevent = event

    def key_destroy(self, event):
        self.lastevent = event
        self.destroy()

    # Hauptprogramm initialisierung
    def __init__(self):
        super().__init__()
        self.color = 0
        self.colors = ["blue", "yellow", "white", "green", "red", "black", "brown", "pink"]
        self.attributes('-fullscreen', True)
        self.overrideredirect(True)
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.config(background="blue")
        # keybindings
        self.bind("<Key>", self.key_pressed)
        self.bind("<Button>", self.key_pressed)
        self.bind("<Button-3>", self.key_destroy)
        self.bind("<Escape>", self.key_destroy)
        self.lastevent = ""


if __name__ == "__main__":
    app = Displaytest()
    app.mainloop()

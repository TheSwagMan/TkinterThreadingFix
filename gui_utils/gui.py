import tkinter as tk


class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        """
        If you need to put a GUI layout here.
        """
        self.bind("<<close>>", self.close)
        self.protocol("WM_DELETE_WINDOW", self.close)

    def close(self, *args):
        print("ok")
        self.destroy()

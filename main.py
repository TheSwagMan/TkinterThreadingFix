from gui import Gui
from adaptor import GuiAdapter

if __name__ == "__main__":
    # creating Tk
    maingui = Gui()
    # passing Tk to GuiAdapter
    adapter = GuiAdapter(maingui)
    # starting adaptor in another thread
    adapter.start()
    # looping Tk
    maingui.mainloop()

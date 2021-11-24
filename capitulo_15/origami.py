import tkinter as tk
from PIL import ImageTk,Image

class App():
    def __init__(self, toplevel):
        self.img = ImageTk.PhotoImage(Image.open("origami.png"))
        self.panel = tk.Label(toplevel, image = self.img)
        self.panel.pack()

raiz = tk.Tk()
app = App(raiz)
raiz.mainloop()
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image

class App():
    def __init__(self, toplevel):
        self.raiz = toplevel
        self.raiz.title('AquaPython App')
        # define tamanho da janela
        self.raiz.geometry("300x300")
        # impede redimensionar a janela
        self.raiz.resizable(False, False)
        self.create_widgets()

    def caixa_dagua_necessaria(self, volume_necessario):
        """
        Escolha da caixa d'agua adequada
        """
        dimensoes = [300, 500,1000,1500,2000,3000,5000]
        for d in dimensoes:
            if d > volume_necessario:
                return d

    def volume_necessario(self):
        """
        cp = consumo per capita
        n = numero de pessoas
        """
        cp = float(self.consumo_entry.get())
        n = int(self.n_pessoas_entry.get())
        volume =  cp*n*1.2
        caixa = self.caixa_dagua_necessaria(volume)
        "Message box cria uma caixa de aviso"
        messagebox.showinfo("Caixa d'água",f"Consumo diário {volume}L\n Utilizar caixa d'água de {caixa}L")
    def create_widgets(self):
        # Cria os frames
        self.frame1 = tk.Frame(self.raiz)
        self.frame1.pack(fill=tk.BOTH)
        self.frame2 = tk.Frame(self.raiz)
        self.frame2.pack(fill=tk.BOTH, padx=10, pady=5)
        self.frame3 = tk.Frame(self.raiz)
        self.frame3.pack(fill=tk.BOTH, padx=10, pady=5)
        self.frame4 = tk.Frame(self.raiz)
        self.frame4.pack(fill=tk.BOTH, padx=10, pady=5)

        self.img = ImageTk.PhotoImage(Image.open("caixa_3d.png"))
        self.panel = ttk.Label(self.frame1, image = self.img)
        self.panel.pack(side=tk.LEFT)
        
        # Consumo
        self.consumo_label = ttk.Label(self.frame2, text="Consumo per capita (L/dia):")
        self.consumo_label.pack(side=tk.LEFT)
        self.consumo_entry = ttk.Entry(self.frame2, width=11)
        self.consumo_entry.pack(side=tk.RIGHT)

        # Numero de pessoas
        self.n_pessoas_label = ttk.Label(self.frame3, text="Nº de pessoas:")
        self.n_pessoas_label.pack(side=tk.LEFT)
        self.n_pessoas_entry = ttk.Entry(self.frame3, width=11)
        self.n_pessoas_entry.pack(side=tk.RIGHT)

        # login button
        button = ttk.Button(self.frame4, text="Calcular", command=self.volume_necessario)
        button.pack(side=tk.RIGHT)

raiz = tk.Tk()
app = App(raiz)
raiz.mainloop()
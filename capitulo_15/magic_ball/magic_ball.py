import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import random

class App():
    def __init__(self, toplevel):
        self.raiz = toplevel
        self.raiz.title('Bola Mágica 8')
        # define tamanho da janela
        self.raiz.geometry("400x530")
        # impede redimensionar a janela
        self.raiz.resizable(False, False)
        self.create_widgets()

    def sacudir(self):
        # move a imagem criando o efeito de sacudir
        self.raiz.after(300, self.canvas.move, self.image_container, 30, 0)
        self.raiz.after(400, self.canvas.move, self.image_container, -30, 0)
        self.raiz.after(500, self.resposta)

    def resposta(self):
        # gera números aleatórios entre 0 e 5
        guess = random.randint(0, 5)
        self.img = ImageTk.PhotoImage(Image.open(f"{guess}.png"))
        self.canvas.itemconfig(self.image_container,image=self.img)
        
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

        # Cria o widget Canva para inserir a imagem
        # Neste exemplo foi optado pelo Canva em vez do Label
        # para possibilitar o movimento da imagem
        self.canvas = tk.Canvas(self.frame1, width=400, height=400)
        self.canvas.pack(side=tk.LEFT) # this makes it visible
        self.img = ImageTk.PhotoImage(Image.open("intro.png"))
        self.image_container = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)
        
        # Label da pergunta
        self.consumo_label = tk.Label(self.frame2, text="Qual sua pergunta?", font=('Helvetica', 12, 'bold'))
        self.consumo_label.pack(side=tk.TOP)
        # Caixa do texto
        self.consumo_entry = ttk.Entry(self.frame3, width=40, font=('Helvetica', 12, 'bold'))
        self.consumo_entry.pack(side=tk.LEFT)

        # Aparência do botão
        style = ttk.Style()
        style.theme_use('alt')
        style.configure('TButton', background = 'purple', foreground = 'white', height=40, 
                        width = 20, focusthickness=3, focuscolor='none', font=('Helvetica', 12, 'bold'), )
        style.map('TButton', background=[('active','purple')])

        # Botão
        button = ttk.Button(self.frame4, text="Sacudir", command=self.sacudir)
        button.pack(side=tk.TOP)

if __name__ == "__main__":
    raiz = tk.Tk()
    app = App(raiz)
    raiz.mainloop()
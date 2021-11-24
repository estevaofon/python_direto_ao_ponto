import tkinter as tk

class App():
    def __init__(self, toplevel):
        toplevel.geometry("160x110")
        self.frame1 = tk.Frame(toplevel)
        self.frame1.pack(fill="both", padx=10, pady=5)
        self.frame2 = tk.Frame(toplevel)
        self.frame2.pack(fill="both", padx=10, pady=5)
        self.frame3 = tk.Frame(toplevel)
        self.frame3.pack(fill="both", padx=10, pady=5)

        self.label = tk.Label(self.frame1, text="Usuário")
        self.label.pack(side="left") 
        self.usuario = tk.Entry(self.frame1,width=10)
        self.usuario.pack(side="right")
        self.label2 = tk.Label(self.frame2, text="Senha")
        self.label2.pack(side="left")
        self.senha = tk.Entry(self.frame2,width=10, show='*')
        self.senha.pack(side="right")
        self.button = tk.Button(self.frame3, text='Logar',
        command = self.logar)
        self.button.pack(side="right")
        self.label3 = tk.Label(self.frame3, text="")
        self.label3.pack(side="left")

    def logar(self):
        usuario = self.usuario.get()
        senha = self.senha.get()
        if senha == usuario:
            self.label3['text']="Acesso permitido"
        else:
            self.label3['text']="Acesso negado"
        

raiz = tk.Tk()
app = App(raiz)
raiz.mainloop()
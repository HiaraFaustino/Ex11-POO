import tkinter as tk
from tkinter import messagebox
import jogos as jog

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('250x250')
        self.menubar = tk.Menu(self.root)
        self.jogosMenu = tk.Menu(self.menubar)
        self.sairMenu = tk.Menu(self.menubar)

        self.jogosMenu.add_command(label="Cadastrar", \
                command=self.controle.cadastrarJogos)
        self.jogosMenu.add_command(label="Avaliar", \
                command=self.controle.avaliarJogos)
        self.jogosMenu.add_command(label="Consultar", \
                command=self.controle.consultarJogos)
        self.menubar.add_cascade(label="Jogos", \
                menu=self.jogosMenu)
        
        self.sairMenu.add_command(label="Salva", \
                    command=self.controle.salvaDados)
        self.menubar.add_cascade(label="Sair", \
                    menu=self.sairMenu)

        self.root.config(menu=self.menubar)

class ControlePrincipal():
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlJogo = jog.CtrlJogo(self)
        self.limite = LimitePrincipal(self.root, self)
        self.root.title("Jogos")
        self.root.mainloop()

    def cadastrarJogos(self):
        self.ctrlJogo.cadastrarJogos()

    def avaliarJogos(self):
        self.ctrlJogo.avaliarJogos()

    def consultarJogos(self):
        self.ctrlJogo.consultarJogos()

    def salvaDados(self):
        self.ctrlJogo.salvaJogos()
        self.root.destroy()

if __name__ == '__main__':
    c = ControlePrincipal()
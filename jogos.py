import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os.path
import pickle

class Jogo():
    def __init__(self, codigo, titulo, console, genero, preco):
        self.__codigo = codigo
        self.__titulo = titulo
        self.console = console
        self.genero = genero
        self.preco = preco
        self.__avaliacoes = []

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def console(self):
        return self.__console
    
    @console.setter
    def console(self, valor):
        self.consoles = ["Xbox", "PlayStation", "Switch", "PC"]
        if not valor in self.consoles:
            raise ValueError("Console inválido: {}".format(valor))
        else:
            self.__console = valor
    
    @property
    def genero(self):
        return self.__genero
    
    @genero.setter
    def genero(self, valor):
        self.generos = ["Ação", "Aventura", "Estratégia", "RPG", "Esporte", "Simulação"]
        if not valor in self.generos:
            raise ValueError("Gênero inválido: {}".format(valor))
        else:
            self.__genero = valor
    
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, valor):
        if valor < 0 or valor > 500:
            raise ValueError("Valor inválido: {}".format(valor))
        else:
            self.__preco = valor
    
    @property
    def avaliacoes(self):
        return self.__avaliacoes
    
    def addAvaliacao(self, avaliacao):
        self.__avaliacoes.append(avaliacao)
    
class LimiteInsereCadastro(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x180')
        self.title("Cadastro")
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameTitulo = tk.Frame(self)
        self.frameConsole = tk.Frame(self)
        self.frameGenero = tk.Frame(self)
        self.framePreco = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameTitulo.pack()
        self.frameConsole.pack()
        self.frameGenero.pack()
        self.framePreco.pack()
        self.frameButton.pack()

        self.labelCodigo = tk.Label(self.frameCodigo,text="Código: ")
        self.labelTitulo = tk.Label(self.frameTitulo,text="Título: ")
        self.labelConsole = tk.Label(self.frameConsole,text="Console: ")
        self.labelGenero = tk.Label(self.frameGenero,text="Gênero: ")
        self.labelPreco = tk.Label(self.framePreco,text="Preço: ")
        self.labelCodigo.pack(side="left")
        self.labelTitulo.pack(side="left")
        self.labelConsole.pack(side="left")
        self.labelGenero.pack(side="left")
        self.labelPreco.pack(side="left")

        self.inputCodigo = tk.Entry(self.frameCodigo,width=20)
        self.inputCodigo.pack(side="left")
        self.inputTitulo = tk.Entry(self.frameTitulo,width=20)
        self.inputTitulo.pack(side="left")
        self.inputConsole = tk.Entry(self.frameConsole,width=20)
        self.inputConsole.pack(side="left")
        self.inputGenero = tk.Entry(self.frameGenero,width=20)
        self.inputGenero.pack(side="left")
        self.inputPreco = tk.Entry(self.framePreco,width=20)
        self.inputPreco.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)

        self.buttonClear = tk.Button(self.frameButton, text="Clear")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandlerCadastro)

        self.buttonClose = tk.Button(self.frameButton, text="Close")
        self.buttonClose.pack(side="left")
        self.buttonClose.bind("<Button>", controle.closeHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteInsereAvaliacao(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Avaliação")
        self.controle = controle

        self.frameCodigoJogo = tk.Frame(self)
        self.frameEstrelas = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigoJogo.pack()
        self.frameEstrelas.pack()
        self.frameButton.pack()

        self.labelCodigoJogo = tk.Label(self.frameCodigoJogo,text="Código: ")
        self.labelCodigoJogo.pack(side="left")
        self.inputCodigoJogo = tk.Entry(self.frameCodigoJogo,width=20)
        self.inputCodigoJogo.pack(side="left")

        self.labelEstrelas = tk.Label(self.frameEstrelas,text="Número de estrelas: ")
        self.labelEstrelas.pack(side="left")
        self.escolhacombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameEstrelas,width=15,textvariable=self.escolhacombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = ["1 estrela", "2 estrelas", "3 estrelas", "4 estrelas", "5 estrelas"]

        self.buttonInsere = tk.Button(self.frameButton,text="Inserir")
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", lambda event: controle.insereAvaliacao(event))

        self.buttonClose = tk.Button(self.frameButton, text="Close")
        self.buttonClose.pack(side="left")
        self.buttonClose.bind("<Button>", controle.closeHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteInsereConsulta(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x150')
        self.title("Consulta")
        self.controle = controle

        self.frameEstrelas = tk.Frame(self)
        self.frameResultado = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameEstrelas.pack()
        self.frameButton.pack()
        self.frameResultado.pack()

        self.labelEstrelas = tk.Label(self.frameEstrelas,text="Número de estrelas: ")
        self.labelEstrelas.pack(side="left")
        self.escolhacombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameEstrelas,width=15,textvariable=self.escolhacombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = ["1 estrela", "2 estrelas", "3 estrelas", "4 estrelas", "5 estrelas"]
        self.combobox.pack(side="left")

        self.listbox = tk.Listbox(self.frameResultado,height=10,width=30)
        self.listbox.pack()

        self.buttonConsulta = tk.Button(self.frameButton,text="Consultar")
        self.buttonConsulta.pack(side="left")
        self.buttonConsulta.bind("<Button>", lambda event: controle.consultarAvaliacao())

        self.buttonClose = tk.Button(self.frameButton, text="Close")
        self.buttonClose.pack(side="left")
        self.buttonClose.bind("<Button>", controle.closeHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class CtrlJogo():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        if not os.path.isfile("jogos.pickle"):
            self.listaJogos = []
        else:
            with open("jogos.pickle", "rb") as f:
                self.listaJogos = pickle.load(f)

    def salvaJogos(self):
        if len(self.listaJogos) != 0:
            with open("jogos.pickle", "wb") as f:
                pickle.dump(self.listaJogos, f)

    def enterHandler(self, event):#entrar com dados do cadastro
        codigo = self.limite.inputCodigo.get()
        titulo = self.limite.inputTitulo.get()
        console = self.limite.inputConsole.get()
        genero = self.limite.inputGenero.get()
        preco = float(self.limite.inputPreco.get())

        try:
            jogo = Jogo(codigo, titulo, console, genero, preco)
            self.listaJogos.append(jogo)
            self.limite.mostraJanela('Sucesso', 'Jogo cadastrado com sucesso!')
            self.clearHandlerCadastro(event)

        except ValueError as error:#conferir se eles correspondem ao esperado
            self.limite.mostraJanela('Erro', error)

    def clearHandlerCadastro(self, event):
        self.limite.inputCodigo.delete(0, len(self.limite.inputCodigo.get()))
        self.limite.inputTitulo.delete(0, len(self.limite.inputTitulo.get()))
        self.limite.inputConsole.delete(0, len(self.limite.inputConsole.get()))
        self.limite.inputGenero.delete(0, len(self.limite.inputGenero.get()))
        self.limite.inputPreco.delete(0, len(self.limite.inputPreco.get()))
        
    def closeHandler(self, event):
        self.limite.destroy()

    def clearHandlerAvaliacao(self, event):
        self.limite.inputCodigoJogo.delete(0, len(self.limite.inputCodigoJogo.get()))
        self.limite.escolhacombo.set("")

    def insereAvaliacao(self, event):
        codigoJogo = self.limite.inputCodigoJogo.get()#entra com o código
        estrelas = int(self.limite.escolhacombo.get().split()[0])#recebe o nro de estrelas e separa a string
        jogo = self.getJogo(codigoJogo)#obtem o jogo correspondente de acordo com o código
        if jogo:
            jogo.addAvaliacao(int(estrelas))#add a avaliação
            self.limite.mostraJanela('Sucesso', 'Avaliação realizada com sucesso!')
            self.clearHandlerAvaliacao(event)
        else:
            self.limite.mostraJanela('Erro', 'Jogo não encontrado!')

    def getJogo(self, codigo):#serve para pegar o código correspondente
        jogRet = None
        for jogo in self.listaJogos:
            if jogo.codigo == codigo:
                jogRet = jogo
        return jogRet

    def avaliacaoMedia(self, jogo):
        if not jogo.avaliacoes:#se nao tem avaliacoes 
            return 0
        media = sum(jogo.avaliacoes) / len(jogo.avaliacoes)
        #sum soma dos numeros da lista e len numero de elementos da lista
        if 0 <= media <= 1:
            return 1
        elif 1 < media <= 2:
            return 2
        elif 2 < media <= 3:
            return 3
        elif 3 < media <= 4:
            return 4
        elif 4 < media <= 5:
            return 5
        else: 
            return 0

    def consultarAvaliacao(self):
        estrelas = int(self.limite.escolhacombo.get().split()[0])#obtem a quant de estrelas do combobox
        jogosFiltrados = self.filtrarJogosAvaliacao(int(estrelas))#pega os jogos q tem aquela avaliação desejada
        self.limite.listbox.delete(0, tk.END)#apaga a listbox
        for jogo in jogosFiltrados:
            media = self.avaliacaoMedia(jogo)#media recebe a avaliação (pode ser retirado)
            self.limite.listbox.insert(tk.END, f"{jogo.titulo} - {jogo.console} - {jogo.genero} - R${jogo.preco:.2f}")
   
    def filtrarJogosAvaliacao(self, estrelas):
        jogosFiltrados = [] #faz uma lista para pegar s jogos
        for jogo in self.listaJogos:
            if jogo.avaliacoes:
                avaliacao = self.avaliacaoMedia(jogo)#avaliação recebe a avaliação do jogo
                if int(avaliacao) == (int(estrelas)):#se a avaliação for igual ao numero de estrelas desejado
                    jogosFiltrados.append(jogo)# jogo add a lista
        return jogosFiltrados

    def cadastrarJogos(self):
        self.limite = LimiteInsereCadastro(self)

    def avaliarJogos(self):
        self.limite = LimiteInsereAvaliacao(self)

    def consultarJogos(self):
        self.limite = LimiteInsereConsulta(self)
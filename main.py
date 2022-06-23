from colecao import colecao

#cl1 = colecao(3, "teste3")
#print(cl1.insert())

from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Inserir colecao")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.idLabel = Label(self.segundoContainer,text="Id", font=self.fontePadrao)
        self.idLabel.pack(side=LEFT)

        self.id = Entry(self.segundoContainer)
        self.id["width"] = 30
        self.id["font"] = self.fontePadrao
        self.id.pack(side=LEFT)

        self.nomeLabel = Label(self.terceiroContainer, text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.terceiroContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Inserir"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.inserirColecao()
        self.autenticar.pack()

    #Método verificar senha
    #def verificaSenha(self):
    #    usuario = self.nome.get()
    #    senha = self.senha.get()
    #    if usuario == "usuariodevmedia" and senha == "dev":
    #        self.mensagem["text"] = "Autenticado"
    #    else:
    #        self.mensagem["text"] = "Erro na autenticação"

    def inserirColecao(self):
         print("1")





root = Tk()
Application(root)
root.mainloop()
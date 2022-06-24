from conexao import conexao
from apiweb import apiweb

class colecao:
    def __init__(self, id =  None, nome = None) -> None:
        self.id = id
        self.nome = nome
        pass

    def select(self, id):
        cn = conexao()
        return cn.select("select * from colecao where id_colecao = " + str(id))
        
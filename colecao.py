from conexao import conexao

class colecao:
    def __init__(self, id, nome) -> None:
        self.id = id
        self.nome = nome
        pass

    def insert(self):
        cn = conexao()
        cn.execute("insert into colecao values (" + str(self.id) + ", '" + str(self.nome) +"')")
        
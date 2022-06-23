import pandas as pd
import psycopg2 as pg
from sqlalchemy import create_engine

class conexao:
    def __init__(self) -> None:
        self.engine = create_engine('postgresql://postgres:pgsenha@localhost:5432/biblioteca')
        self.connection = pg.connect(user = "postgres", password = "pgsenha", host = "localhost", port="5432", database = "biblioteca")
        self.cursor = self.connection.cursor()

    def select(self, sql_select):
        try:
            return pd.read_sql_query(sql_select, con=self.engine)
        except NameError as erro:
            return erro

    def execute(self, sql_execute):
        try: 
            self.cursor.execute(sql_execute)
            self.connection.commit()
        except NameError as erro:
            return erro

#sql_select = "select * from dono"

#print(select)

#sql_insert = "insert into dono values ('10000120000', 'Brunão')"
#estabelecer conecção com o banco
#connection = pg.connect(user = "postgres", password = "pgsenha", host = "localhost", port="5432", database = "Petshop")

#curs.execute(sql_insert)
#connection.commit()
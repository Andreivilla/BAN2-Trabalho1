from itsdangerous import json
from sympy import print_maple_code
from colecao import colecao
from apiweb import apiweb

cl = colecao()
aw = apiweb()
 
a = cl.select(1).to_dict()

aw.post("http://localhost:4000/products", a)
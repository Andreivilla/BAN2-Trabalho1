import requests
import json

class apiweb:
    def get_simples(self, url):
        requisicao = requests.get(url)
        return requisicao


    def get_params(self, url, p):
        requisicao = requests.get(url, params=p)
        return requisicao
        

    def post(self, url, data):
        # body => json, objeto python -> json=
        # params => parametros visiveis NÃO É SEGURO FAZER ISSO -> params=
        # data => qualquer coisa
        requisicao = requests.post(url, json=data)
        return requisicao

    def patch(self, url, data):
        data = 'dicionario_python'
        requisicao = requests.patch(url, data=data)
        return requisicao

    def delete(self, url):
        requisicao = requests.delete(url)
        return requisicao



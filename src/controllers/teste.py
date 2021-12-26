from flask import Flask
from flask_restx import Api, Resource

from src.server.instance import server

app, api = server.app, server.api


teste = [   
            {'id':0, 'name':'carlos'},
            {'id':1, 'name':'marcelo'}
        ]

@api.route('/dev')
class Teste (Resource):
    def get(self):
        return teste, 200

    def delete(self):
        teste.pop()
        return 'removido', 200

    def post(self):
        dados = api.payload
        teste.append(dados)
        return dados , 201


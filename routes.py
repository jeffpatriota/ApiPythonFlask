

from ast import USub
from telnetlib import STATUS
from urllib import response
from flask import Flask, request

from dataBase import insertUsuario

app = Flask("TargetData")

@app.route("/testeapi", methods = ["GET"])
def testeApi():
    return "<h1>API com Flask</h1>"

@app.route("/cadastra/usuario", methods = ["POST"])
def cadastraUsuario():
    

    body = request.get_json()


    def geraResponse(status, mensagem, nome_do_conteudo=False, conteudo=False):
        response={}
        response["status"] = status 
        response["mensagem"] = mensagem

        if(nome_do_conteudo and conteudo):
            response[nome_do_conteudo] = conteudo
        
        return response
        
    if("nome" not in body):
        return geraResponse(400,"O parametro nome é obrigatorio")

    if("email" not in body):
        return geraResponse(400,"O parametro email é obrigatorio")

    if("senha" not in body):
        return geraResponse(400,"O parametro senha é obrigatorio")
    
    usuario = insertUsuario(body["nome"],body["email"],body["senha"])

    
    return geraResponse(200, "Usuario criado", "user", usuario)
    
app.run()
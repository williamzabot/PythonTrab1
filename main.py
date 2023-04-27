#No Windows funcionou professora! Hahahahha

import os
import pathlib
from datetime import datetime
from datetime import date
import socket

def listaArquivos():
    path = os.getcwd()
    startPathlib = pathlib.Path(path)
    lista = list(startPathlib.glob('**/*'))
    return lista

def mostraLista():
    for file in listaArquivos():
        print(str(file)+"\n")

def mostraInfo():
    data = date.today().strftime('%d/%m/%Y')
    horario = datetime.now().strftime('%H:%M')
    pathSplit = str(os.getcwd()).split("\\")
    unidadeDeDisco = pathSplit[0].replace(":", "")
    index = (len(pathSplit)-1)
    atualDiretorio = pathSplit[index]
    hostname = socket.gethostname()
    qtdArquivos = len(listaArquivos())
    print("Data: {}\nHorário: {}\nUnidade de disco: {}\nHostname: {}\nDiretório atual: {}\nQuantidade de arquivos: {}"
          .format(data, horario, unidadeDeDisco, hostname, atualDiretorio, qtdArquivos))

senhaPreDefinida = "python"
loops = 0

while True:
    if loops == 3:
        print("Esgotaram-se as tentativas")
        loops = 0
    inputSenha = str(input("Digite a senha: "))
    loops = loops+1
    if inputSenha == senhaPreDefinida:
        print("Senha correta!")
        mostraInfo()
        escolha = str(input("Quer que mostre a lista de arquivos? s ou n: "))
        if escolha == "s":
            mostraLista()

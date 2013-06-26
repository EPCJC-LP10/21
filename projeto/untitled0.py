# -*- coding: utf-8 -*-

from collections import namedtuple

import menu


servicoReg = namedtuple("servicoReg", " lavagem,revisao,mudanca do oleo,alinhamento direcao,teste a bateria")
listaserviço = []



def encontrar_posicao(codigo):
    pos = -1
    for i in range (len(listaservico)):
        if listaservico[i].id == codigo:
            pos = i
            break
                            
    return pos


def pesquisar_serviço():
    ser = input("Qual o serviço a utilizar? ")

    pos = encontrar_posicao(ser)

    if pos == -1:
        print "Não existe esse serviço"
        return

    print "Serviço: ", listaservico[pos].nome
    


def listar_serviço():
    for i in range (len(listaservico)):
        print "Nome: ", listaservico[i].nome
        
  

def eliminar_servico():
    cod = input ("Nome do servico a eliminar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe nenhum servico com esse nome"
        return

    # TODO: Confirmar eliminação
    listaservico.pop(pos)


    
def alterar_servico():
    ser = input ("Nome do servico a alterar --> ")
    pos = encontrar_posicao(ser)

    if pos == -1:
        print "Não existe nenhum servico com esse nome"
        return

    # só altera o nome
    novoservico = raw_input("Qual o servico? ")
    listaservico[pos] = listaservico[pos]._replace(servico=novoservico)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.servicos()

        if op == '1':
            inserir_servico()
        elif op =='2':
            listar_servico()
        elif op == '3':
            pesquisar_servico()
        elif op == '4':
            alterar_servico()
        elif op == '5':
            eliminar_servico()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"





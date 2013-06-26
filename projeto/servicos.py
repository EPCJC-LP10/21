# -*- coding: utf-8 -*-

from collections import namedtuple

import menu


servicosReg = namedtuple("servicosReg", " lavagem,revisao,mudanca do oleo,alinhamento direcao,teste a bateria")
listaservicos = []



def encontrar_posicao(codigo):
    pos = -1
    for i in range (len(listaservicos)):
        if listaservicos[i].id == codigo:
            pos = i
            break
                            
    return pos


def pesquisar_servicos():
    ser = input("Qual o serviço a utilizar? ")

    pos = encontrar_posicao(ser)

    if pos == -1:
        print "Não existe esse serviço"
        return

    print "Serviço: ", listaservicos[pos].nome
    


def listar_servicos():
    for i in range (len(listaservicos)):
        print "Nome: ", listaservicos[i].nome
        
  

def eliminar_servicos():
    cod = input ("Nome do servico a eliminar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe nenhum servico com esse nome"
        return

    # TODO: Confirmar eliminação
    listaservicos.pop(pos)


    
def alterar_servicos():
    ser = input ("Nome do servico a alterar --> ")
    pos = encontrar_posicao(ser)

    if pos == -1:
        print "Não existe nenhum servico com esse nome"
        return

    # só altera o nome
    novoservico = raw_input("Qual o servico? ")
    listaservicos[pos] = listaservicos[pos]._replace(servicos=novoservico)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.servicos()

        if op == '1':
            inserir_servicos()
        elif op =='2':
            listar_servicos()
        elif op == '3':
            pesquisar_servicos()
        elif op == '4':
            alterar_servicos()
        elif op == '5':
            eliminar_servicos()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"





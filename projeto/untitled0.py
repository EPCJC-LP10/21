# -*- coding: utf-8 -*-

from collections import namedtuple

import menu


oficinaReg = namedtuple("oficinaReg", "clientes, veiculos, serviços")
listaoficina = []



def encontrar_posicao(codigo):
    pos = -1
    for i in range (len(listaoficina)):
        if listaoficina[i].id == codigo:
            pos = i
            break
                            
    return pos


def pesquisar_serviço():
    cod = input("Qual o serviço a utilizar? ")

    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe esse serviço"
        return

    print "Serviço: ", listaoficina[pos].nome
    


def listar_serviço():
    for i in range (len(listaofcina)):
        print "Nome: ", listaoficina[i].nome
        
  

def eliminar_cliente():
    cod = input ("Nome do cliente a eliminar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe cliente com esse nome"
        return

    # TODO: Confirmar eliminação
    listaoficina.pop(pos)


    
def alterar_cliente():
    cod = input ("Nome do cliente a alterar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe cliente com esse nome"
        return

    # só altera o nome
    novonome = raw_input("Qual o nome do cliente? ")
    listaoficina[pos] = listaoficina[pos]._replace(nome=novonome)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.cliente()

        if op == '1':
            inserir_cliente()
        elif op =='2':
            listar_cliente()
        elif op == '3':
            pesquisar_cliente()
        elif op == '4':
            alterar_cliente()
        elif op == '5':
            eliminar_cliente()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"





# -*- coding: utf-8 -*-

from collections import namedtuple

import menu


clienteReg = namedtuple("clienteReg", "cod, nome, contato")
listaClientes = []



def encontrar_posicao(codigo):
    pos = -1
    for i in range (len(listaClientes)):
        if listaClientes[i].id == codigo:
            pos = i
            break
                            
    return pos


def inserir_clientes():
    cod = raw_input("Qual o nome do cliente? ")

    pos = encontrar_posicao(cod)

    if pos >= 0:
        print "Cliente já existente"
        return

    #ler dados
    nome = raw_input("Qual o nome do cliente? ")
    contato = raw_input("Introduza um contato do cliente? ")
    
    registo = clienteReg(cod, nome, contato)
    listaClientes.append(registo)


def pesquisar_clientes():
    nome = input("Qual o nome do cliente? ")

    pos = encontrar_posicao(nome)

    if pos == -1:
        print "Não existe cliente com esse nome"
        return

    print "Nome: ", listaClientes[pos].nome
    


def listar_clientes():
    for i in range (len(listaClientes)):
        print "Nome: ", listaClientes[i].nome
        
  

def eliminar_clientes():
    nome = input ("Nome do cliente a eliminar --> ")
    pos = encontrar_posicao(nome)

    if pos == -1:
        print "Não existe cliente com esse nome"
        return

    # TODO: Confirmar eliminação
    listaClientes.pop(pos)


    
def alterar_clientes():
    cod = input ("Nome do cliente a alterar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe cliente com esse nome"
        return

    # só altera o nome
    novonome = raw_input("Qual o nome do cliente? ")
    listaClientes[pos] = listaClientes[pos]._replace(nome=novonome)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.clientes()

        if op == '1':
            inserir_clientes()
        elif op =='2':
            listar_clientes()
        elif op == '3':
            pesquisar_clientes()
        elif op == '4':
            alterar_clientes()
        elif op == '5':
            eliminar_clientes()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"











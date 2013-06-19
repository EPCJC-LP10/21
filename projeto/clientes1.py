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


def inserir_cliente():
    cod = input("Qual o nome do cliente? ")

    pos = encontrar_posicao(cod)

    if pos >= 0:
        print "Cliente já existente"
        return

    #ler dados
    nome = raw_input("Qual o nome do cliente? ")
    
    registo = oficinaReg(clientes, veiculos,serviços)
    oficinaAlunos.append(registo)


def pesquisar_cliente():
    cod = input("Qual o nome do cliente? ")

    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe cliente com esse nome"
        return

    print "Nome: ", listaoficina[pos].nome
    


def listar_clientes():
    for i in range (len(listaclientes)):
        print "Nome: ", listaclientes[i].nome
        
  

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











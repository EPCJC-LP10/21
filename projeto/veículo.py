# -*- coding: utf-8 -*-

from collections import namedtuple

import menu


oficinaReg = namedtuple("oficinaReg", "clientes0, veiculos,serviços")
listaoficina = []



def encontrar_posicao(codigo):
    pos = -1
    for i in range (len(listaoficina)):
        if listaoficina[i].id == codigo:
            pos = i
            break
                            
    return pos


def inserir_veiculo():
    marca = raw_input("Qual a marca do veiculo? ")
    matr = input ("Qual a matricula do veiculo?")
    pos = encontrar_posicao(marca,matr)

    if pos >= 0:
        print "Veículo já existe"
        return

    #ler dados
    marca = raw_input("Qual a marca do veículo? ")
    matri = raw_input ("Qual a matricula do veículo?)
    registo = oficinaReg(cod, matri)
    listaoficina.append(registo)


def pesquisar_veiculo():
    marca = input("Qual a marca veículo a pesquisar? ")
    matr = input("Qual a matricula do veículo?")

    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Veículo nao existente"
        return

    print "Marca: ", listaoficina[pos].id
    print "Matricula: ", listaoficna[pos].nome
    


def listar_veiculo():
    for i in range (len(listaoficina)):
        print "Marca: ", listaoficina[i].id
        print "Matricula: ", listaoficina[i].no
        
  

def eliminar_veiculo():
    cod = input ("Matricula do carro a eliminar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe nenhum veículo com esta matricula"
        return

    # TODO: Confirmar eliminação
    listaoficina.pop(pos)


    
def alterar_veiculo():
    cod = input ("Matricula do veículo a alterar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe veículço com esta matricula"
        return

    # só altera o nome
    novonome = raw_input("Qual a matricula? ")
    listaoficina[pos] = listaoficina[pos]._replace(nome=novonome)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.veiculo()

        if op == '1':
            inserir_veiculo()
        elif op =='2':
            listar_veiculo()
        elif op == '3':
            pesquisar_veiculo()
        elif op == '4':
            alterar_veiculo()
        elif op == '5':
            eliminar_veiculo()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"











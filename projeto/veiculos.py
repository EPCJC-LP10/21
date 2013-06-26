# -*- coding: utf-8 -*-

from collections import namedtuple

import menu


veiculoReg = namedtuple("veiculosReg", "matricula, marca")
listaVeiculos = []



def encontrar_posicao(codigo):
    pos = -1
    for i in range (len(listaVeiculos)):
        if listaVeiculos[i].id == codigo:
            pos = i
            break
                            
    return pos


def inserir_veiculo():
    marca = raw_input("Qual a marca do veiculo? ")
    matr = raw_input ("Qual a matricula do veiculo?")
    pos = encontrar_posicao(matr)

    if pos >= 0:
        print "Veiculo ja existe"
        return

    #ler dados
    marca = raw_input("Qual a marca do veiculo? ")
    matri = raw_input ("Qual a matricula do veiculo? ")
    registo = veiculosReg(marca, matri)
    listaVeiculo.append(registo)


def pesquisar_veiculo():
    marca = input("Qual a marca veiculo a pesquisar? ")
    matr = input("Qual a matricula do veiculo?")

    pos = encontrar_posicao(marca,matr)

    if pos == -1:
        print "Veiculo nao existente"
        return

    print "Marca: ", listaVeiculos[pos].id
    print "Matricula: ", listaVeiculos[pos].nome
    


def listar_veiculo():
    for i in range (len(listaVeiculos)):
        print "Marca: ", listaVeiculos[i].id
        print "Matricula: ", listaVeiculos[i].no
        
  

def eliminar_veiculo():
    matr = input ("Matricula do carro a eliminar --> ")
    pos = encontrar_posicao(matr)

    if pos == -1:
        print "Não existe nenhum veículo com esta matricula"
        return

    # TODO: Confirmar eliminação
    listaVeiculos.pop(pos)


    
def alterar_veiculo():
    matr = input ("Matricula do veículo a alterar --> ")
    pos = encontrar_posicao(matr)

    if pos == -1:
        print "Não existe veículço com esta matricula"
        return

    # só altera o nome
    novonome = raw_input("Qual a matricula? ")
    listaVeiculos[pos] = listaVeiculos[pos]._replace(nome=novonome)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.veiculos()

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











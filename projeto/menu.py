# -*- coding: utf-8 -*-


def principal():
    print
    print " **** MENU Principal ****** "
    print
    print "   1. Gestão Clientes"
    print "   2. Registar Serviço "
    print 
    print "   0. Sair"
    print     
    
    
def clientes():
    print
    print " **** MENU CLIENTES ****** "
    print
    print "   1. Inserir novo cliente:"
    print "   2. Alterar menu do cliente: "
    print 
    print "   0. Menu Anterior"
    print 

    op = raw_input("Opção: ")
    return op


def servicos():
    print
    print " *** MENU SERVIÇOS **** "
    print
    print "1. LAVAGEM - 10€"
    print "2. Revisão - 75€"
    print "3. Mudança do Óleo - 40€"
    print "4. Alinhamento direção - 25"
    print "5. Teste á à bateria - 10€"
    print 
    print "0. Menu Anterior"

    op = raw_input("Opçao: ")
    return op


def veiculo():
    print
    print " *** MENU VEÍCULOS **** "
    print
    print "1. Inserir novo veículo:"
    print "2. Alterar dados do veículo:"
    print 
    print "0. Menu Anterior"

    op = raw_input("Opçao: ")
    return op
    

if __name__ == "__main__":
    print "Este programa nao deve ser executado diretamente"
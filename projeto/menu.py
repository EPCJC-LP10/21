# -*- coding: utf-8 -*-


def principal():
    print
    print " **** MENU Principal ****** "
    print
    print "   1. Gestao Clientes"
    print
    print "   2. Gestao Veiculos"
    print
    print "   3. Gestao Servicos"
    print 
    print "   0. Sair"
    print     
    op = raw_input("Opcao: ")
    return op
    
    
def clientes():
    print
    print " **** MENU CLIENTES ****** "
    print
    print "   1. Inserir novo cliente:"
    print "   2. Alterar menu do cliente: "
    print 
    print "   0. Menu Anterior"
    print 

    op = raw_input("Opcao: ")
    return op
    
def servicos():
    print
    print " *** MENU SERVICOS **** "
    print
    print "1. LAVAGEM - 10€"
    print "2. Revisao - 75€"
    print "3. Mudanca do Oleo - 40€"
    print "4. Alinhamento direcao - 25"
    print "5. Teste a bateria - 10€"
    print 
    print "0. Menu Anterior"

    op = raw_input("Opcao: ")
    return op


def veiculos():
    print
    print " *** MENU VEICULOS **** "
    print
    print "1. Inserir novo veiculo:"
    print "2. Alterar dados do veiculo:"
    print 
    print "0. Menu Anterior"

    op = raw_input("Opcao: ")
    return op
    

if __name__ == "__main__":
    print "Este programa nao deve ser executado diretamente"
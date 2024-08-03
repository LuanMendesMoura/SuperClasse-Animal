from classe import *
from views import *
from funcoes import *

lista_humanos = []
lista_cachorros = []


close = True
while close:
    print(menu_principal())
    op = input("Insira uma opção: ")
    if op == "1":
        lista_humanos.append(create_humano())
    elif op == "2":
        lista_cachorros.append(create_cachorro())
    elif op == "3":
        read_humanos(lista_humanos)
    elif op == "4":
        read_cachorros(lista_cachorros)
    elif op == "5":
        op = int(input("Insira o número do humano: "))
        delete_humanos(lista_humanos,op)
    elif op == "6":
        op = int(input("Insira o número do cachorro: "))
        delete_cachorros(lista_cachorros,op)
    elif op == "7":
        print(menu_acoes())
        op = input("Insira uma opção: ")
        if op == "1":
            print(sub_menu_acoes_humano())
            op = input("Insira uma opção: ")
            if op == "1":
                read_humanos(lista_humanos)
                humano = int(input("Insira o número do cachorro: "))
                f"{print(lista_humanos[humano].nome)}: {lista_humanos[humano].cumprimentar()}"
            elif op == "2":
                read_humanos(lista_humanos)
                humano = int(input("Insira o número do cachorro: "))
                f"{print(lista_humanos[humano].nome)}: {lista_humanos[humano].andar()}"
            else:
                pass
        elif op == "2":
            print(sub_menu_acoes_cachorro())
            op = input("Insira uma opção: ")
            if op == "1":
                read_cachorros(lista_cachorros)
                cao = int(input("Insira o número do cachorro: "))
                f"{print(lista_cachorros[cao].nome)}: {lista_cachorros[cao].latir()}"
            elif op == "2":
                read_cachorros(lista_cachorros)
                cao = int(input("Insira o número do cachorro: "))
                f"{print(lista_cachorros[cao].nome)}: {lista_cachorros[cao].andar()}"
            else: 
                pass
    elif op == "8":
        close = False
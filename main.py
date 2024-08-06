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
        print(sub_menu_create())
        op = input("Insira uma opção: ")
        if op == "1":
            lista_humanos.append(create_humano())
        elif op == "2":
            lista_cachorros.append(create_cachorro()) 
        else:
            print("\nOpção não encontrada!\n")
    elif op == "2": 
        print(sub_menu_read())
        op = input("Insira uma opção: ") 
        if op == "1":
            read_humanos(lista_humanos)
        elif op == "2":
            read_cachorros(lista_cachorros)
        else:
            print("\nOpção não encontrada!\n")
    elif op == "3":
        print(sub_menu_upload())
        op = input("Insira uma opção: ")
        if op == "1":
            upload_humanos(lista_humanos)
        elif op == "2":
            upload_cachorros(lista_cachorros)
        else:
            print("\nOpção não encontrada!\n")
    elif op == "4":
        print(sub_menu_delete())
        op = input("Insira uma opção: ")
        if op == "1":
            read_humanos(lista_humanos)
            op = int(input("Insira o número do humano: "))
            delete_animal(lista_humanos,op)
        elif op == "2":
            read_cachorros(lista_cachorros)
            op = int(input("Insira o número do cachorro: "))
            delete_animal(lista_cachorros,op)
        else:
            print("\nOpção não encontrada!\n")
    elif op == "5":    
        print(sub_menu_acoes())
        op = input("Insira uma opção: ")
        if op == "1":
            print(sub_menu_acoes_humano())
            op = input("Insira uma opção: ")
            if op == "1":
                read_humanos(lista_humanos)
                humano = int(input("Insira o número do humano: "))
                f"{print(lista_humanos[humano].nome,":",lista_humanos[humano].cumprimentar())}"
            elif op == "2":
                read_humanos(lista_humanos)
                humano = int(input("Insira o número do humano: "))
                f"{print(lista_humanos[humano].nome,":",lista_humanos[humano].andar())}"
            elif op == "3":
                read_humanos(lista_humanos)
                humano = int(input("Insira o número do humano: "))
                f"{print(lista_humanos[humano].nome,":",lista_humanos[humano].dormir())}"
            elif op == "4":
                read_humanos(lista_humanos)
                humano = int(input("Insira o número do humano: "))
                f"{print(lista_humanos[humano].nome,":",lista_humanos[humano].comer())}"
            else:
                print("\nOpção não encontrada!\n")
        elif op == "2":
            print(sub_menu_acoes_cachorro())
            op = input("Insira uma opção: ")
            if op == "1":
                read_cachorros(lista_cachorros)
                cao = int(input("Insira o número do cachorro: "))
                f"{print(lista_cachorros[cao].nome,":",lista_cachorros[cao].latir())}"
            elif op == "2":
                read_cachorros(lista_cachorros)
                cao = int(input("Insira o número do cachorro: "))
                f"{print(lista_cachorros[cao].nome,":",lista_cachorros[cao].andar())}"
            elif op == "3":
                read_cachorros(lista_cachorros)
                cao = int(input("Insira o número do cachorro: "))
                f"{print(lista_cachorros[cao].nome,":",lista_cachorros[cao].dormir())}"
            elif op == "4":
                read_cachorros(lista_cachorros)
                cao = int(input("Insira o número do cachorro: "))
                f"{print(lista_cachorros[cao].nome,":",lista_cachorros[cao].comer())}"
            else: 
                print("\nOpção não encontrada!\n")
        else:
            print("\nOpção não encontrada!\n")
    elif op == "6":
        close = False
    else:
        print("\nOpção não encontrada!\n")
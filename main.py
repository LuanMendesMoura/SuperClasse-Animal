from classe import *
from views import *

humanos = []
cachorros = []

def create_cachorro():
    nome = input("Nome: ")
    cor = input("Cor: ")
    tamanho = int(input("Tamanho em CM: "))
    peso = float(input("Peso em KG: "))
    idade = int(input("Idade: "))
    raca = input("Raça: ")
    cao = Cachorro(nome,cor,tamanho,peso,idade,raca)
    cachorros.append(cao)

def create_humano():
    nome = input("Nome: ")
    cor = input("Cor: ")
    tamanho = int(input("Altura em CM: "))
    peso = float(input("Peso em KG: "))
    idade = int(input("Idade: "))
    escolaridade = input("Escolaridade: ")
    ocupacao = input("Profissão: ")
    humano = Humano(nome,cor,tamanho,peso,idade,escolaridade,ocupacao)
    humanos.append(humano)

def read_cachorros():
    for index,cao in zip(range(0,len(cachorros)),cachorros):
        print(f"""{index} - Nome: {cao.nome}\n     Cor: {cao.cor}\n     Tamanho: {cao.tamanho} CM
     Peso: {cao.peso} KG\n     Idade: {cao.idade} Anos\n     Raça: {cao.raca}\n""")

def read_humanos():
    for index,humano in zip(range(0,len(humanos)),humanos):
        print(f"""{index} - Nome: {humano.nome}\n     Cor: {humano.cor}\n     Tamanho: {humano.tamanho} CM
     Peso: {humano.peso} KG\n     Idade: {humano.idade} Anos\n     Escolaridade: {humano.escolaridade}\n     Ocupação: {humano.ocupacao}\n""")

def delete_cachorros(op):
    cachorros.pop(op)

def delete_humanos(op):
    humanos.pop(op)


close = True
while close:
    print(menu_principal())
    op = input("Insira uma opção: ")
    if op == "1":
        create_humano()
    elif op == "2":
        create_cachorro()
    elif op == "3":
        read_humanos()
    elif op == "4":
        read_cachorros()
    elif op == "5":
        op = int(input("Insira o número do humano: "))
        delete_humanos(op)
    elif op == "6":
        op = int(input("Insira o número do cachorro: "))
        delete_cachorros(op)
    elif op == "7":
        close = False
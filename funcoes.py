from classe import * 

def create_cachorro():
    nome = input("Nome: ")
    cor = input("Cor: ")
    tamanho = int(input("Tamanho em CM: "))
    peso = float(input("Peso em KG: "))
    idade = int(input("Idade: "))
    raca = input("Raça: ")
    cao = Cachorro(nome,cor,tamanho,peso,idade,raca)
    return cao

def create_humano():
    nome = input("Nome: ")
    cor = input("Cor: ")
    tamanho = int(input("Altura em CM: "))
    peso = float(input("Peso em KG: "))
    idade = int(input("Idade: "))
    escolaridade = input("Escolaridade: ")
    ocupacao = input("Profissão: ")
    humano = Humano(nome,cor,tamanho,peso,idade,escolaridade,ocupacao)
    return humano

def read_cachorros(lista_cachorros):
    for index,cao in zip(range(0,len(lista_cachorros)),lista_cachorros):
        print(f"""\n{index} - Nome: {cao.nome}\n     Cor: {cao.cor}\n     Tamanho: {cao.tamanho} CM
     Peso: {cao.peso} KG\n     Idade: {cao.idade} Anos\n     Raça: {cao.raca}\n""")

def read_humanos(lista_humanos):
    for index,humano in zip(range(0,len(lista_humanos)),lista_humanos):
        print(f"""\n{index} - Nome: {humano.nome}\n     Cor: {humano.cor}\n     Tamanho: {humano.tamanho} CM
     Peso: {humano.peso} KG\n     Idade: {humano.idade} Anos\n     Escolaridade: {humano.escolaridade}\n     Ocupação: {humano.ocupacao}\n""")

def upload_cachorros(lista):
    posicao = int(input("Insira o número do cachorro: "))
    nome = input(f"|Nome Antigo: {(lista[posicao].nome)}| - Novo Nome: ")
    cor = input(f"|Cor Antiga: {(lista[posicao].cor)}| - Nova Cor: ")
    tamanho = int(input(f"|Altura Antiga: {(lista[posicao].altura)}| - Nova Altura em CM: "))
    peso = float(input(f"|Peso Antigo: {(lista[posicao].peso)}| - Novo Peso em KG: "))
    idade = int(input(f"|Idade Antiga: {(lista[posicao].idade)}| - Nova Idade: "))
    raca = input(f"|Raça Antiga: {(lista[posicao].raca)}| - Nova Raça: ")
    lista[posicao].nome = nome
    lista[posicao].cor = cor
    lista[posicao].tamanho = tamanho
    lista[posicao].peso = peso
    lista[posicao].idade = idade
    lista[posicao].raca = raca

def upload_humanos(lista):
    posicao = int(input("Insira o número do humano: "))
    nome = input(f"|Nome Antigo: {(lista[posicao].nome)}| - Novo Nome: ")
    cor = input(f"|Cor Antiga: {(lista[posicao].cor)}| - Nova Cor: ")
    tamanho = int(input(f"|Altura Antiga: {(lista[posicao].tamanho)}| - Nova Altura em CM: "))
    peso = float(input(f"|Peso Antigo: {(lista[posicao].peso)}| - Novo Peso em KG: "))
    idade = int(input(f"|Idade Antiga: {(lista[posicao].idade)}| - Nova Idade: "))
    escolaridade = input(f"|Escolaridade Antiga: {(lista[posicao].escolaridade)}| - Nova Escolaridade: ")
    ocupacao = input(f"|Profissão Antiga: {(lista[posicao].ocupacao)}| - Nova Profissão: ")
    lista[posicao].nome = nome
    lista[posicao].cor = cor
    lista[posicao].tamanho = tamanho
    lista[posicao].peso = peso
    lista[posicao].idade = idade
    lista[posicao].escolaridade = escolaridade
    lista[posicao].ocupacao = ocupacao

def delete_animal(lista,op):
    lista.pop(op)

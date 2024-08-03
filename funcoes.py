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

def delete_cachorros(lista_cachorros,op):
    lista_cachorros.pop(op)

def delete_humanos(lista_humanos,op):
    lista_humanos.pop(op)
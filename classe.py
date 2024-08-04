class Animal():
    nome=str
    cor=str
    tamanho=float
    peso=float
    idade=int
    coracao:bool
    racional:bool
    instinto:bool

    def __init__(self,nome,cor,tamanho,peso,idade,coracao,racional,instinto):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.peso = peso
        self.idade = idade
        self.coracao = coracao
        self.racional = racional
        self.instinto = instinto

    def andar(self):
        return("Andando ")
    
    def dormir(self):
        return("Dormindo ")
    
    def comer(self):
        return("Comendo ")

class Cachorro(Animal):
    raca = str
    
    def __init__(self,nome,cor,tamanho,peso,idade,raca):
        super().__init__(nome,cor,tamanho,peso,idade,True,False,True)
        self.raca = raca

    def latir(self):
        return("Au-au ")

class Humano(Animal):
    escolaridade = str
    ocupacao = str

    def __init__(self, nome, cor, tamanho, peso, idade, escolaridade, ocupacao):
        super().__init__(nome,cor,tamanho,peso,idade,True,True,True)
        self.escolaridade = escolaridade
        self.ocupacao = ocupacao

    def cumprimentar(self):
        return("Olá, tudo bem? ")

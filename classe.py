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

class Cachorro(Animal):
    raca = str
    
    def __init__(self,nome,cor,tamanho,peso,idade,raca):
        super().__init__(nome,cor,tamanho,peso,idade,True,False,True)
        self.raca = raca

    def latir(self):
        print("Au-au")

    # def info_cachorro(self):
    #     return {"nome": self.nome}

    # def atualizar_info_cachorro(self,nome,cor,tamanho,peso,idade,raca):
    #     self.nome = nome
    #     self.cor = cor
    #     self.tamanho = tamanho
    #     self.peso = peso
    #     self.idade = idade
    #     self.raca = raca

class Humano(Animal):
    escolaridade = str
    ocupacao = str

    def __init__(self, nome, cor, tamanho, peso, idade, escolaridade, ocupacao):
        super().__init__(nome,cor,tamanho,peso,idade,True,True,True)
        self.escolaridade = escolaridade
        self.ocupacao = ocupacao

    # def atualizar_dados_cachorro(self,nome,cor,tamanho,peso,idade,escolaridade, ocupacao):
    #     self.nome = nome
    #     self.cor = cor
    #     self.tamanho = tamanho
    #     self.peso = peso
    #     self.idade = idade
    #     self.escolaridade = escolaridade
    #     self.ocupacao = ocupacao
    

class Pessoa():
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo


def criar(nome, idade, sexo):
    pessoa = Pessoa(nome, idade, sexo)
    return pessoa


def ler(pessoa):
    print(f'Nome: {pessoa.nome}')
    print(f'Idade: {pessoa.idade}')
    print(f'Sexo: {pessoa.sexo}')


def atualizar(pessoa, nome, idade, sexo):
    pessoa.nome = nome
    pessoa.idade = idade
    pessoa.sexo = sexo


def excluir(pessoa):
    del pessoa


pessoas = []

pessoa1 = criar("Pedro", 35, "masculino")
pessoas.append(pessoa1)

pessoa2 = criar("Maria", 25, "feminino")
pessoas.append(pessoa2)

ler(pessoa1)

atualizar(pessoa1, "Ana", 30, "feminino")

ler(pessoa1)

excluir(pessoa2)

print(pessoas)

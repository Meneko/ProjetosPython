class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self.nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if not isinstance(idade, int) and idade > 0:
            self._idade = idade
        else:
            raise ValueError("Idade deve ser um numero inteiro e positivo!")

def main():
    pessoa = Pessoa("João", 30)
    print(pessoa.nome)
    print(pessoa.idade)

    pessoa.nome = 'Maria'
    pessoa.idade = 25

    print(pessoa.nome)
    print(pessoa.idade)

if __name__ == '__main__':
    main()
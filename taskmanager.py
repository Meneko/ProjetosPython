from datetime import datetime
class Funcionarios:
    def __init__(self, nome, idade, sexo, ano_nascimento):
        self.nome = nome
        self.idade = int(idade)
        self.sexo = sexo
        self.ano_nascimento = int(ano_nascimento)

    def guardar(self):
        return f'Nome do funcionario: {self.nome} | Idade do funcionario: {self.idade} | Sexo do funcionario: {self.sexo} | Ano de nascimento: {self.ano_nascimento}\n'


funcionarios = []

for contador in range(1,1001): #If u want to change the number of workers, just change the 1001 to one value that u want =) // Se você quiser mudar o numero de funcionarios, apenas mude o 10001 para um valor de sua escolha =)

    nome = input('Digite o nome do funcionário: ')
    while nome.isdigit():
        print('Introduza apenas caracteres alfabeticos!')
        nome = input('Digite o nome do funcionário: ')

    idade = input('Digite a idade: ')
    while not idade.isdigit():
        print('insira apenas digitos numericos!')
        idade = input('Digite a idade do funcionário: ')
    idade = int(idade)

    sexo = input('Insira o sexo do funcionário(M/F): ')
    while not sexo == 'M' or sexo == 'F':
        print('Insira apenas M ou F!')
        sexo = input('Insira o sexo do funcionário(M/F): ')

    ano_nascimento = input('Insira o ano de nascimento do funcionário: ')
    while not ano_nascimento.isdigit() or len(ano_nascimento) != 4:
        print('Insira apenas 4 digitos númericos!')
        ano_nascimento = input('Insira o ano de nascimento do funcionário: ')
    ano_nascimento = int(ano_nascimento)

    pessoa = Funcionarios(nome.capitalize(), idade, sexo.upper(), ano_nascimento)
    funcionarios.append(Funcionarios.guardar(pessoa))

print(funcionarios)

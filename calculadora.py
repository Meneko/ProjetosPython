def operacoes(n1, n2, operacao):
    if operacao == '+':
        return n1 + n2
    elif operacao == '-':
        return n1 - n2
    elif operacao == '*':
        return n1 * n2
    elif operacao == '/':
        return n1 / n2



def calculadora(textoinicio):
    print(textoinicio)
    operacao = input("Introduza sua operação > ")
    while operacao not in ['+', '-', '*', '/']:
        operacao = input(f"\n{textoinicio}\nIntroduza apenas uma opção valida! Introduza sua opção> ")
    n1 = int(input("Introduza o primeiro numero > "))
    while not isinstance(n1, int):
        n1 = int(input(f"Introduza apenas numeros! > "))
    n2 = int(input("introduza o segundo numero > "))
    while not isinstance(n2, int):
        n2 = int(input(f"Introduza apenas numeros! > "))
    print(f"O resultado de {n1} {operacao} {n2} é igual = {operacoes(n1, n2, operacao)}")
    resultado = operacoes(n1, n2, operacao)
    recomecar(resultado)


def recomecar(resultado):
    denovo = input("Você gostaria de calcular uma conta novamente ? Se sim digite \"S\" se não digite \"N\" >")
    while True:
        if denovo.upper() == 'S':
            condicao = input("Gostaria de inserir um numero na memoria ? Responda com S ou N >")
            if condicao.upper() == "S":
                print("Introduza S para usar o resultado da ultima Operação.")
                print("Introduza N para criar uma memoria da sua escolha.")
                condicao = input("Responda com S ou N >")
                if condicao.upper() == "S":
                    valormem = resultado
                    print(f"O resultado de {resultado} + {valormem} = ")
                    resultado += valormem
                    print(resultado)
                    calculadora(textoinicio = "|+ para soma         |\n|- para subtração    |\n|* para multiplicação|\n|/ para divisão      |\n")
                elif condicao.upper() == "N":
                    valormem = int(input("Introduza um novo valor para a memoria >"))
                    while not isinstance(valormem, int):
                        print("Introduza apenas numeros")
                        valormem = input("Introduza um novo valor para a memoria >")
                    print(f"O resultado de {resultado} + {valormem} = ")
                    resultado += valormem
                    print(resultado)
                    calculadora(textoinicio = "|+ para soma         |\n|- para subtração    |\n|* para multiplicação|\n|/ para divisão      |\n")
                else:
                    continue
            elif condicao == "N":
                print("Nenhuma memoria gravada!")
                calculadora(textoinicio = "|+ para soma         |\n|- para subtração    |\n|* para multiplicação|\n|/ para divisão      |\n")
            else:
                continue
        elif denovo.upper() == 'N':
            break
        else:
            print("Erro, digite apenas \"S\" ou \"N\"")
            continue

def main():
    print(f"Bem vindo {nome.capitalize()} a um programa que é uma calculadora!")
    print("-" * 30)
    calculadora(textoinicio = "|+ para soma         |\n|- para subtração    |\n|* para multiplicação|\n|/ para divisão      |\n")



nome = input("Qual é seu nome ? > ")
while not isinstance(nome, str):
    print("Insira um nome correto!")
    nome = input("Qual é seu nome ? > ")
main()

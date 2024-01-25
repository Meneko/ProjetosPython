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
    n1 = input("Introduza o primeiro numero > ")
    while n1.isdigit() == False:
        n1 = input(f"Introduza apenas numeros! > ")
    n2 = input("introduza o segundo numero > ")
    while n2.isdigit() == False:
        n2 = input(f"Introduza apenas numeros! > ")
    print(f"O resultado de {n1} {operacao} {n2} é igual = {operacoes(n1, n2, operacao)}")
    recomecar()


def recomecar():
    denovo = input("Você gostaria de calcular uma conta novamente ? Se sim digite \"S\" se não digite \"N\"")
    while True:
        if denovo.upper() == 'S':
            calculadora()
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
main()

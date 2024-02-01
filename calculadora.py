import math
class Calculadora:
    def __init__(self, operacao, n1, n2):
        self.operacao = operacao
        self.n1 = n1
        self.n2 = n2

    def returnoperacao(self):
        match self.operacao:
            case '+':
                return self.n1 + self.n2

            case '-':
                return self.n1 - self.n2

            case '/':
                if self.n2 > 0:
                    return self.n1 / self.n2
                else:
                    raise ZeroDivisionError('Não se pode dividir por zero')

            case '*':
                return self.n1 * self.n2

            case 'sqrt':
                return self.n1 + math.sqrt(self.n2)

            case '^':
                return self.n1 ** self.n2

    def validar(self):
        if self.operacao in {'+', '-', '*', '/', 'sqrt', '^'}:
            pass
        else:
            raise Exception('A operação inserida é incorreta')

    def validarnum1(self):
        if isinstance(self.n1, int):
            pass
        else:
            raise ValueError('O numero inserido não é inteiro')

    def validarnum2(self):
        if isinstance(self.n2, int):
            pass
        else:
            raise ValueError('O numero inserido não é inteiro')


def main():
    print('Olá!, bem vindo a calculadora!')
    print('Introduza AC, para apagar tudo, e SAIR para sair!')
    n1 = None
    n2 = None
    resultado = 0
    while True:
        operacao = input('Insira uma operação presente nessa lista \'+\', \'-\', \'*\', \'/\', \'sqrt\', \'^\'> ')
        calculadora = Calculadora(operacao.lower(), None, None)
        calculadora.validar()

        if operacao in {'+', '-', '*', '/', '^'}:
            if not n1 is None:
                pass
            else:
                n1 = input('Insira o primeiro numero> ')
                try:
                    n1 = int(n1)
                except:
                    if n1.upper() == 'SAIR':
                        break
                    elif n1.upper() == 'AC':
                        n1 = None
                        n2 = None
                        resultado = 0
                        print('TODOS OS ULTIMOS NUMEROS FORAM LIMPOS DO CACHE DO SISTEMA!')
                        continue
                    else:
                        calculadora = Calculadora(operacao, n1, None)
                        calculadora.validarnum1()

            if n2 is None:
                n2 = input('Insira o segundo numero> ')
            else:
                n2 = input('Insira o numero> ')
            try:
                n2 = int(n2)
            except:
                if n2.upper() == 'SAIR':
                    break
                elif n2.upper() == 'AC':
                    n1 = None
                    n2 = None
                    resultado = 0
                    print('TODOS OS ULTIMOS NUMEROS FORAM LIMPOS DO CACHE DO SISTEMA!')
                    continue
                else:
                    calculadora = Calculadora(operacao, n1, n2)
                    calculadora.validarnum2()
            calculadora = Calculadora(operacao, n1, n2)
            while True:
                if resultado == 0:
                    resultado = calculadora.returnoperacao()
                    break
                else:
                    resultado = calculadora.returnoperacao() + n1
                    break
            print(f'{n1} {operacao} {n2} = \n{resultado}')
            n1 = resultado
        else:
            n2 = input('Insira o numero da raiz quadrada> ')
            try:
                n2 = int(n2)
            except:
                if n2.upper() == 'SAIR':
                    break
                elif n2.upper() == 'AC':
                    n1 = None
                    n2 = None
                    resultado = 0
                    print('TODOS OS ULTIMOS NUMEROS FORAM LIMPOS DO CACHE DO SISTEMA!')
                    continue
                else:
                    calculadora = Calculadora(operacao, n1, None)
                    calculadora.validarnum1()
            calculadora = Calculadora(operacao, 0, n2)
            while True:
                if resultado == 0:
                    resultado = calculadora.returnoperacao()
                    break
                else:
                    resultado = calculadora.returnoperacao() + n1
                    break
            print(f'√{n2} ≅ {round(resultado, 6)}')
            n1 = resultado



    print('Obrigado por usar nossa calculadora =)')


if __name__ == '__main__':
    main()

class Calculadora:

    def __init__(self, operacao, n1, n2):
        self.operacao = operacao
        self.n1 = n1
        self.n2 = n2

    def returnoperacao(self):
        if self.operacao == '+':
            return Calculadora.soma(self)
        elif self.operacao == '-':
            return Calculadora.subtracao(self)
        elif self.operacao == '*':
            return Calculadora.multiplicacao(self)
        elif self.operacao == '/':
            return Calculadora.divisao(self)

    def validar(self):
        operacoes = ['+', '-', '*', '/']
        if self.operacao in operacoes:
            pass
        else:
            raise Exception('A operação inserida é incorreta')

    def validarnum1(self):
        if isinstance(self.n1, int):
            pass
        else:
            raise ValueError('O numero inserido não é inteiro')

    def validarnum2(self):
        if isinstance(self.n1, self.n2, int):
            pass
        else:
            raise ValueError('O numero inserido não é inteiro')

    def soma(self):
        return (self.n1 + self.n2)

    def subtracao(self):
        return (self.n1 - self.n2)

    def divisao(self):
        if self.n2 > 0:
            return (self.n1 / self.n2)
        else:
            raise ZeroDivisionError('Não se pode dividir por zero')

    def multiplicacao(self):
        return (self.n1 * self.n2)


def main():
    ResultadoLocal = ResultadoGlobal
    print('Olá!, bem vindo a calculadora!')
    print('Introduza AC, para apagar tudo, e SAIR para sair!')
    while True:
        operacao = input('Insira uma operação presente nessa lista \'+\', \'-\', \'*\', \'/\'')
        calculadora = Calculadora(operacao, n1=None, n2=None)
        calculadora.validar()

        n1 = input('Insira o primeiro numero')
        try:
            n1 = int(n1)
        except:
            if n1.upper() == 'SAIR':
                break
            elif n1.upper() == 'AC':
                ResultadoLocal = ResultadoGlobal
                print('TODOS OS ULTIMOS NUMEROS FORAM LIMPOS DO CACHE DO SISTEMA!')
                continue
            else:
                calculadora = Calculadora(operacao, n1, n2=None)
                calculadora.validarnum1()

        n2 = input('Insira o segundo numero')
        try:
            n2 = int(n2)
        except:
            if n2.upper() == 'SAIR':
                break
            elif n2.upper() == 'AC':
                ResultadoLocal = ResultadoGlobal
                print('TODOS OS ULTIMOS NUMEROS FORAM LIMPOS DO CACHE DO SISTEMA!')
                continue
            else:
                calculadora = Calculadora(operacao, n1, n2)
                calculadora.validarnum2()

        calculadora = Calculadora(operacao, n1, n2)
        resultado = calculadora.returnoperacao() + ResultadoLocal
        print(f'{n1} {operacao} {n2} = \n{resultado}')
        ResultadoLocal = resultado

    print('Obrigado por usar nossa calculadora =)')


ResultadoGlobal = 0

if __name__ == '__main__':
    main()


def fim():
    return 'Obrigado por usar nossa calculadora ='

class ContaBancaria:
    def __init__(self, nidentificao, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo <= valor:
            self.saldo -= valor
            return True
        else:
            return False


class ContaCorrente(ContaBancaria):
    def __init__(self, nidentificao, saldo, limite):
        super().__init__(nidentificao, saldo)
        self.limite = limite


class ContaPoupanca(ContaBancaria):
    def __init__(self, nidentificao, saldo, taxa_juros):
        super().__init__(nidentificao, saldo)
        self.taxa_juros = taxa_juros

def main():
    conta_corrente = ContaCorrente(123, 1000, 500)
    conta_poutanca = ContaPoupanca(456, 2000, 0.05)

    conta_corrente.depositar(500)
    conta_poutanca.depositar(1000)

if __name__ == '__main__':
    main()
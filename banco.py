class SaldoInsuficienteError(Exception):
    pass

class Conta:
    def __init__(self, saldo, limite):
        self.saldo = saldo
        self.limite = limite

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            raise SaldoInsuficienteError("Você não tem esse saldo disponivel!")
        else:
            self.saldo -= valor

    def get_saldo(self):
        return f'Saldo: {self.saldo}'


conta = Conta(100, 500)

conta.depositar(100)
print(conta.saldo)

try:
    conta.sacar(201)
except SaldoInsuficienteError as erro:
    print(erro)

print(conta.saldo)


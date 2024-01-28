class Veiculo:
    def ligar(self):
        raise NotImplementedError


class Carro(Veiculo):
    def ligar(self):
        print('Carro - Ligando o Veiculo')


class Moto(Veiculo):
    def ligar(self):
        print('Moto - Ligando o Veiculo')


def main():
    veiculos = [Carro(), Moto()]
    for veiculo in veiculos:
        veiculo.ligar()


if __name__ == '__main__':
    main()
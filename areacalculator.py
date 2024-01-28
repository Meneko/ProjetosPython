class FiguraGeometrica():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def calcularArea(self):
        raise NotImplementedError


class Quadrado(FiguraGeometrica):
    def __init__(self, nome, cor, lado):
        super().__init__(nome, cor)
        self.lado = lado

    def calcularArea(self):
        return self.lado * self.lado


class Retangulo(FiguraGeometrica):
    def __init__(self, nome, cor, largura, altura):
        super().__init__(nome, cor)
        self.largura = largura
        self.altura = altura

    def calcularArea(self):
        return self.largura * self.altura


class Circulo(FiguraGeometrica):
    def __init__(self, nome, cor, raio):
        super().__init__(nome, cor)
        self.raio = raio

    def calcularArea(self):
        return 3.14 * (self.raio**2)


def main():
    quadrado = Quadrado('Quadrado', 'Verde', 10)
    retangulo = Retangulo('Retângulo', 'Azul', 5, 10)
    circulo = Circulo('Circulo', 'Vermelho', 5)

    print(f'A area do quadrado: {quadrado.calcularArea()}')
    print(f'A area do retangulo: {retangulo.calcularArea()}')
    print(f'A area do circulo: {circulo.calcularArea()}')


if __name__ == '__main__':
    main()
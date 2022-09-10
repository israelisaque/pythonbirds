class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    israel = Pessoa(nome='Israel')
    isaque = Pessoa(israel, nome="Isaque")
    print(Pessoa.cumprimentar(israel))
    print(id(israel))
    print(israel.cumprimentar())
    print(israel.nome)
    print(israel.idade)
    for filho in isaque.filhos:
        print(filho.nome)


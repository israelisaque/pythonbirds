class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


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
    isaque.sobrenome = "Oliveira"   #Adicionando atributo em tempo de execução
    del isaque.filhos   #Removendo atributo em tempo de execução
    print(isaque.__dict__)   #__dict__ exibe os atributos de instância
    print(israel.__dict__)
    print(Pessoa.olhos)
    print(israel.olhos)
    print(isaque.olhos)
    print(id(Pessoa.olhos), id(israel.olhos), id(isaque.olhos))
    print(Pessoa.metodo_estatico(), israel.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), israel.nome_e_atributos_de_classe())


class Pessoa:
    def cumprimenta(self):
        return 'Olá'


if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimenta(p))
    print(id(p))
    print(p.cumprimenta())


class MyClass:
    def __init__(self, x, preco):
        self.x = x
        self.preco = preco
        self.y = 6
    def __repr__(self):
        return f'Vetor({self.x!r})'

    def __format__(self, spec):
        if spec == 'moeda':
            return f'R$ {self.preco:,.2f}'

m = MyClass(x="opa", preco=200000)
print(f'{m:moeda}')

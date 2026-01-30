def gerar_acumulador():
    historico = []
    def add(a):
        historico.append(a)
        return historico
    return add

h = gerar_acumulador()

a = id(h.__closure__[0].cell_contents)
b = id(h('a'))
print(a == b)


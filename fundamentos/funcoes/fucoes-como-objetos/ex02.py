def dobrar(n):
    return n * 2

def triplicar(n):
    return n * 3

operar = {
    '2x': dobrar,
    '3x': triplicar
}

n = float(input('Número: '))
op = input('Operação: ')
print(operar.get(op)(n))

import functools

def mult(num1, num2):
    return num1 * num2

acoes = {
    'x': mult,
    '2x': functools.partial(mult, num2=2),
    '3x': functools.partial(mult, num2=3),
    '4x': functools.partial(mult, num2=4),
    '1543x': functools.partial(mult, num2=1543)
}
print(acoes.get('5x', mult)(2, 5))
import functools

def multiplicar_resultado(fator):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) * fator
        return wrapper
    return decorator

@multiplicar_resultado(3)
def n():
    return 10

print(n())



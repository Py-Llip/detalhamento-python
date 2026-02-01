from functools import wraps

def limitador_chamadas(max_vezes):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal max_vezes
            max_vezes -= 1
            if max_vezes < 0:
                return None
            return func(*args, **kwargs)
        return wrapper
    return decorator

@limitador_chamadas(5)
def my_func():
    print('minha funcao')

for n in range(10):
    my_func()
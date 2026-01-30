# import functools
#
# def meu_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         """Documentação do wrapper"""
#         print('Log: executando a função...')
#         return func(*args, **kwargs)
#     return wrapper
#
# @meu_decorator
# def saudacao(nome):
#     """Retorna uma saudacao amigavel"""
#     return f'Olá, {nome}!'
#
# print(saudacao.__name__)
# print(saudacao.__doc__)
#
# print(saudacao('Fellipe'))
###########################################################

import functools

def repetir(n):
    def decorator_real(func):
        @functools.wraps(func) # Preserva metadados da função original [8, 9]
        def wrapper(*args, **kwargs):
            resultado = None
            for _ in range(n):
                resultado = func(*args, **kwargs)
            return resultado
        return wrapper
    return decorator_real

@repetir(n=4)
def saudar(nome):
    print(f"Olá, {nome}!")

saudar("Alice")
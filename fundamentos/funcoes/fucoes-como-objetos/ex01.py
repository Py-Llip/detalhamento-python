def executar_pipeline(valor, lista_funcoes):
    for func in lista_funcoes:
        valor = func(valor)
    return valor

print(executar_pipeline(2, [lambda x: x ** 2, lambda x: x * 2]))
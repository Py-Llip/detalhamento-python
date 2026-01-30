# Closure
def multiplicador(multiplicar, opa = None):
    def por(numero):
        print(opa)
        return numero * multiplicar

    return por

dobrar = multiplicador(2)
print(multiplicador(2).__closure__[1].cell_contents)
print(dobrar.__code__.co_freevars)

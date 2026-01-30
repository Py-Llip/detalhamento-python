def fabrica(n):
    def interna(arg):
        return arg * n
    return interna

dobrar = fabrica(2)

print(dobrar.__code__.co_freevars)
print(fabrica.__code__.co_cellvars)
print(fabrica.__code__.co_varnames)
print(dobrar.__closure__[0].cell_contents)
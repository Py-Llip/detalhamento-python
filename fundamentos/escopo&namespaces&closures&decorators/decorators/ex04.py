def contar_metodos(cls):
    print(len([i for i in vars(cls).values() if callable(i)]))
    return cls

@contar_metodos
class MyClass:
    var = 0
    def __init__(self):
        pass
    def method(self):
        ...
    def other_method(self):
        pass
    # def __doc__(self):
    #     """My doc"""
    #     pass

a = MyClass.__name__
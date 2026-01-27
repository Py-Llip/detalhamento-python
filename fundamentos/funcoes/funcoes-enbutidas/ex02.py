def sens(lista1, lista2, lista3):
    return all(any(x > 50 for x in i) for i in zip(lista1, lista2, lista3, strict=True))
    # m = []
    # c = 0
    # for i in zip(lista1, lista2, lista3, strict=True):
    #     print(i)
    #     if any(list(map(lambda x: x > 50, i))):
    #         m.append(True)
    #     else:
    #         m.append(False)
    # print(m)
    # return all(m)

print(sens([1, 5], [2, 62], [400, 7]))
l = list(x > 50 for x in [2, 3, 4, 50, 52, 3, 5])
print(l)
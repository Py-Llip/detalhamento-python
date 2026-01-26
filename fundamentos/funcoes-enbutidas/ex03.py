lista = [1, 1, 3]
# for e, i in enumerate(lista):
#     try:
#         if i == e + lista[e+1]:
#             print(i)
#     except:
#         break
for atual, proximo in zip(lista, lista[1:]):
    if atual == proximo:
        print(atual)

def invite_matriz(matriz: list):
    transposta = zip(*matriz)
    e = []
    # for linha, coluna in zip(matriz, transposta):
    #     e.append(list(linha) == list(coluna))
    # print(e)
    # if all(e):
    #     print('simetrica')
    # else:
    #     print('assimetrica')
    if all(list(linha) == list(coluna) for linha, coluna in zip(matriz, transposta)):
        print('simetrica')
    else:
        print('assimetrica')


invite_matriz([[5,5], [5, 5]])
# 5, 7    5, c
# c, d    7, d
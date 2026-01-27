matriz = [[6, 7, 8], [9, 10, 11], [12, 13, 14]]
multiplos = [i**2 for l in matriz for i in l if i % 3 == 0]
print(multiplos)
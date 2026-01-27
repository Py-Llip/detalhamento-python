frases = ['Python é incrível', 'Aprender lógica é essencial', 'Python é versátil']
conjunto = {p.lower() for palavras in frases for palavra in palavras.split() if len(p := palavra.strip()) > 4}
print(conjunto)
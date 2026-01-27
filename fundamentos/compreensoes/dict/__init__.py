produtos = {'TV': 1000,
            'Fone': 40,
            'Monitor': 60,
            'Mouse': 55}

precos = {novo: i for i, p in produtos.items() if (novo := p - p * 0.1) > 50}
print(precos)
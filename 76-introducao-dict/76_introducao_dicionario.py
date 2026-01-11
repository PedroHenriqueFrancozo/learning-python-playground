"""
Tópico: Introdução a Dicionários em python
foco: Dicionário são estrutura de dados do tipo par de "chave" e "valor"
"""
# Criando dicionário utilizando chaves {}
produtos = {
    'produto': 'arroz',
    'preco': 10.99,
    'quantidade': 20,
    'marca': 'Tio Nego',
    'local': [
        {'corredor': 1, 'partilheira': 5 },
    ],
}


# Para pegar ambos valores ao mesmo tempo, usar o método .items()
for chave in produtos.items():
    print(chave)

print()

# Outra forma de itera sobre a chave
for chave in produtos:
    print(chave, produtos[chave])

print()

# Criando dicionário utilizando o classe dict()
carro = dict(marca='ford', nome='escort', ano='1999', valor='13.900')

print(carro['marca'])
print(carro['nome'])



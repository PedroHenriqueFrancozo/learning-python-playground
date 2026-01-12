"""
Topic: Métodos úteis dos dicionários
Focus: Técnicas de iteralção utilizando os métodos .items(), .enumerate(), .keys(), .values(), .setdefault(), .copy(), .get(), .pop(), .popitem(), .update().
"""

carro = {
    'marca': 'Nissan',
    'nome': 'GT-R35 Nismo',
    'ano': '2020',
}   

print(len(carro))
print()
print(list(carro.keys()))
print()
print(list(carro.values()))
print()
print(list(carro.items()))




# pessoa.setdefault('idade', 0)
# print(pessoa['idade'])


# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)
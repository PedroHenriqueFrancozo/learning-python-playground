"""
Topic: Métodos úteis dos dicionários
Focus: Técnicas de iteralção utilizando os métodos .items(), .enumerate(), .keys(), .values(), .setdefault(), .copy(), .get(), .pop(), .popitem(), .update().
"""

carro = {
    'marca': 'Nissan',
    'nome': 'GT-R35 Nismo',
    'ano': '2020',
    # 'valor': 120000,
}   

print(len(carro))
print()
print(list(carro.keys()))
print()
print(list(carro.values()))
print()
print(list(carro.items()))

carro.setdefault('valor', 'Valor do carro ainda não está disponível')
print(carro['valor'])


"""
Topic: Métodos úteis dos dicionários
Focus: Técnicas de iteralção utilizando os métodos .items(), .enumerate(), .keys(), .values(), .setdefault(), .copy(), .get(), .pop(), .popitem(), .update().
"""

import copy # módolu copy

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
print()


# Exemplo de uma Shallow copy
moto = {
    'moto1': 'z1000',
    'moto2': 'mt-09',
}

moto2 = moto.copy()

# Alterando o valor do clone para ver a mudança no dicionário original.
moto2['moto1'] = 's1000r'
print(moto)
print(moto2)
print()


# Realizando uma cópia profunda
moto3 = {
    'moto3': 'z1000',
    'moto4': 'mt-09',
}

moto4 = copy.deepcopy(moto3)

# Alterando o valor da cópia para ver que não será mais afetada 
moto4['moto3'] = 's1000r'
print(moto3)
print(moto4)
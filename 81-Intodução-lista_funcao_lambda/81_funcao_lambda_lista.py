"""
Topic: Função Lambda + list.sort e sorted + Ordenação
"""

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

lista2 = [
    {'marca': 'ford', 'modelo': 'mustang'},
    {'marca': 'bmw', 'modelo': 'x1'},
    {'marca': 'chevrolet', 'modelo': 'camaro'},
]


def exibir(lista):
    for item in lista:
        print(item)
    print()


l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

l3 = sorted(lista2, key=lambda item: item['marca'])
l4 = sorted(lista2, key=lambda item: item['modelo'])

exibir(l1)
exibir(l2)

exibir(l3)
exibir(l4)


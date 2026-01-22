"""
Topic: Introdução à List comprehension
"""

# print(list(range(10)))
lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

# [ resultado / para cada item / no iterável ]
lista = [
    numero * 2
    for numero in range(10)
]
print(lista)
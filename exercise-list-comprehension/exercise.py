"""
Topic: 
"""

# Tabuada de 5 Nível Básico de mapeamento
tabuada = [
    n * 5
    for n in range(1, 11) 
]

print(tabuada)

# Números ao quadrado

numeros = [1, 2, 3, 4, 5]

quadrados = [
    n ** 2
    for n in numeros
]

print(quadrados)

# outra maneira de resolver o execício ao quadrado

number = [
    n ** 2 for n in range(1, 6)
]

print(number)

# Gritos todos os nomes da lista com letra maiúsculas

nomes = ['luiz', 'maria', 'aline']

gritos = [
    nome.upper()
    for nome in nomes
]

print(gritos)

# Apenas pares Nível 2

pares = [    
    n for n in range(21)
    if n % 2 == 0
]

print(pares)

# Nomes curtos 

curtos = [
    nome for nome in nomes
    if len(nome) < 5
]

print(curtos)

# Preços baixos

precos = [1.50, 4.99, 10.00, 85.20, 3.40]

baratos = [
    p for p in precos
    if p < 5
]

promocao = [
    p * 0.9
    if p >= 10 else p for p in precos  
]

print(baratos)
print(promocao)
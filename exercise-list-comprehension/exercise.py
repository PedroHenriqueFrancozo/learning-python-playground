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

quadrado = [
    n ** 2
    for n in numeros
]

print(quadrado)

# Apenas pares Nível 2

pares = [    
    n for n in range(21)
    if n % 2 == 0
]

print(pares)





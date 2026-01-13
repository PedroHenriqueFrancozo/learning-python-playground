"""
Topic: Argumentos nomeados e argumentos posicionais

"""

def soma(x, y):
    # Definição
    print(x + y)

print(soma) # Referência de memória

print(soma(1, 1)) # Por padrão esse print irá retornar None, pois ele não retorna nada
print()


def soma1 (x, y):
    print(f'{x=} y={y}', '|' 'x + y =', x + y )

soma1(2, 3) # Argumento Posicional: A ordem define quem é X e quem é Y.
soma1(y=2, x=3) # Argumento Nomeado: O nome define o alvo, ignorando a ordem.
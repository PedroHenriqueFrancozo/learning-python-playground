"""
Topic: Argumentos nomeados e argumentos posicionais

"""

def soma(x, y):
    # Definição
    print(x + y)

print(soma) # Está referindo ao nome da função

print(soma(1, 1)) # Por padrão esse print irá retornar None, pois ele não retorna nada
print()


def soma1 (x, y):
    print(f'{x=} y={y}', '|' 'x + y =', x + y )

soma1(2, 3) # A ordem do argumento importa dessa forma
soma1(y=2, x=3) # nomenado o argumento
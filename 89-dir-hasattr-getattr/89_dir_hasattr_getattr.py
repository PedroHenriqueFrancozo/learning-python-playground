"""
Topic: Inspeção de Objetos: Dir, Hasattr e getattr
"""

string = 'Pedro'
metodo = 'strip'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)
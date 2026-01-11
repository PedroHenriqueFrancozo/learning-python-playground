"""
Tópico: Manipulando chaves e valores em dicionários
foco:
"""

moto = {}

chave = 'nome', 'ano', 'cc', 'hp', 'valor'

moto['nome'] = 'S1000RR'
moto['cc'] = 1000
moto['hp'] = 200
moto['ano'] = '2016'
moto['valor'] = 65.000

moto['nome'] = 'S1000R'

print(moto)
print(moto['nome'])
 
print()

del moto['valor']
print(moto)

# Gerando keyError
# print(moto['valor'])

print(moto.get('valor', None))
print()

# Outra maneira de utilizar o .get() com if is

if moto.get('valor') is None:
    print('Não Existe')
else:
    print(moto['valor'])

# Trantando erro com try/except

try:
    print(moto['valor'])
except KeyError:
    print('⚠️Aviso: A informção "valor" não está disponível.')
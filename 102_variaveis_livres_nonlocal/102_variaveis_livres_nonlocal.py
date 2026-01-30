"""
Topic:Variáveis livres e nonlocal
"""

def externa(x):
    a = x  # 'a' é uma variável do escopo de 'externa'
    
    def interna():
        # 'a' aqui é uma variável livre, pois interna() 
        # a conhece, mas não a definiu.
        print(a) 
    return interna

funcao = externa(10)
funcao() 

# Utilizando o nonlocal

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
final = c()
print(final)
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
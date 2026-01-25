# 📋 Verificação de tipo com isinstance

Nesta aula, compreendi o uso do `isinstance()` Verifica se um objeto é uma instância de uma classe ou tipo especificado, ou de qualquer uma de suas subclasses. Retorna verdadeiro `True` ou `False`

- **Sintaxe:** `isinstance(object, classinfo)`
    - **object:** O objeto ou variável a ser verificado.
    - **classinfo:** Uma classe, tipo ou tupla de classes/tipos para comparação. 

### 📝 isinstance() vs. type()

1. **isinstance()**
    - Verifica se um objeto pertence a uma classe ou a alguma de suas subclasses (considera herança).
    - Geralmente, essa é a forma preferida de verificação de tipos em Python idiomático, pois promove flexibilidade e polimorfismo no código.

2. **type()**
    - Retorna o tipo de classe exato de um objeto (não considera herança).
    - Útil quando você precisa garantir que um objeto seja de um tipo específico, não pertencente a subclasses.
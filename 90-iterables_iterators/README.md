# ⚙️ Generator expression, Iterables e Iterators

### 1. Iterable (Iterável)
Um objeto é um Iterable se ele possui o método mágico `__iter__`. Ele detém os valores, mas não sabe necessariamente como entregá-los um a um; ele apenas "promete" que pode ser iterado.

- **Exemplos:** Listas, Strings, Tuplas, Dicionários.

### 2. Iterator (Iterador)
Um Iterator é o objeto que realmente faz o trabalho de "dar o próximo passo". Ele é criado a partir de um iterável usando a função `iter()`.

- **Responsabilidade:** Entregar um valor por vez.
- **Mecanismo:** Possui o método `__next__`. Quando os dados acabam, ele levanta a exceção `StopIteration`.

### 3. Generator Expression (Expressão Geradora)
Enquanto uma List Comprehension cria a lista inteira e a joga na memória RAM imediatamente, o Generator não salva nada na memória além da "lógica" de como criar o próximo item.

- **Sintaxe:** Usa parênteses `()` em vez de colchetes `[]`.
- **Vantagem:** Economia extrema de memória. É ideal para lidar com milhões de itens.

# ⚠️ dica:
O `sys.getsizeof()` é uma maneira de **encontrar o consumo de memória atribuida a um único objeto, em bytes**


# ⚡ List Comprehension (Compreensão de Lista)
A List Comprehension é uma forma sintática curta para criar uma nova lista a partir de um iterável (como um `range`, lista ou tupla). Ela é geralmente mais rápida e utiliza menos linhas de código que o comando `append()`.

### 🏗️ Anatomia da List Comprehension
A estrutura básica pode ser dividida em três partes:

- 1. **Expressão (Resultado):** O que será adicionado à lista (Ex: `numero * 2`).
- 2. **Variável:** O nome que representa cada item do ciclo (Ex: `numero`).
- 3. **Iterável:** A fonte dos dados (Ex: `range(10)`).

### 🔄 Comparação: For Tradicional vs. List Comprehension
Ambos os códigos abaixo produzem o mesmo resultado, mas de formas diferentes:

**Método 1:** Laço `for` com `append()`
É o modo manual. Cria uma lista vazia, percorre um intervalo e "empurra" cada item para dentro da lista.

**Método 2:** List Comprehension
É o modo declarativo. Define o que quer (o resultado) diretamente dentro dos colchetes.
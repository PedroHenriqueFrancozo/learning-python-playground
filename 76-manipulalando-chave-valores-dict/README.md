# Aula 76 - Manipulando chaves e valores em dicionários 📝

Nesta aula, aprendi a manipular dicionários após a sua criação. Compreendi que, por serem estruturas mutáveis, é possível **adicionar** novos pares de chave-valor quanto **alterar** valores de chaves já existentes.

### Exemplo prático 🛠️
Desenvolvi um dicionário, realizando a adição e alteração de valores. Pra testar o código, gerei intencionalmente um erro do tipo `KeyError`, o que permitiu explorar o método `.get()`como uma alternativa segura. Além disso, utilizei a estrutura `try/except` para o tratamento de exceções, técnica fundamental para lidar tanto com `KeyError`(em dicionários) quanto com `IndexError` (em lista).

### 📘 Conceitos
O método .get() é a ferramenta para realizar buscas em dicionários. Ele aceita dois argumentos: a **cahve** que queremos buscar e um **valor de retorno opcional**
* **Tratamento de Ausência:** Caso a chave não seja encontrada, o método evita que programa pare, retornando `None` por padrão ou um valor específicado.
* Uma prática comum é combinar o `.get()` com estruturas condicionais (`if/else`). Utilizando os operadores `is None` ou `is not None`, é possível validar a existência do dado antes de processá-lo.
* Garante que o programa não tente acessar diretamente um índice inexistente, eliminando o risco de erros,



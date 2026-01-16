# Aula 82 - Função lambda complexas 📋

Nesta aula, compreendi o uso de Funções de Ordem Superior (Higher-Order Functions). Uma função de ordem superior é aquela que recebe outra função como argumento ou retorna uma função.
Permitindo criar uma estrutura genérica (como a função `executa`) que pode rodar qualquer lógica passada pra ela. E o `*args` é essencial para garantir que a função executadora consiga
repassar qualquer quantidade de argumentos para a função interna.

---

# ⚖️ Lambdas Aninhadas e Closures

As funções Lambda podem retornar outras funções Lambda. Isso cria uma Closure (fechamento), onde a função interna "lembra" do escopo da função externa.

Sintaxe: `duplica = executa(lambda m: lambda n: n * m, 2)`

* A primeira lambda recebe `m` (o multiplicador).
* Ela retorna uma segunda lambda que espera `n` (o número a ser multiplicado).
* O valor de `m` fica "salvo" na memória da função `duplica`.

---

# 🛠️ Flexibilidade com *args em Lambdas

Assim como nas funções definidas com def, as Lambdas também podem aceitar empacotamento de argumentos.

* Sintaxe: `lambda *args: sum(args)`
* Vantagem: Permite processar uma lista dinâmica de valores em uma única linha de código.
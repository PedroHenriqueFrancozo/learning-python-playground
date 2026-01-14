# Aula 68 Escopo de função e módulos 📋

Nesta aula, aprendi que se eu tenho um **escopo fechado** dentro de uma função, o código executado ali dentro não afetará o que está fora em determinados momentos. O **escopo global** é aquele onde todo o código é alcançável (visível). Já o **escopo local** é o ambiente interno de uma função, onde apenas os nomes definidos naquele mesmo local podem ser acessados.

### 📋 O que aprendi / What I learned:

* **Escopo Global:** Variáveis definidas fora de qualquer função. São acessíveis em todo o arquivo. / Variables defined outside any function. Accessible throughout the file.
* **Escopo Local:** Variáveis definidas dentro de uma função. Elas só existem enquanto a função está sendo executada. / Variables defined inside a function. They only exist while the function is running.
* **Palavra-chave `global`:** Permite que uma função altere uma variável que está no escopo global. / Allows a function to modify a variable in the global scope.
* **Hierarquia:** Funções internas podem acessar variáveis de funções externas (escopo de fechamento), mas o inverso não é verdadeiro.
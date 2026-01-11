# Aula 76 - Introdução ao Dicionário 📝

Nasta aula, compreendi a diferença fundamental entre `dicionário` e `lista` principalmente na forma de acesso aos dados.
Enquanto na `lista`o acecsso é feito via índices númericos (0,'1, 2...), o que torna difícil localizar um dado específico em grandes volumes de informação, no `dicionário` utilizamos `chaves` (keys). Isso permite acessar um valor diretamente pelo seu nome (identificador), tornando o código muito mais semântico e eficiente para buscas específicas.

* O valor associado a uma chave pode ser de qualquer tipo, incluindo listas ou outros dicionários (conceito conhecido como **Dicionário Aninhados** ou *Nested Dictionaries*) 
* Assim como as listas, o dicionário é **mutalvel**, podemos adicionar, remover ou alterar valor após a sua criação.
* Para criar um dicionário, utilizamos chaves `{}` ou a classe `dict()`.
* As **chaves** devem ser obrigatoriamente de tipos **imutáveis**(str, int, float, bool, tuple, etc.)
* As operações base consistem em **armazenar** (atribuir valor a uma chave) e **recuperar** acessando os dados posteriormente.
* Tentar accessar uma chave inexistente diretamente levanta `(dicio['chave_fantasma'])` levanta um erro do tipo `KeyError`, Melhor forma de evitar que o programa quebre é usar o método `get()`, que retorna `None` (ou um valor padrão definido).


Estruturas de dados - Documetanção (https://docs.python.org/pt-br/3.14/tutorial/datastructures.html#dictionaries)



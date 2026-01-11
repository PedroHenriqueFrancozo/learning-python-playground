# Aula 76 - Introdução ao Dicionário 📝

Nasta aula, compreendi a diferença fundamental entre `dicionário` e `lista` principalmente na forma de acesso aos dados.
Enquanto na `lista`o acecsso é feito via índices númericos (0,'1, 2...), o que torna difícil localizar um dado específico em grandes volumes de informação, no `dicionário` utilizamos `chaves` (keys). Isso permite acessar um valor diretamente pelo seu nome (identificador), tornando o código muito mais semântico e eficiente para buscas específicas.

O valor pode ser qualquer tipo, incluindo outros dicionários que é chamado de Dicionários alinhados.

Dicionário é mutável igual a lista

É usado as chaves `{},` ou a classe dict para criar dicionários 

Dicionário pode ser de qualquer tipo imutável (str, int, float, bool, tuple, etc.)

Operações em dicionários são armazenar e recuperar valores

No dicionário chave inexistente por meio de um índice levanta `KeyError`, Melhor forma de evitar isso é usando o método `get()`, o método retorna o valor `None`.


Estruturas de dados - Documetanção (https://docs.python.org/pt-br/3.14/tutorial/datastructures.html#dictionaries)



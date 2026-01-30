# 🔗 Variáveis Livres e nonlocal
Este conceito lida com como funções aninhadas (uma dentro da outra) acessam variáveis que não estão no seu escopo local, mas também não são globais.

### 1. O que são Variáveis Livres (Free Variables)?
Uma **variável livre** é uma variável que é usada em um escopo local, mas não foi definida ali. Ela pertence a um escopo "pai" (externo), mas não é global.

### 2. A palavra-chave nonlocal
Por padrão, o Python permite que ler variáveis livres, mas se tentar atribuir um novo valor a elas (ex: a = 2), o Python criará uma nova variável local com o mesmo nome, em vez de alterar a variável da função externa.
O `nonlocal` avisa ao Python: "Não crie uma variável local, use a variável do escopo anterior (não global)".
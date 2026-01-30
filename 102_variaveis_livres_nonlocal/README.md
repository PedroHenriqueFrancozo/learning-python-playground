# 🔗 Variáveis Livres e nonlocal
Este conceito lida com como funções aninhadas (uma dentro da outra) acessam variáveis que não estão no seu escopo local, mas também não são globais.

### 1. O que são Variáveis Livres (Free Variables)?
Uma **variável livre** é uma variável que é usada em um escopo local, mas não foi definida ali. Ela pertence a um escopo "pai" (externo), mas não é global.


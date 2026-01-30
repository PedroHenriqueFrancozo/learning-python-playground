# 🍬 Decoradores: Syntax Sugar (@)
O símbolo `@` seguido do nome da função decoradora é um atalho que o Python oferece para não precisarmos atribuir a função manualmente (ex: `func = decorador(func)`).

### 1. Como o Python lê o @
O interpretador do Python entende: "Pegue a função `inverte_string`, passe-a como argumento para `criar_funcao`, e o que voltar de lá será o novo valor de `inverte_string`".

### 2. A Identidade da Função Decorada
Como você notou ao usar `__name__`, a função original "perde" sua identidade e assume a da função `interna`.

- **Por que isso ocorre?** Porque o decorador literalmente substituiu a função original por uma nova versão "embrulhada".
- **Dica:** Para manter o nome original e a docstring da sua função mesmo após ser decorada, usamos um decorador especial da biblioteca padrão chamado `functools.wraps`.


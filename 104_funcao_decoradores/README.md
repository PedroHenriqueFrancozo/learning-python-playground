# 🍬 Decoradores: Syntax Sugar (@)
O símbolo `@` seguido do nome da função decoradora é um atalho que o Python oferece para não precisarmos atribuir a função manualmente (ex: `func = decorador(func)`).

### 1. Como o Python lê o @
O interpretador do Python entende: "Pegue a função `inverte_string`, passe-a como argumento para `criar_funcao`, e o que voltar de lá será o novo valor de `inverte_string`".
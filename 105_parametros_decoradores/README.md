# 🏭 Fábrica de Decoradores (Decoradores com Parâmetros)
Quando precisamos que o comportamento do decorador mude dependendo de certas configurações (como níveis de acesso, prefixos de log ou multiplicadores), usar uma estrutura de três camadas.

# 1. As Três Camadas de Funções
Para passar parâmetros ao decorador, a estrutura precisa de:

1. A Fábrica: Recebe os parâmetros do decorador (`a, b, c`) e retorna a função decoradora.
2. A Decoradora: Recebe a função original (`func`) e retorna a função executável.
3. A Aninhada (Wrapper): Recebe os argumentos da função original (`*args, **kwargs`), executa a lógica e a função real.

# 2. Por que usar parênteses no @?

- **Sem parâmetros:** O Python passa a função automaticamente.
- **Com parâmetros:** Primeiro chama a fábrica. O resultado dessa chamada (a `fabrica_de_funcoes`) é o que realmente decora a função `soma`.
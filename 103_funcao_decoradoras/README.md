# 📖Funções Decoradoras e Decoradores
Decorar uma função significa **envolvê-la** em uma lógica adicional. 
É como colocar uma moldura em um quadro: o quadro (função original) permanece o mesmo, mas a moldura (decorador) adiciona novos detalhes ao redor dele.

### 1. O que uma Função Decoradora faz?
Ela recebe uma função como parâmetro e retorna uma nova função (geralmente chamada de `interna` ou `wrapper`). Essa função interna:

1. Executa ações antes da função original.
2. Chama a função original usando `*args` e `**kwargs` (para aceitar qualquer argumento).
3. Executa ações depois da função original.
4. Retorna o resultado da função original.


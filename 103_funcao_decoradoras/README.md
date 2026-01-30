# 📖Funções Decoradoras e Decoradores
Decorar uma função significa **envolvê-la** em uma lógica adicional. 
É como colocar uma moldura em um quadro: o quadro (função original) permanece o mesmo, mas a moldura (decorador) adiciona novos detalhes ao redor dele.

### 1. O que uma Função Decoradora faz?
Ela recebe uma função como parâmetro e retorna uma nova função (geralmente chamada de `interna` ou `wrapper`). Essa função interna:

1. Executa ações antes da função original.
2. Chama a função original usando `*args` e `**kwargs` (para aceitar qualquer argumento).
3. Executa ações depois da função original.
4. Retorna o resultado da função original.

### 2. Analisando meu Código
No meu exemplo, a função `criar_funcao` é a **decoradora**. Ela adiciona uma camada de validação e logs:

- Validação: Ela chama e_string(arg) para garantir que ninguém envie números para uma função que inverte strings.
- Logs: Ela imprime mensagens antes e depois da execução.
- Flexibilidade: Ao usar `resultado = func(*args, **kwargs)`, ela garante que não importa quantos argumentos a função original tenha, ela continuará funcionando.


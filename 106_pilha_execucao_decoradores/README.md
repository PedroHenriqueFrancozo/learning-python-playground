# 📚 Múltiplos Decoradores (Empilhamento)
Quando usamos vários decoradores em uma única função, o Python cria uma estrutura aninhada. O decorador mais próximo da função (o de baixo) é o primeiro a "abraçá-la", e o decorador no topo é o último.

### 1. A Ordem de Decoração (Definição)
No momento em que o Python lê o código (antes de chamar `soma`), ele executa as fábricas e os decoradores de baixo para cima:

1. A `soma` é decorada pelo `nome='1'`.
2. O resultado (a nova função) é decorado pelo `nome='2'`.
3. ...e assim por diante até o `nome='5'`.

É por isso que, se olhar o terminal, os `print('Decorador:', nome)` aparecerão na ordem: **1, 2, 3, 4, 5**.

### 2. A Ordem de Execução (Chamada)
Quando finalmente chama soma(10, 5), o processo se inverte. Está chamando a função que o decorador '5' criou. O fluxo de retorno do código específico funciona assim:

1. A função do decorador 5 chama a de baixo e recebe o resultado.
2. Ela pega esse resultado e concatena o seu próprio `nome` ('5').
3. Isso volta subindo a pilha até o final.

O resultado do `print` será: `15 1 2 3 4 5`
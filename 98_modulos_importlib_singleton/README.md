# 🔄 Recarregando Módulos com importlib.reload
Nesta aula, compreendi que o Python importa cada módulo apenas uma vez por sessão. Isso serve para otimizar a performance, mas pode ser um problema se você estiver fazendo alterações em um módulo e quiser testá-las sem reiniciar o programa principal.

### 1. O Comportamento Padrão (Singleton)
Se escrever `import meu_modulo` dez vezes em um laço de repetição, o Python lerá o arquivo na primeira vez e, nas outras nove, apenas usará a versão que já está na memória RAM.

### 2. A Função reload()
A biblioteca padrão `importlib` fornece a função `reload(modulo)`. Ela força o Python a:

1. Ler o arquivo fonte do módulo novamente.
2. Recompilar o código.
3. Atualizar o dicionário do módulo na memória.
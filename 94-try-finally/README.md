# 🏗️ O Ciclo Completo: try, except, else e finally
Enquanto o try e o except cuidam da tentativa e do erro, o else e o finally gerenciam o fluxo de sucesso e a finalização obrigatória.

### 1. A Estrutura de Fluxo

- **try:** "Vou tentar executar este código".
- **except:** "Deu erro? Eu trato o problema aqui".
- **else:** "Não deu erro nenhum? Então execute isto aqui também". (Opcional)
- **finally:** "Não importa o que aconteceu, execute isto ao final". (Opcional)

### 2. Por que usar o finally?
O finally é executado sempre, ocorrendo um erro ou não. Ele é essencial para a liberação de recursos. Imagine que o código abre uma conexão com um banco de dados:

- Se o `try` falhar, é preciso fechar a conexão.
- Se o `try` funcionar, também precisa fechar a conexão. O `finally` garante que você não deixe "lixo" ou conexões penduradas na memória do servidor.
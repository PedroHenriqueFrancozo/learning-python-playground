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

### 3. Por que usar o else?
O bloco `else` serve para separar o código que pode gerar erro (dentro do try) do código que rode apenas se tudo der certo. Isso deixa o try mais limpo e focado apenas na linha perigosa.

# 📝 Resumo de Execução

Situação | `try` | `except` | `else` | `finally`
| :--- | :--- | :--- | :--- | :--- | 
Sem erro | Executa | Pula |	Executa	| Executa
Com erro tratado | Para no erro | Executa | Pula | Executa
Com erro não tratado | Para no erro | Pula | Pula | Executa (depois quebra)

---

### Hierarquia das exceções
https://docs.python.org/pt-br/3.6/library/exceptions.html
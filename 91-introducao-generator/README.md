# 🏗️ Generator Functions (Funções Geradoras)
As Generator Functions são funções que não terminam após retornar um valor. Em vez disso, elas "pausam" sua execução e podem ser retomadas de onde pararam.

### 1. A palavra-chave yield
Diferente do return, que encerra a função e limpa tudo da memória, o yield faz três coisas:

1. **Entrega** o valor atual para quem chamou.
2. **Pausa** a execução da função.
3. **Salva** o estado de todas as variáveis locais.

Quando o próximo valor é solicitado (via `next()` ou um laço `for`), a função continua exatamente da linha logo abaixo do `yield`.

### 2. Por que usar Generator Functions?

- **Eficiência de Memória:** Você pode processar um arquivo de 10GB linha por linha sem precisar carregar os 10GB na RAM de uma vez.
- **Lazy Evaluation (Execução Preguiçosa):** O cálculo só é feito no momento exato em que o valor é necessário.
- **Infinitude:** É possível criar geradores que nunca terminam (como um contador infinito), já que você decide quando parar de pedir valores.


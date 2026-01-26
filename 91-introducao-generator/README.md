# 🏗️ Generator Functions (Funções Geradoras)
As Generator Functions são funções que não terminam após retornar um valor. Em vez disso, elas "pausam" sua execução e podem ser retomadas de onde pararam.

# 1. A palavra-chave yield
Diferente do return, que encerra a função e limpa tudo da memória, o yield faz três coisas:

1. **Entrega** o valor atual para quem chamou.
2. **Pausa** a execução da função.
3. **Salva** o estado de todas as variáveis locais.

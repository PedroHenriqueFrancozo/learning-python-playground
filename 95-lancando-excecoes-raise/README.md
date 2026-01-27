# 🛠️ Lançando Exceções com raise
Diferente do `except` (que captura erros), o `raise` é usado para criar um erro intencionalmente. Ele interrompe a execução da função e envia a exceção para quem a chamou.

### Por que lançar os próprios erros?

- **Validação Antecipada:** Impede que o código continue rodando com dados inválidos.
- **Mensagens Personalizadas:** Pode explicar exatamente o que deu errado, tornando o erro muito mais claro para quem está lendo o log.
- **Consistência:** Garante que as funções recebam apenas os tipos de dados que elas sabem processar.

# 📝 Resumo de Boas Práticas

Regra | Descrição
| :--- | :--- |
Ser Específico	| Usar o erro que melhor descreve o problema (ex: `ValueError` para valores errados, `TypeError` para tipos errados).
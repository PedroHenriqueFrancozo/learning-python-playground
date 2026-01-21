# 📦 Empacotamento e Desempacotamento (Dicionários & Kwargs)
Nesta aula, explorei como o Python lida com a distribuição de valores em variáveis e a passagem de múltiplos argumentos nomeados para funções.

### 1. Desempacotamento de Variáveis e Troca de Valores
O Python permite desempacotar iteráveis de forma direta e realizar a inversão de valores (swap) sem a necessidade de uma variável temporária.

- **Inversão de Valores:** `a, b = b, a` troca os conteúdos das variáveis simultaneamente.
- **Dicionários:** Ao usar `.items()`, podemos desempacotar as tuplas de chave-valor diretamente em variáveis.

### 2. Junção de Dicionários (`**`)
Para criar um novo dicionário a partir de outros existentes, utilizamos o operador de desempacotamento de dicionários `**`

### 3. Funções com *args e **kwargs
Essa combinação permite que uma função seja extremamente flexível, aceitando qualquer tipo e quantidade de entrada.

- `*args` **(Non-keyword arguments):** Captura argumentos posicionais e os armazena em uma Tupla.
- `**kwargs` **(Keyword arguments):** Captura argumentos nomeados e os armazena em um Dicionário.

---

# 📝 Observações:
**Ordem dos Parâmetros:** Na definição de uma função, a ordem correta deve ser: parametros_comuns, `*args`, parametros_padrao, `**kwargs`.
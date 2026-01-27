# 🛡️ Tratamento de Erros: try e except
O bloco `try/except` é a estrutura usada para capturar e tratar erros (exceções) que ocorreriam durante a execução do código, permitindo que o programa continue rodando.

### 1. Funcionamento Básico

- **try:** Você coloca o código que **pode** dar algum erro. O Python tentará executá-lo linha por linha.
- **except:** Se ocorrer um erro dentro do `try`, o Python pula imediatamente para o bloco `except` correspondente. Se não houver erro, os blocos `except` são ignorados.

### 2. Capturando Múltiplas Exceções
Tratar cada erro de uma forma específica:

- **Exceção Única:** `except ZeroDivisionError:` captura especificamente divisões por zero.
- **Múltiplas Exceções em um bloco:** `except (TypeError, IndexError):` trata dois tipos de erro da mesma maneira (usando uma tupla).
- **Classe Base (`Exception`):** O `except Exception:` funciona como um "filtro universal". Ele captura qualquer erro que herde da classe base. **Dica:** Use sempre ao final para evitar que erros desconhecidos derrubem seu sistema.

# 📝 Resumo Técnico: Boas Práticas

Elemento | Função
| :--- | :--- |
`try` | Bloco de código "sob observação".
`except` | tratamento específico para um erro nomeado.
`Exception `| Captura erros genéricos (último recurso).
Fluxo | O código para a execução no try assim que o primeiro erro ocorre.

---

# 🔎 Inspeção e Apelidos para Exceções (`as`)
Ao utilizar a palavra-chave as, cria uma variável que armazena o objeto do erro. Isso dá acesso a detalhes internos da falha que ocorreu.

- **error:** Exibe a mensagem do erro (o que o Python diria no console).
- **error.__class__.__name__:** Retorna apenas o nome da classe da exceção (ex: "IndexError"). É muito útil quando para capturar vários erros no mesmo bloco e quer saber qual deles aconteceu de fato.
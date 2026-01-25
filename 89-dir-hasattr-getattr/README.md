# 🔎 Inspeção de Objetos: Dir, Hasattr e getattr
Nesta aula, compreeidi como verificar em tempo de execução quais atributos e métodos um objeto possui.

### 1. dir() (O Diretório)
A função `dir()` retorna uma lista de strings contendo todos os atributos e métodos disponíveis para aquele objeto (incluindo os métodos "mágicos" do Python, como `__init__`, `__str__`, etc.).

- **Uso:** Excelente para debugar e descobrir o que você pode acessar em um objeto desconhecido.

### Hasattr() (A Verificação)
Verifica se um atributo ou método específico existe.
- **Sintaxe:** `hasattr(objeto, 'nome_do_atributo')`
- **Retorno:** Booleano (`True` ou `False`).
- **Vantagem:** Evita o erro fatal `AttributeError`.


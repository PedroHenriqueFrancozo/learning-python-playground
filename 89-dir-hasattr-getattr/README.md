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

### 3. getattr() (A Captura Dinâmica)
Enquanto o `hasattr` apenas checa, o `getattr()` busca o valor do atributo ou a referência do método para que você possa usá-lo.

- **Sintaxe:** `getattr(objeto, 'nome_do_atributo', default)`

# ⚠️ Dica: 
O `getattr` aceita um terceiro argumento opcional (o default). Se o atributo não existir, em vez de dar erro, ele retorna o que você definiu ali. Ex: `getattr(obj, 'idade', 'Não informada').`
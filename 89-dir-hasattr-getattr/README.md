# 🔎 Inspeção de Objetos: Dir, Hasattr e getattr
Nesta aula, compreeidi como verificar em tempo de execução quais atributos e métodos um objeto possui.

### 1. dir() (O Diretório)
A função `dir()` retorna uma lista de strings contendo todos os atributos e métodos disponíveis para aquele objeto (incluindo os métodos "mágicos" do Python, como `__init__`, `__str__`, etc.).

- **Uso:** Excelente para debugar e descobrir o que você pode acessar em um objeto desconhecido.

### Hasattr() (A Verificação)
A função hasattr() verifica se um objeto possui um atributo ou método específico.
- Usado para inspeção dinâmica de objetos e verificação da existência de atributos, o que previne o `AttributeError` na execução 

- Sintaxe: `hasattr(object, name)`

- **object:** O objeto cujo atributo você deseja verificar.
- **name:** Uma string representando o nome do atributo (ou método) que você deseja verificar. Deve ser uma string

### Valor de retorno
A função retorna um valor **booleano**: 

- `True:` se o atributo com o nome fornecido existir no objeto.
- `False:` se o atributo não existir. 
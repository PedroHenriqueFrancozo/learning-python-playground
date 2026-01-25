# ⚖️ Valores Truthy e Falsy & Tipos de Dados
Nesta aula, compreendi sobre valores truthy (verdadeiros) e falsy (falsos) determinam o comportamento em contextos booleanos (como em um `if` ou `while`).

1. **Valores Falsy**
Um valor é considerado **Falsy** se ele for interpretado como `False` em uma estrutura condicional. Geralmente, são valores "**vazios**" ou "**zerados**".

| Categoria | Exemplos Falsy |
| :--- | :--- |
| Sequências Vazias | `[]` (lista), `{}` (dict), `set()`, `()`, `''` (string) |
| Números | `0`, `0.0` |
| Constantes | `None`, `False` |
| Iteráveis Vazios | `range(0)` |

2. Valores Truthy
Qualquer valor que não seja um dos listados acima é considerado **Truthy**.

- Exemplo: `' '` (uma string com um espaço), `[0]` (uma lista com um item), `1` (número diferente de zero).
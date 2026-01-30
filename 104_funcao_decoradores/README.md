# 🍬 Decoradores: Syntax Sugar (@)
O símbolo `@` seguido do nome da função decoradora é um atalho que o Python oferece para não precisarmos atribuir a função manualmente (ex: `func = decorador(func)`).

### 1. Como o Python lê o @
O interpretador do Python entende: "Pegue a função `inverte_string`, passe-a como argumento para `criar_funcao`, e o que voltar de lá será o novo valor de `inverte_string`".

### 2. A Identidade da Função Decorada
Como você notou ao usar `__name__`, a função original "perde" sua identidade e assume a da função `interna`.

- **Por que isso ocorre?** Porque o decorador literalmente substituiu a função original por uma nova versão "embrulhada".
- **Dica:** Para manter o nome original e a docstring da sua função mesmo após ser decorada, usamos um decorador especial da biblioteca padrão chamado `functools.wraps`.

### 3. Ordem de Execução
O fluxo de uma função decorada segue este caminho:

1. **Chamada:** O usuário chama `inverte_string('123')`.
2. **Entrada no Wrapper:** O código entra na função `interna`.
3. **Pré-execução:** Faz a validação `e_string`.
4. **Execução Real:** A função original (inverter a string) é disparada.
5. **Pós-execução:** O resultado é impresso e retornado.

---

# 📝 Resumo de Conceitos
Termo |	Definição
| :--- | :--- |
**Syntax Sugar** | Uma sintaxe criada para facilitar a escrita e leitura do código (o @).
**Wrapper** | A função `interna` que "envolve" a lógica original.
`*args` e `**kwargs` | Permitem que o decorador funcione com qualquer função, independente do número de parâmetros.
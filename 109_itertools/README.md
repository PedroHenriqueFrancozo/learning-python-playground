# ♾️ Itertools: `count` vs `range`
Embora pareçam similares, o `count` do módulo `itertools` e a função nativa `range` possuem naturezas técnicas diferentes.

### 1. O que é o count?
O `count` é um Iterador que gera números sequenciais indefinidamente. Ele não tem fim, a menos que você force uma parada (como um `break`).

- **Parâmetros:**
    - **start:** O número inicial (padrão é 0).
    - **step:** O intervalo entre os números (padrão é 1).

### 2. Diferença Técnica: Iterável vs Iterador
Usar `hasattr` para checar os métodos mágicos. Aqui está a explicação do resultado:

Objeto | `__iter__` (Iterável) | `__next__` (Iterador) | Natureza
| :--- | :--- | :--- | :--- |
`range` | ✅ Sim | ❌ Não | É um **Iterável**, mas não um iterador (ele não "lembra" onde parou sozinho).
count | ✅ Sim | ✅ Sim | É um **Iterador**. Ele sabe qual é o próximo valor (`next`).

### 3. Comparativo de Comportamento
`range(start, stop, step)`

- **Finito:** Você precisa definir onde ele para (`stop`).
- **Memória:** Muito eficiente, pois calcula os valores sob demanda, mas tem limites claros.
- **Uso:** Quando sabe exatamente o intervalo que precisa percorrer.

`itertools.count(start, step)`

- **Infinito:** Ele continuará gerando números enquanto houver memória ou até o Python atingir o limite de tamanho de inteiros.
- **Lazy Evaluation:** Só gera o próximo número quando solicitado.
- **Uso:** Gerar IDs únicos, índices para elementos de uma lista infinita ou em loops onde a condição de parada depende de um fator externo.

# ⚠️ Cuidado Importante!
Nunca use o `count` em um loop for sem uma condição de parada (`if` + `break`), a menos que sua intenção seja realmente criar um loop infinito. Caso contrário, seu programa travará (congelará) ao tentar consumir algo que nunca termina.

# 📝 Resumo para o seu README

- `count` é um iterador infinito do módulo itertools.
- Ele implementa tanto `__iter__` quanto `__next__`.
- Ao contrário do `range`, ele não aceita um parâmetro de fim (`stop`).
- É ideal para situações onde o limite da iteração não é conhecido de antemão.
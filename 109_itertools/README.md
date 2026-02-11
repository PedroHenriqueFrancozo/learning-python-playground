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
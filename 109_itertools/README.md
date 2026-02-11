# ♾️ Itertools: `count` vs `range`
Embora pareçam similares, o `count` do módulo `itertools` e a função nativa `range` possuem naturezas técnicas diferentes.

### 1. O que é o count?
O `count` é um Iterador que gera números sequenciais indefinidamente. Ele não tem fim, a menos que você force uma parada (como um `break`).

- **Parâmetros:**
    - **start:** O número inicial (padrão é 0).
    - **step:** O intervalo entre os números (padrão é 1).
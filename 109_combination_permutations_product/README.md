# 🎲 Combinatória com itertools
O módulo `itertools` fornece funções otimizadas para gerar sequências matemáticas complexas. As principais diferenças entre elas residem em como tratam a **ordem** dos elementos e a **repetição**.

### 1. `combinations(iterable, r)`
Usada quando a **ordem não importa**.

- Se tivermos (João, Joana), o par (Joana, João) é considerado o mesmo e não será exibido.
- Requer o iterável e o tamanho do grupo (`r`).

### 2. permutations(iterable, r)
Usada quando a **ordem importa**.

- (João, Joana) e (Joana, João) são considerados resultados diferentes.
- Se `r` não for especificado, o padrão é o tamanho total do iterável.

### 3. `product(*iterables, repeat=1)`
Cria o **Produto Cartesiano** entre os iteráveis fornecidos. É o equivalente a usar loops `for` aninhados para combinar tudo com tudo.
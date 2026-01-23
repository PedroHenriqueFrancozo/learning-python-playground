# 🟢 Nível 1: Básico (Mapeamento Simples)Objetivo:

Criar listas a partir de cálculos.

1. **Tabuada do 5:** Crie uma lista que contenha o resultado de 5 multiplicado por cada número de 1 a 10.
2. **Quadrados:** Dada a lista `numeros = [1, 2, 3, 4, 5]`, crie uma nova lista com todos os valores elevados ao quadrado ($n^2$).
3. **Gritos:** Dada a lista `nomes = ['luiz', 'maria', 'aline']`, crie uma nova lista com os nomes todos em letras maiúsculas.

Dica: Pense na List Comprehension como uma frase: "Eu quero isso para cada item na lista" -> `[item * 5 for item in lista`

# 🟡 Nível 2: Filtros (O if no final)
Objetivo: Selecionar apenas o que importa.

1. **Apenas Pares:** Crie uma lista com os números pares de 0 a 20.
2. **Nomes Curtos:** Dada uma lista de nomes, crie uma nova lista que contenha apenas os nomes que possuem menos de 5 letras.
3. **Preços Baixos:** Dada a lista precos = [1.50, 4.99, 10.00, 85.20, 3.40], filtre apenas os valores menores que 5 reais.  Desafio: Imagine que você quer dar um desconto de 10% apenas nos produtos que custam mais de R$ 10,00. Os outros continuam com o preço normal.

# 🟠 Nível 3: Mapeamento Condicional (O `if/else` no início)
Objetivo: Transformar dados baseando-se em uma regra.

1. **Par ou Ímpar:** Crie uma lista que percorra `range(10)`. Se o número for par, coloque a string `'Par'`; se for ímpar, coloque `'Ímpar'`.
2. **Status de Nota:** Dada a lista notas = [8.5, 4.2, 7.0, 3.5, 9.0], crie uma lista que retorne `'Aprovado'` se a nota for >= 7$ e `'Reprovado'` caso contrário.
# 📋List Comprehension: Mapeamento e Lógica
A **List Comprehension** não serve apenas para replicar dados, mas também para transformá-los (mapear) enquanto a lista é criada. 
É uma forma rápida para criar listas a partir de iteráveis.

### 🗺️ Mapeamento de Dados (Map)
No mapeamento, criamos uma nova lista com o mesmo tamanho da original, mas transformamos os valores de cada item.

Usei o desempacotamento de dicionário (`**produto`) para manter os dados originais e alterar apenas a chave `'preco'`.

### 🔀 Condicionais no Mapeamento (Ternário)
Quando queremos aplicar uma lógica de **"Se... senão..."** ao valor que será inserido na lista, usamos a expressão condicional antes do `for`.

**Estrutura:** `[ <VALOR_SE_VERDADEIRO> if <CONDICAO> else <VALOR_SE_FALSO> for item in iteravel ]`

- **Se o preço for > 20:** O produto recebe um aumento de 5%.
- **Caso contrário:** O produto é mantido com os dados originais (**produto).

# 🔍 Diferença entre Mapear e Filtrar
É fundamental saber onde posicionar o if na sua **List Comprehension**:

**Mapeamento (Antes do `for`):** Você usa um `if/else` para decidir qual valor entra na lista. A lista final terá o mesmo tamanho da original.
- Ex: "Aumentar preço de quem for caro, manter de quem for barato".

**Filtro (Depois do `for`):** Você usa apenas o `if` para decidir se o item deve ou não entrar na lista. A lista final pode ser menor que a original.
- Ex: "Criar uma lista apenas com produtos que custam mais de 20 reais".
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
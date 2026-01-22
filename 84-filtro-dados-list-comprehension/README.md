# 🛠️ List Comprehension: Mapeamento + Filtro
Combinamos mapeamento e filtro para conseguir realizar operações complexas em uma única linha, mantendo o código poderoso e conciso.

### 🧩 A Ordem das Peças
Para não confundir a lógica:

- **1. Mapeamento (`if/else` antes do `for`):** Define **O QUE** será o dado (ex: aplicar aumento ou manter o preço).
- **2. Iteração (`for` no meio):** Define **DE ONDE** vêm os dados.
- **3. Filtro (`if` no final):** Define **QUEM** passa para a nova lista.

# 🔍 Dica de Visualização: `pprint`
Você introduziu o módulo `pprint` (Pretty Print). Ele é essencial para:

- Exibir dicionários e listas de forma **identada**.
- Controlar a **largura** da saída (`width=40`).
- Desativar a ordenação automática das chaves (**sort_dicts=False**), mantendo a ordem original que você criou no dicionário.
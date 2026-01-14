# Aula 81 - Introdução à função lambda + list.sort e sorted 📋

Nesta aula, compreendi o uso das **funções lambda**. Elas são funções anônimas (sem nome) que possuem uma sintaxe simplificada, entendi que existem duas formas principais de ordenar dados em Python, cada uma com um comportamento diferente `lista.sort()` e `sorted(lista)`. em caso de dicionario e não possuir maior ou menor, precisamos ensinar o Python a foram como desejamos ordenar a lista 


### 📖 Função Lambda (Funções Anônimas)

* **Estrutura:** Tudo deve ser contido em uma única linha e uma única expressão.
* **Uso ideal:** São excelentes para ações rápidas, como passar uma lógica de ordenação ou filtro para outras funções (como `map`, `filter` e `sort`), sem a necessidade de definir uma função completa com `def`.

### ⚖️ `list.sort()` vs `sorted()`

* `lista.sort():` Altera a lista original. É mais eficiente em memória, mas "destrói" a ordem antiga.
* `sorted(lista):` Retorna uma **nova lista** (cópia rasa), preservando a original intacta.`

### 🛠️ Ensinando o Python a Ordenar

* Dicionários não possuem uma ordem natural de "maior ou menor". Por isso, usamos o parâmetro **key** com uma lambda para extrair o valor que servirá de base para a comparação.
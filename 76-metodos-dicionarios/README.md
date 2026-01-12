# Aula 76 - Métodos úteis dos dicionário 📋

Nesta aula, compreendi a utilização de métodos para manipular pares chaves-valor, além do uso de métodos **Dunder** (como __init__, __str__, __add__). também conhecido como métodos mágicos ou métodos especiais.

Ao utilizar métodos como `.keys()` ou `.items()`, o Python retorna objetos do tipo `dict_keys`, `dict_values` ou `dict_items`. Esses objetos são iteráveis, mas, caso seja necessário, podem ser convertidos para outros tipos de coleções, como `listas` ou `tuplas.`

### Conceitos 🛠️

* 📏 len(): Quantas chaves o dicionário possui.
* 🔑 keys(): Retorna as chaves (útil para loops).
* 💰 values(): Retorna apenas os valores armazenados.
* 📦 items(): Retorna os pares completos (chave e valor).
* 🛡️ get(): Forma segura de acessar um valor sem quebrar o código.
* 🔄 update(): Atualiza o dicionário com novos dados de outro dict ou iterável.
* 📋 copy(): Gera uma cópia rasa (cuidado: objetos aninhados ainda são compartilhados).
* 📌 setdefault(): Garante que uma chave exista com um valor inicial.
* 🗑️ pop(): Remove um item específico e te entrega o valor de volta.
* ⏱️ popitem(): Remove o último item inserido (estratégia LIFO).

---

 ### 💡 Dica

 No método .copy(), existe uma diferença entre Shallow Copy (Cópia Rasa) e Deep Copy (Cópia Profunda).
 * ⚠️ Se o dicionário contiver listas ou outros dicionários dentro dele, o .copy() copiará apenas a referência desses itens. Se você alterar o "clonado", o original também mudará.
 * 💡 Para uma independência total, usar o módulo `copy`.

 ---
 
 ### ✅ Checkpoint de Aprendizado

* [x] Diferença entre Lista e Dicionário (Índice vs Chave)
* [x] Adicionar, Alterar e Deletar (`del`)
* [x] Uso do `.get()` para evitar `KeyError`
* [x] Uso do `setdefault()` para garantir uma chave com valor padrão (sem sobrescrever caso ela já exista).
* [x] Iteração com `.items()`
* [x] Diferença entre Shallow e Deep Copy
# Aula 67 - Valores padrão para parâmetros em funções. 📋

Ao definir uma função, os parâmetros podem ter valores padrão. Caso nenhum valor seja enviado para um parâmetro específico durante a chamada da função, esse valor padrão será automaticamente utilizado.

### 📝 O uso de None como "Não-Valor" 

É uma prática muito comum definir o valor padrão de um parâmetro como `None`. Isso é feito para representar um "não-valor" ou um estado de "valor não fornecido". Usar `None` é preferível a usar `0` ou strings vazias, pois evita confusões lógicas (por exemplo, quando o usuário realmente deseja passar o número `0` como um dado válido).
Definir o padrão como `None` permite realizar verificações seguras dentro da função utilizando os operadores `is` ou `is not`.

### ⚠️ Regra importante: 
* Todo parâmetro que possui um valor padrão deve vir depois dos parâmetros que não possuem. Parâmetros sem padrão não podem "vir depois" de parâmetros com padrão.
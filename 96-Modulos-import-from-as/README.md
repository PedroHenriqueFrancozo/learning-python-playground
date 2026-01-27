# 📦 Módulos Padrão do Python (import)
Módulos são arquivos contendo definições e instruções Python que podem ser reaproveitados em outros programas.

### 1. Importação Inteira (import modulo)
Traz o módulo completo. Para usar algo dele, deve usar o prefixo modulo.objeto.

- **Vantagem:** Evita conflitos. Você sabe exatamente de onde vem cada função.
- **Desvantagem:** O código pode ficar extenso se o nome do módulo for grande.

### 2. Importação de Partes (from modulo import objeto)
Traz apenas o que precisa diretamente para o seu código.

- **Vantagem:** Sintaxe mais curta e limpa.
- **Desvantagem:** Pode causar conflito de nomes se você já tiver uma variável com o mesmo nome no seu arquivo.
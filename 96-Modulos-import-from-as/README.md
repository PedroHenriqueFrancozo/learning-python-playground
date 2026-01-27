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

### 3. Uso de Alias / Apelidos (as)
Permite renomear o módulo ou o objeto importado dentro do seu arquivo.

- **Aliasing do Módulo:** `import sys as s`
- **Aliasing do Objeto:** `from sys import platform as pf`
- **Vantagem:** Resolve conflitos de nomes e encurta comandos.
- **Cuidado:** Use apelidos intuitivos (ex: `pd` para `pandas`, `np` para `numpy`) para não confundir outros programadores.

### 4. Má Prática: O Wildcard (from modulo import *)
Importa todos os objetos do módulo de uma vez.

- **Por que evitar?** Polui o código com centenas de nomes que não conhece, podendo sobrescrever as próprias funções sem perceber. Além disso, torna o código difícil de ler (Não sabe de onde veio a função x()).

# 📝 Resumo de Estilos de Importação

Comando | Como usar	| Recomendação
| :--- | :--- | :--- |
`import sys` | `sys.platform` | Melhor para clareza
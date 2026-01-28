# 🏗️ Modularização: Criando Os Próprios Módulos
Modularizar é o ato de dividir seu programa em vários arquivos. Isso facilita a manutenção, o reuso de código e a legibilidade.

### 1. O Módulo Especial __main__
O primeiro arquivo que você executa no Python é sempre batizado internamente como `__main__`.

- Se imprimir print(__name__) no arquivo que deu "Play", o resultado será __main__.
- Se esse arquivo importar outro (ex: modularizacao97_m), o nome impresso dentro de modularizacao97_m será o nome do próprio arquivo.

### 2. Onde o Python Procura os Módulos? (sys.path)
O Python não sai procurando arquivos em todo o seu computador. Ele segue uma lista de caminhos chamada `sys.path`.

- **Pasta Atual:** O local onde o arquivo __main__ está.
- **Pastas Abaixo:** Subpastas da pasta atual (pacotes).
- **Built-ins:** Pastas onde o Python está instalado.
- ⚠️ **Limitação:** Por padrão, o Python não olha para pastas acima do arquivo que iniciou a execução.

### 3. Singleton de Módulos
Uma característica importante do Python é que ele importa o módulo apenas uma vez por execução, mesmo que escreva `import modulo` dez vezes. Isso é eficiente porque evita que o código do módulo seja reexecutado desnecessariamente.

### 4. Boas Práticas na Criação de Módulos

- **Nomes:** Use letras minúsculas e underscores (ex: meu_modulo.py).
- **Código Executável:** Evite colocar códigos que rodam imediatamente (como print) dentro de módulos, a menos que seja estritamente necessário. O ideal é que módulos contenham definições (funções e classes).

# 📝 Resumo de Comportamento
Termo | Significado
| :--- | :--- |
`__name__` | Variável que guarda o nome do módulo.
`__main__` | Nome do módulo que está sendo executado diretamente.
`sys.path` | Lista de diretórios onde o Python busca o que você importou.
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

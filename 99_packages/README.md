# 📦 Packages (Pacotes) e o uso do __all__
Um Package em Python nada mais é do que uma pasta que contém múltiplos módulos. Isso permite agrupar funcionalidades relacionadas de forma organizada.

### 1. Formas de Importar de um Pacote
Existem três maneiras principais de acessar um módulo dentro de um pacote, cada uma alterando o **namespace** (como você chama a função):

- Importando o caminho completo: import aula99_package.modulo
    - Uso: exemplo_99_packages.packages.soma_do_modulo()

- Importando o módulo do pacote: from aula99_package import modulo
    - Uso: packages.soma_do_modulo()

- Importando os objetos diretamente: from aula99_package.modulo import soma_do_modulo
    - Uso: soma_do_modulo()

### 2. O Controle Especial com __all__
Quando usar o "wildcard" (**from modulo import ***), o Python importa tudo o que não começa com underline (_). No entanto, pode restringir ou definir exatamente o que será exportado usando a variável global __all__ dentro do módulo.

- **Vantagem:** Evita que variáveis internas ou imports auxiliares de dentro do módulo "poluam" o arquivo de quem está importando.
- **Nota:** O `__all__` só afeta o comportamento do `import *`. Se você importar especificamente o nome, ele funcionará normalmente.

---

# 📝 Resumo Técnico

Método de Importação | Sintaxe de Uso | Recomendação
| :--- | :--- | :--- |
`import pacote.modulo` | `pacote.modulo.func()` | Mais seguro (evita qualquer conflito).
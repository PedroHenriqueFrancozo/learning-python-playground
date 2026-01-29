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
# 📋 Geradores: O comando `yield from`
O `yield from` é utilizado para delegar a iteração de um gerador para outro sub-gerador (ou qualquer iterável). Ele funciona como um "atalho" para repassar valores de uma fonte externa diretamente para quem está consumindo o gerador principal.

### 1. Delegação de Iteração
Em vez de escrever um laço manual para extrair valores de um gerador dentro de outro, usamos o yield from.

### 2. Anatomia do Código Estudado
A função `gen2` age como um **gerador mestre** que decide se deve ou não incluir valores de outro gerador antes de seguir com sua própria sequência.

- **Flexibilidade:** Ao passar `gen1()` ou `gen3()` como argumento, `gen2` consome todos os valores do gerador enviado antes de entregar os números `4, 5, 6`.
- **Tratamento de None:** O código prevê o caso em que nenhum gerador é passado (`gen=None`), garantindo que o `yield from` não seja executado em um objeto não iterável.

# 📝 Resumo Técnico: Vantagens do `yield from`

Vantagem | Descrição
| :--- | :--- |
Legibilidade | Elimina a necessidade de laços `for` aninhados dentro de geradores.
Composição | Facilita a união de múltiplos geradores em uma única sequência lógica.
Transparência | Além de valores, ele também lida com o envio de exceções e valores via `.send()` (conceitos avançados de corrotinas).
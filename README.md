# Atividade-LP-09-11

Aluno: Roger Vinícius Pereira Augusto

Explicação das Escolhas:

- Herança e Especialização de Instrumentos: As classes Guitarra, Baixo, e Violao herdam de Instrumento para modelar as peculiaridades e informações diferenciadas de cada instrumento "a partir da minha imaginação" (não conhecia essas particularidades dos intrumentos).

- Associação (Loja - Funcionario): Cada Funcionario está associado a uma Loja, mas ele pode ser remanejado. A classe Loja pode adicionar e remover funcionários.

- Composição (Loja - Instrumento): Os instrumentos fazem parte do estoque da Loja. Se uma loja é removida, os instrumentos deixam de existir junto com ela.

- Agregação (Loja - Loja): Cada Loja pode ter uma referência para a loja mais próxima. Essa relação é de proximidade, sem dependência.
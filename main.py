"""
Driver code que testa as funcionalidades implementadas.
"""

from loja import Loja
from funcionario import Funcionario
from instrumento import Guitarra, Baixo, Violao

# Criação de lojas
loja_sp = Loja("Santos")
loja_rj = Loja("Bonsucesso")
loja_rj.loja_mais_proxima = loja_sp  # Agregação

# Criação de funcionários
funcionario1 = Funcionario("Roger", "123.456.789-10", 3000, "Vendedor")
funcionario2 = Funcionario("Tokao", "111.222.333-44", 6000, "Gerente")

# Adição de funcionários à loja
loja_rj.adicionar_funcionario(funcionario1)
loja_rj.adicionar_funcionario(funcionario2)

# Criação de instrumentos
guitarra1 = Guitarra("Fender", "Stratocaster", 7000, 6)
baixo1 = Baixo("Ibanez", "SR300", 3500, 4)
violao1 = Violao("Yamaha", "C40", 800, 6)

# Adição de instrumentos ao estoque da loja
loja_rj.adicionar_instrumento(guitarra1)
loja_rj.adicionar_instrumento(baixo1)
loja_rj.adicionar_instrumento(violao1)

# Teste de funcionalidades
print("Estoque de instrumentos em Bonsucesso:", loja_rj.consultar_estoque())
print("Funcionários por cargo em Bonsucesso:", loja_rj.consultar_funcionarios_por_cargo())

# Remoção de um funcionário e um instrumento
# Remove os últimos que foram adicionados, pois a remoção está sendo feita com pop
loja_rj.remover_funcionario()
loja_rj.remover_instrumento()

print("Estoque após remoção de um instrumento:", loja_rj.consultar_estoque())
print("Funcionários por cargo após remoção:", loja_rj.consultar_funcionarios_por_cargo())

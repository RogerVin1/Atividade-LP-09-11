class Funcionario:
    def __init__(self, nome, documento, salario, cargo):
        self.nome = nome
        self.documento = documento
        self.salario = salario
        self.cargo = cargo
        self.loja_atual = None  # Associação com a loja

class Loja:
    def __init__(self, localizacao):
        self.localizacao = localizacao
        """
        Funcionários e estoque foram declarados como lista, pois uma loja pode ter vários funcionários, 
        assim como o estoque de uma loja pode conter vários instrumentos de diferentes tipos, 
        ficando mais fácil de serem manipulados ao serem colocados em forma de lista
        """ 
        self.funcionarios = []  # Associação com funcionários
        self.estoque = []       # Composição com instrumentos
        self.loja_mais_proxima = None  # Agregação com outra loja
    
    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
        funcionario.loja_atual = self
    
    def remover_funcionario(self):
        if self.funcionarios:
            funcionario = self.funcionarios.pop()
            funcionario.loja_atual = None
    
    def adicionar_instrumento(self, instrumento):
        self.estoque.append(instrumento)
    
    def remover_instrumento(self):
        if self.estoque:
            self.estoque.pop()
    
    def consultar_estoque(self):
        contagem = {'Guitarra': 0, 'Baixo': 0, 'Violao': 0}
        for instrumento in self.estoque:
            contagem[instrumento.tipo] += 1
        return contagem
    
    def consultar_funcionarios_por_cargo(self):
        contagem_cargos = {}
        for funcionario in self.funcionarios:
            cargo = funcionario.cargo
            contagem_cargos[cargo] = contagem_cargos.get(cargo, 0) + 1
        return contagem_cargos


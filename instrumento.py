class Instrumento:
    def __init__(self, marca, modelo, preco, numero_cordas, tipo):
        self.marca = marca
        self.modelo = modelo
        self.preco = preco
        self.numero_cordas = numero_cordas
        self.tipo = tipo

class Guitarra(Instrumento):
    def __init__(self, marca, modelo, preco, numero_cordas, tipo='Guitarra'):
        super().__init__(marca, modelo, preco, numero_cordas, tipo)
        self.captador = "humbucker"

class Baixo(Instrumento):
    def __init__(self, marca, modelo, preco, numero_cordas, tipo='Baixo'):
        super().__init__(marca, modelo, preco, numero_cordas, tipo)
        self.num_trastes = 20

class Violao(Instrumento):
    def __init__(self, marca, modelo, preco, numero_cordas, tipo='Violao'):
        super().__init__(marca, modelo, preco, numero_cordas, tipo)
        self.cordas = "nylon"
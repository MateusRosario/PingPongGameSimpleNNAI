class Controle_player:
    def __init__(self, direita, esquerda):
        self.direita = direita
        self.esquerda = esquerda

    def dir(self, key):
        return True if key == self.direita else False

    def esq(self, key):
        return True if key == self.esquerda else False
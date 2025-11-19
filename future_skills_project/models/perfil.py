class Perfil:
    def __init__(self, nome, competencias):
        self.nome = nome
        self.competencias = competencias

    def __str__(self):
        return f"Perfil de {self.nome}: {self.competencias}"

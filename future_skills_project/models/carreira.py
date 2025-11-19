class Carreira:
    def __init__(self, nome, requisitos):
        self.nome = nome
        self.requisitos = requisitos

    def calcular_match(self, competencias_perfil):
        score = 0
        for comp, req in self.requisitos.items():
            if competencias_perfil.get(comp, 0) >= req:
                score += 1
        return score

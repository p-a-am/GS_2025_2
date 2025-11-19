from data.carreiras import carreiras

class Recomendador:
    def recomendar(self, perfil):
        print("\n===== Recomendações para", perfil.nome, "=====\n")

        ranking = []

        for carreira in carreiras:
            match = carreira.calcular_match(perfil.competencias)
            ranking.append((carreira.nome, match))

        ranking.sort(key=lambda x: x[1], reverse=True)

        for nome, score in ranking:
            print(f"{nome} — Compatibilidade: {score}/3")

        print("\nÁreas para aprimoramento:")
        for comp, nivel in perfil.competencias.items():
            if nivel < 5:
                print(f"- {comp} (nível {nivel}) — precisa melhorar")

from models.perfil import Perfil
from services.recomendador import Recomendador

def menu():
    print("\n===== Future Skills Lab – Orientador de Carreira =====")
    print("1. Criar perfil")
    print("2. Ver recomendações")
    print("3. Sair")

def main():
    perfil = None
    recomendador = Recomendador()

    while True:
        menu()
        opc = input("\nEscolha uma opção: ")

        if opc == "1":
            nome = input("Seu nome: ")
            print("\nAvalie suas competências de 0 a 10:")
            competencias = {
                "logica": int(input("Lógica: ")),
                "criatividade": int(input("Criatividade: ")),
                "colaboracao": int(input("Colaboração: ")),
                "adaptabilidade": int(input("Adaptabilidade: "))
            }

            perfil = Perfil(nome, competencias)
            print("\n✔ Perfil criado com sucesso!")

        elif opc == "2":
            if perfil is None:
                print("\n⚠ Crie um perfil antes!")
            else:
                recomendador.recomendar(perfil)

        elif opc == "3":
            print("\nEncerrando...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

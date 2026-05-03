from fibonacci import gerar_sequencia, termo
from utils import salvar_em_arquivo, mostrar_estatisticas


def menu():
    print("\n=== Fibonacci Toolkit ===")
    print("1 - Gerar sequência")
    print("2 - Calcular termo específico")
    print("3 - Estatísticas")
    print("4 - Salvar sequência")
    print("0 - Sair")


def main():
    seq = []

    while True:
        menu()
        opcao = input("Escolha: ")

        if opcao == "1":
            n = int(input("Quantos termos? "))
            seq = gerar_sequencia(n)
            print("Sequência:", seq)

        elif opcao == "2":
            n = int(input("Qual termo? "))
            print("Resultado:", termo(n))

        elif opcao == "3":
            stats = mostrar_estatisticas(seq)
            print("Estatísticas:", stats)

        elif opcao == "4":
            nome = input("Nome do arquivo: ")
            salvar_em_arquivo(nome, seq)
            print("Salvo com sucesso!")

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
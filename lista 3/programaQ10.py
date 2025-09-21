import operacoes

def menu():
    print("\n=== MENU DE OPERAÇÕES ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

while True:
    menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "0":
        print("Saindo do programa. Até mais!")
        break

    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    if escolha == "1":
        print("Resultado:", operacoes.soma(a, b))
    elif escolha == "2":
        print("Resultado:", operacoes.subtracao(a, b))
    elif escolha == "3":
        print("Resultado:", operacoes.multiplicacao(a, b))
    elif escolha == "4":
        print("Resultado:", operacoes.divisao(a, b))
    else:
        print("Opção inválida! Tente novamente.")

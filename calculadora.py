print("INICIANDO CALCULADORA")

def soma():
    calc_soma = (n1 + n2)
    print(f"Resultado: {calc_soma}")
    return

def multi():
    calc_multi = (n1 * n2)
    print(f"Resultado: {calc_multi}")
    return

def sub():
    calc_sub = (n1 - n2)
    print(f"Resultado: {calc_sub}")
    return

def div():
    calc_div = (n1 / n2)
    print(f"Resultado: {calc_div}")
    return

while True:
    print("\nMódulos")
    print("\n0 - SOMA")
    print("\n1 - SUBTRAÇÃO")
    print("\n2 - MULTIPLICAÇÃO")
    print("\n3 - DIVISÃO")

    escolha = int(input("\nESCOLHA UM MÓDULO: "))

    if escolha == 0:
        print("Método + escolhido")
        n1 = int(input("Digite primeiro número: "))
        n2 = int(input("Digite segundo número: "))
        soma()


    elif escolha == 1:
        print("Método - escolhido")
        n1 = int(input("Digite número Minuendo: "))
        n2 = int(input("Digite número Subtraendo: "))
        print(f"{n1} - {n2}")
        sub()


    elif escolha == 2:
        print("Método * escolhido")
        n1 = int(input("Digite número multiplicando: "))
        n2 = int(input("Digite número multiplicador: "))
        print(f"{n1} * {n2}")
        multi()

    elif escolha == 3:
        print("Método / escolhido")
        n1 = int(input("Digite número Dividendo: "))
        n2 = int(input("Digite número Divisor: "))
        print(f"{n1} / {n2}")
        div()

    else:
        print("Módulo ainda não implementado!")

    # Pergunta se quer continuar
    continuar = input("\nDeseja realizar outra operação? (S/N): ").strip().upper()
    if continuar != "S":
        print("Encerrando a calculadora...")
        break
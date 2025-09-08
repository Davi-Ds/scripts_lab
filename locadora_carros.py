#criar um script em pythohn para locação de carros
print("===================")
print("\nBem vindo à locadora de carros do Bender!")
print("\n===================")


# Dicionário de carros

carros = {
    "Toyota Corolla": {
        "ano": 2022,
        "cor": "Prata",
        "motor": "2.0",
        "preço": 120000
    },
    "Honda Civic": {
        "ano": 2021,
        "cor": "Preto",
        "motor": "1.5 Turbo",
        "preço": 130000
    },
    "Chevrolet Onix": {
        "ano": 2023,
        "cor": "Branco",
        "motor": "1.0 Turbo",
        "preço": 85000
    }
}
alugados = []
disponiveis = list(carros.keys())

while True:
    print("\nO que deseja fazer?")
    print ("\n0 - Mostrar portifólio de carros | 1 - Alugar carros | 2 - Devolver carros")
    print("")

    escolha = int(input("\nDigite sua opção: "))
    
    
    # Mostrar portfólio
    if escolha == 0:
        print("\n=== Portfólio de Carros ===")
        i = 1
        for modelo in carros:
                print(f"{i}- {modelo}")
                i += 1
        continue


    if escolha == 1:
          if not disponiveis:
            print("\nNenhum carro disponível para aluguel no momento.")
            continue
          
          print("\n=== Carros Disponíveis ===")
          for i, modelo in enumerate(disponiveis, start=1):
            print(f"{i} - {modelo}")


    # Solicitar escolha do usuário
    escolha = int(input("\nSelecione o número do modelo: "))

    # Validar e exibir detalhes do carro escolhido
    if 1 <= escolha <= len(disponiveis):
        modelo = disponiveis[escolha - 1]  # pega o carro pelo índice
        alugados.append(modelo)  # adiciona à lista de alugados
        print(f"\nVocê escolheu: {modelo}")
        print("Detalhes:")
        for chave, valor in carros[modelo].items():
            print(f"  {chave}: {valor}")
    else:
        print("Opção inválida. Tente novamente.")
    


    #Devolver carros alugados pelo usuario
    if escolha == 2:
        if not alugados:
            print("\nVocê não possui carros para devolver.")
            continue

        print("\n=== Seus carros alugados ===")
        for i, modelo in enumerate(alugados, start=1):
            print(f"{i}. {modelo}")

        escolha_devolver = int(input("\nSelecione o número do carro para devolver: "))

        if 1 <= escolha_devolver <= len(alugados):
            modelo = alugados.pop(escolha_devolver - 1)  # remove da lista de alugados
            print(f"\nVocê devolveu o carro: {modelo}")
        else:
            print("Opção inválida.")

        continuar = input("\nDeseja realizar outra operação? (S/N): ").strip().upper()
        if continuar != "S":
            print("\nA locadora de carros do Bender agradece sua preferência!")
            break
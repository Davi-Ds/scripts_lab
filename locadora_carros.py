# -*- coding: utf-8 -*-

print("===================")
print("\nBem-vindo à locadora de carros do Bender!")
print("\n===================")

# Dicionário de carros
carros = {
    "Toyota Corolla": {"ano": 2022, "cor": "Prata", "motor": "2.0", "preço": 120000},
    "Honda Civic": {"ano": 2021, "cor": "Preto", "motor": "1.5 Turbo", "preço": 130000},
    "Chevrolet Onix": {"ano": 2023, "cor": "Branco", "motor": "1.0 Turbo", "preço": 85000},
}

# Listas de controle
disponiveis = list(carros.keys())
alugados = []

def mostrar_portfolio():
    print("\n=== Portfólio de Carros ===")
    for i, modelo in enumerate(carros.keys(), start=1):
        print(f"{i} - {modelo}")
        print("\n===========================")

def listar_disponiveis():
    if not disponiveis:
        print("\nNenhum carro disponível para aluguel no momento.")
        return False
    print("\n=== Carros Disponíveis ===")
    for i, modelo in enumerate(disponiveis, start=1):
        print(f"{i} - {modelo}")
        print("\n===========================")
    return True

def detalhar(modelo):
    print(f"\nVocê selecionou: {modelo}")
    print("Detalhes:")
    for k, v in carros[modelo].items():
        print(f"  {k}: {v}")
        print("\n===========================")

def alugar_carro():
    if not listar_disponiveis():
        return
    else:
        escolha = int(input("\nSelecione o número do modelo para ALUGAR: "))
        if 1 <= escolha <= len(disponiveis):
            modelo = disponiveis.pop(escolha - 1)
            detalhar(modelo)
            alugados.append(modelo)
            print(f"\n {modelo} foi alugado com sucesso!")
            print("\n===========================")
        else:
            print("Opção inválida.")

def devolver_carro():
    if not alugados:
        print("\n(Nenhum carro alugado no momento.)")
        return
    print("\n=== Seus carros alugados ===")
    for i, modelo in enumerate(alugados, start=1):
        print(f"{i} - {modelo}")
        print("\n===========================")
    else:
        escolha = int(input("\nSelecione o número do carro para DEVOLVER: "))
        if 1 <= escolha <= len(alugados):
            modelo = alugados.pop(escolha - 1)
            disponiveis.append(modelo)
            print(f"\n Você devolveu o carro: {modelo}")
            print("\n===========================")
        else:
            print("Opção inválida.")


# Loop principal
while True:
    print("\nO que deseja fazer?")
    print("0 - Mostrar portfólio de carros")
    print("1 - Alugar carros")
    print("2 - Devolver carros")
    print("3 - Sair")
          

    escolha = int(input("\nDigite sua opção: "))

    if escolha == 0:
        mostrar_portfolio()
    elif escolha == 1:
        alugar_carro()
    elif escolha == 2:
        devolver_carro()
    elif escolha == 3:
        print("\nA locadora de carros do Bender agradece sua preferência!")
        break
    else:
        print("Opção inválida.")

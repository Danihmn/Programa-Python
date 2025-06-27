print("Lanchonete")

# Catálogo
print("1 - Coxinha R$ 5,00")
print("2 - Pastel R$ 7,00")
print("3 - Café R$ 4,00")
print("4 - Suco R$ 6,00")
print("5 - SAIR")

total = 0 # Total a ser pago

while True:
    # Selecionando opções
    opcao = int(input("Qual item gostaria de comprar? "))

    # Verifica a opção escolhida
    if opcao == 1:
        quantidade = int(input(" Quantas unidades deseja comprar? "))
        total = total + quantidade * 5
    elif opcao == 2:
        quantidade = int(input(" Quantas unidades deseja comprar? "))
        total = total + quantidade * 7
    elif opcao == 3:
        quantidade = int(input(" Quantas unidades deseja comprar? "))
        total = total + quantidade * 4
    elif opcao == 4:
        quantidade = int(input(" Quantas unidades deseja comprar? "))
        total = total + quantidade * 6
    elif opcao == 5:
        break
    else:
        print("Produto inválido, selecione outro")
        continue

# Exibe
print(f"O total a ser pago é de R${total}")
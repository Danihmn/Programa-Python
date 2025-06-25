# Entrada de dados
kwh = float(input("Quantos kWh? "))
tipo = input("Qual o tipo da instalação? (R, C ou I) ")
preco = 0 # Declara preco como 0 para poder ser implementado depois

# Verifica o tipo da instalação e a quantidade de kWh
if tipo == "R":
    if kwh > 500:
        preco = 0.65
    else:
        preco = 0.45
elif tipo == "C":
    if kwh > 1000:
        preco = 0.6
    else:
        preco = 0.55
elif tipo == "I":
    if kwh > 5000:
        preco = 0.6
    else:
        preco = 0.55
else:
    print("Tipo inválido")

# Exibe
print(f"Total a pagar: {kwh * preco}")
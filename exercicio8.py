print("Sacar dinheiro") # Título

# Recebe o valor
valor = int(input("Digite o valor que deseja sacar: "))

# Verifica o valor e vai dividindo
while valor >= 100:
    notas100 = valor // 100
    valor = valor - notas100 * 100
    print(f"{notas100} notas de 100 reais")

while valor >= 50:
    notas50 = valor // 50
    valor = valor - notas50 * 50
    print(f"{notas50} notas de 50 reais")

while valor >= 20:
    notas20 = valor // 20
    valor = valor - notas20 * 20
    print(f"{notas20} notas de 20 reais")

while valor >= 10:
    notas10 = valor // 10
    valor = valor - notas10 * 10
    print(f"{notas10} notas de 10 reais")

while valor >= 5:
    notas5 = valor // 5
    valor = valor - notas5 * 5
    print(f"{notas5} notas de 5 reais")

if valor:
    moeda1 = valor
    print(f"{moeda1} moedas de 1 real")
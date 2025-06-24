km_rodados = int(input("Quantos quilômetros foram percorridos?"))
qnt_dias = int(input("Quantos dias foram percorridos?"))
preco = 60 * qnt_dias + 0.15 * km_rodados # Calculo de preço

# Exibe
print(f"Quilômetros rodados: {km_rodados}")
print(f"Dias percorridos: {qnt_dias}")
print(f"Valor a pagar: {preco} reais")
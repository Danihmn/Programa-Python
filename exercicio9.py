# Variáveis a serem implementadas
total_pessoas = 0
dinheiro = 0
idade_acumulada = 0 # Valor que será incrementado

while True:
    idade = int(input("Qual a sua idade? ")) # Entrada

    # Se a idade for 0 ou menor, encerra
    if idade <= 0:
        break

    # A cada resposta, incrementa o total de pessoas
    total_pessoas += 1
    idade_acumulada += idade # Incrementa em idades a idade da entrada

    # Calcula os preços por idades
    if idade < 3:
        ingresso = 0
    elif idade > 12:
        ingresso = 30
    else:
        ingresso = 15

    # Incrementa no valor do dinheiro o valor do ingresso
    dinheiro += ingresso

# Faz a média de idades
media = idade_acumulada // total_pessoas

# Exibe
print(f"Total de pessoas: {total_pessoas}")
print(f"Total arrecadado: {dinheiro}")
print(f"Média de idades: {media}")
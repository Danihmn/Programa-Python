preco = float(input("Digite o valor do produto")) # Pede o valor do produto
percentual = float(input("Digite a porcentagem de desconto (0 - 100)")) # Pede o percentual de desconto

calculo_desconto = (percentual / 100) * preco # Calcula
valor_final = preco - calculo_desconto # Tira o valor de desconto

# Exibe
print(f"O valor do produto é de {preco}, desconto de {percentual}")
print(f"O valor final do produto é de {valor_final}")
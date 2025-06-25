# Interface da calculadora
print("Calculadora")
print("+ - Adição")
print("- - Subtração")
print("* - Multiplicação")
print("/ - Divisão")
print("Pressione qualquer outra tecla para sair")

operador = input("Qual a operação desejada? ") # Operador

# Valores
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
resultado = 0

# Verifica qual o operador e faz as contas
if operador == "+":
    resultado = valor1 + valor2
elif operador == "-":
    resultado = valor1 - valor2
elif operador == "*":
    resultado = valor1 * valor2
elif operador == "/":
    resultado = valor1 / valor2
else:
    print("Encerrando o programa") # Encerra

# Exibe a conta
print(f"O resultado é igual a {resultado}")
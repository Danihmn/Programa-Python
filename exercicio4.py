# Recebe os três lados do triângulo
lado1 = int(input("Digite o valor do lado 1 do triângulo: "))
lado2 = int(input("Digite o valor do lado 2 do triângulo: "))
lado3 = int(input("Digite o valor do lado 3 do triângulo: "))

# Nenhum lado pode ser menor ou igual a 0
if lado1 > 0 and lado2 > 0 and lado3 > 0:
    # Nenhum lado pote ter o valor maior que a soma dos outros dois lados
    if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado3 + lado1 > lado2:
        # Se o programa chegou aqui, é porque o triângulo é válido
        if lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
            print("Triângulo escaleno")
        elif lado1 == lado2 and lado2 == lado3:
            print("Triângulo equilátero")
        else:
            print("Triângulo isósceles")
    else:
        print("Nenhum lado pote ter o valor maior que a soma dos outros dois lados")
else:
    print("Nenhum lado deve ser menor ou igual a 0")
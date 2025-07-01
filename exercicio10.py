def fatorial(numero):
    """
    fatorial => Calcula o fatorial de um valor
    numero: valor numérico a ser passado
    """

    fatorial = 1  # Inicia como 1

    if numero == 0:
        return fatorial  # Retorna 1 pois o fatorial de 0 é 1

    # Loop que repetirá na x vezes, dependendo do valor passado
    for i in range(1, numero + 1, 1):
        fatorial *= i  # Multiplica o fatorial por 1 e vai o incrementando

    return fatorial


def verifica_numero(solicitacao, minimo, maximo):
    """
    verifica_numero => Verifica se o valor é apropriado para o cálculo
    solicitacao: pergunta do usuário
    minimo: valor numérico
    maximo: valor numérico
    """

    pedido = int(input(solicitacao))

    while (pedido < minimo) or (pedido > maximo):
        pedido = int(input(solicitacao))  # Refaz a solicitação

    return pedido  # Retorna o valor após passar na verificação


# Atribue à variável o valor verificado na função
valor = verifica_numero("Digite um valor inteiro para calcular o seu fatorial: ", 0, 10000)
print(f"{valor}! => {fatorial(valor)}")  # Exibe

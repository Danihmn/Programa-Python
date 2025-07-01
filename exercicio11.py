def verifica_numero(solicitacao, minimo, maximo):
    pedido = int(input(solicitacao))

    while (pedido < minimo) or (pedido > maximo):
        pedido = int(input(solicitacao))  # Refaz a solicitação

    return pedido  # Retorna o valor após passar na verificação


# Função que verifica a existência do arquivo
def existe_arquivo(arquivo):
    try:
        abrir = open(arquivo, "rt")  # Abre o arquivo
        abrir.close()  # Fecha o arquivo
    except FileNotFoundError:
        return False
    else:
        return True


# Função que cria o arquivo
def criar_arquivo(arquivo):
    try:
        abrir = open(arquivo, "wt+")  # Abre o arquivo
        abrir.close()  # Fecha o arquivo
    except:
        print("Ocorreu um erro ao tentar criar o arquivo")
    else:
        print(f"Arquivo {arquivo} criado com sucesso!\n")


# Inserir novos jogos ao arquivo
def cadastrar_jogo(arquivo, nome_jogo, nome_videogame):
    try:
        abrir = open(arquivo, "at")  # Abre o arquivo
    except:
        print("Erro ao tentar abrir o arquivo")
    else:
        abrir.write(f"{nome_jogo}; {nome_videogame}\n")  # Escreve no arquivo
        abrir.write("-" * (len(nome_jogo) + len(nome_videogame)) + "\n")  # Traça uma linha
    finally:
        abrir.close()  # Fecha o arquivo


# Lê o arquivo de jogos
def listar_arquivo(arquivo):
    try:
        abrir = open(arquivo, "rt")
    except:
        print("Erro ao tentar ler o arquivo")
    else:
        print(abrir.read())  # Lê o arquivo
    finally:
        abrir.close()  # Fecha o arquivo


# Programa principal
_arquivo = "Jogos.txt"  # Nome do arquivo

if existe_arquivo(_arquivo):
    print("Arquivo localizado no pc")
else:
    print("Arquivo inexistente")
    criar_arquivo(_arquivo)  # Chama a função que cria o arquivo

while True:
    print("MENU\n")
    print("1 - Cadastrar novo item")
    print("2 - Listar cadastros")
    print("3 - Sair\n")

    # Verifica o valor
    opcao = verifica_numero("Digite o valor que deseja: ", 1, 3)

    if opcao == 1:
        print("Opção de cadastro...\n")
        nome_jogo = input("Nome do jogo: ")
        nome_videogame = input("Nome da plataforma (Xbox, Playstation, PC...): ")
        cadastrar_jogo(_arquivo, nome_jogo, nome_videogame)
    elif opcao == 2:
        print("Opção de listagem...\n")
        listar_arquivo(_arquivo)
    elif opcao == 3:
        print("Programa encerrado")
        break

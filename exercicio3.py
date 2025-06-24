frase = input("Digite uma frase:  ") # Pede uma frase
tamanho_frase = len(frase) # Armazena na variável o tamanho da frase
metade_frase = frase[:int(tamanho_frase / 2)] # Armazena na variável a metade da frase

print(metade_frase[-2:]) # Exibe os dois últimos caracteres da metade da frase
# Crie uma variável de string que receba uma frase qualquer. Crie uma segunda variável agora contendo a metade da string digitada. Imprima na tela somente os dois últimos caracters da segunda variavel do tipo string

texto = input("Escreva sua frase motivacional abaixo\n")
tamanho = len(texto)
metadinha = texto[:int(tamanho/2)]
print(metadinha[-2:])
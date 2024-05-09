# Escreva um algoritmo que calcule a sua média de notas em determinada disciplina
#Vamos assumir que a média final é dada pela média aritmética de cinto notas digitadas

soma = 0 # Variavel acumuladora
cont = 1 # Variavel de contagem

while (cont <= 5):
    x = float(input(f"Digite a {cont}ª nota: "))
    soma = soma + x   # ou soma += x
    cont = cont + 1   # ou cont += 1
media = soma / 5
print(f'Média final: {media}.')

# TODO: Analisar e dissertar sobre o que esta escrito acima em comentario
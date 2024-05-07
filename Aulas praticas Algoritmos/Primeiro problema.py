# Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado a ele. Calcule e exiba o valor do desconto e o preço final do produto

preco = float(input('Escreva o preço do produto:\nR$ '))
desconto = float(input('Qual o valor do desconto?\n ') )
desconto_final = float(preco * (desconto / 100))
valor_final = float(preco - desconto_final)
print(f'Com um desconto de {desconto} %, você economiza {(desconto_final)} R$.\nE leva o produto por apenas {valor_final} R$!')

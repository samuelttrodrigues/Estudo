# Questão 1/4 

print('Bem-vindo ao atacarejo do Samuel Thiago Telles Rodrigues.')
preco_unitario = float(input('Escreva o valor do produto em R$: '))
quantidade = int(input('Escreva a quantidade a ser adquirida: '))

# Calculando o valor "bruto" da compra
valor = preco_unitario * quantidade
print(f'Valor total SEM desconto: R${valor}')

# Implementação de descontos

if (valor >= 10000):
    desconto = valor - (valor * (11/100))
    print(f'Valor total COM desconto: R${desconto}')
elif (6000 <= valor < 10000):
    desconto = valor - (valor * (7/100))
    print(f'Valor total COM desconto: R${desconto}')
elif (2500 <= valor < 6000):
    desconto = valor - (valor * (4/100))
    print(f'Valor total COM desconto: R${desconto}')
else:
    print(f'Valor total COM desconto: R${valor}') 
    # Como não tem desconto para valor abaixo de 2500, sera o mesmo que o valor "bruto"

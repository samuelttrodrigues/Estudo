def primeiro():
    item = []
    mercado = []

    for i in range(3):
        item.append(input('Digite o nome do item: '))
        item.append(int(input('Digite a quantidade: ')))
        item.append(float(input('Digite o valor: ')))
        mercado.append(item[:])
        item.clear() #! limpar a lista de item, para poder cadastrar o proximo
    print(mercado)

#------

mercado = []

for i in range(3):
    nome = input('Digite o nome do item: ')
    qnt = int(input('Digite a quantidade: '))
    valor = float(input('Digite o valor: '))
    mercado.append([nome,qnt,valor])
print(mercado)

#* Calculando com os valores da lista a cima
'''
soma = 0


print('Lista de compras:')
print('-' * 20)
print('Item | Quantidade | Valor unitário | total do item')
for item in mercado:
    print('{} | {} | {} | {}'.format(item[0], item[1], item[2]))
    soma += item[1] * item[2]
print('-' * 20)
print(f'Total a ser pago: {soma}')
'''
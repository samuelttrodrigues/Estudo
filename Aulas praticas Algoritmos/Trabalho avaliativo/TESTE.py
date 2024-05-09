#A Loja possui seguinte relação:
#!•	Tamanho P de Cupuaçu (CP) custa 9 reais e o Açaí (AC) custa 11 reais;
#*•	Tamanho M de Cupuaçu (CP) custa 14 reais e o Açaí (AC) custa 16 reais;
#?•	Tamanho G de Cupuaçu (CP) custa 18 reais e o Açaí (AC) custa 20 reais;


print('Bem-vindo a gelateria do Samuel Thiago Telles Rodrigues.\n')

valor_final = 0

while True:
                                                #Escolha do sabor
    sabor = input('Escolha o sabor. Cupuaçu ou Açaí. (CP/AC): ')
    if (sabor != 'AC' and sabor != 'CP'):
        print('Sabor incorreto. Tente novamente.\n')
        continue
                                                #Escolha do tamanho
    tamanho = input('Escolha o tamanho (P/M/G): ')
    if (tamanho != 'P' and tamanho != 'M' and tamanho != 'G'):
        print('Tamanho incorreto. Tente novamente.\n')
        continue    
                                                #Preços
    #Preço do Cupuaçu
    if(sabor == 'CP'):
        sabor = 'Cupuaçu'
        if(tamanho == 'P'):
            preco = 9
        elif(tamanho == 'M'):
            preco = 14
        else:
            preco = 18
    
    #Preço do Açaí
    if(sabor == 'AC'):
        sabor = "Açaí"
        if(tamanho == 'P'):
            preco = 11
        elif(tamanho == 'M'):
            preco = 16
        else:
            preco = 20

    print(f'Você pediu um {sabor} no tamanho {tamanho}: R${preco:.2f}\n')

    valor_final += preco
    
    outro = input('Deseja mais alguma coisa? (S/N): \n')

    while True:
        if (outro == 'S'):
            continue
        elif (outro == 'N'):
            break
        else:
            print('Você digitou algo errado.')
            continue
    break

print(f'Valor total a ser pago: R$ {valor_final} \n')
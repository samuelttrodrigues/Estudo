# Questão 2/4

print('Bem-vindo a sorveteria do balacobaco do Samuel Thiago Telles Rodrigues.\n')

print('-'*23,' Cardápio ', '-'*23)
print('-'*58)
print('------|  Tamanho  |   Cupuaçu (CP) |   Açaí (AC)   |------')
print('------|     P     |    R$  9.00    |   R$ 11.00    |------')
print('------|     M     |    R$ 14.00    |   R$ 16.00    |------')
print('------|     G     |    R$ 18.00    |   R$ 20.00    |------')
print('-'*58)

#Variável acumuladora Valor de base
valor_final = 0

while True:
                                                #Escolha do sabor
    sabor = input('\nEscolha o sabor. Cupuaçu ou Açaí. (CP/AC): ')
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

    # Variável acumuladora adicionando o preco para o valor final
    valor_final += preco
    
    outro = input('Deseja mais alguma coisa? (S/N): ')

    if (outro == 'S' or outro == 's'):
        continue

    elif (outro == 'N' or outro == 'n'):
        break

    else:   #Se não for nenhum desses inputs. Ira realizar o encerramento da compra e sera cobrado o valor final até o presente momento.
        print('Erro inesperado... Finalizando sua compra até o momento')
        break

print(f'\nValor total a ser pago: R$ {valor_final} \n')
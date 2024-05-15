print('Seja muito bem vindo a Loja da Laura Regina Silveira!')

print('--' * 12, 'CARDÁPIO', '--'*12)
print('--' * 29)
print('-'*3, '|', ' ', 'TAMANHO', ' ', '|', ' ', 'CUPUAÇU (CP)',
      ' ', '|', ' ', 'AÇAÍ (AC)', ' ', '|', '-'*3)
print('-'*3, '|', ' '*4, 'P', ' '*4, '|', ' '*3, 'R$  9.00',
      ' '*3, '|', ' ', 'R$ 11.00', ' '*2, '|', '-'*3)
print('-'*3, '|', ' '*4, 'M', ' '*4, '|', ' '*3, 'R$ 14.00',
      ' '*3, '|', ' ', 'R$ 16.00', ' '*2, '|', '-'*3)
print('-'*3, '|', ' '*4, 'G', ' '*4, '|', ' '*3, 'R$ 18.00',
      ' '*3, '|', ' ', 'R$ 20.00', ' '*2, '|', '-'*3)
print('--' * 29)

valor = 0
while True:

# SABOR
    sabor = input('Escolha o sabor desejado (CP/AC):\n').upper()

# Verificando se o sabor é valido
    if sabor not in ('CP', 'AC'):
        print('Sabor inválido. Tente novamente.')
        continue


# TAMANHO
    tam = input('Qual o tamanho que deseja (P/M/G)?\n').upper()

# Verificando se o tamanho é valido
    if tam != 'P' and tam != 'M' and tam != 'G':
        print('Tamanho inválido. Tente novamente.')
        continue


# COMBINAÇÕES:

# CUPUAÇU
    if sabor == 'CP':
        if tam == 'P':
            total = 9.00
            print(f'Voce pediu um cupuaçu no tamanho {tam}: R$9.00 \n')

        elif tam == 'M':
            total = 14.00
            print(f'Voce pediu um cupuaçu no tamanho {tam}: R$14.00 \n')

        else:
            tam == 'G'
            total = 18.00
            print(f'Voce pediu um cupuaçu no tamanho {tam}: R$18.00 \n')

# AÇAÍ
    if sabor == 'AC':
        if tam == 'P':
            total = 11.00
            print(f'Voce pediu um açaí no tamanho {tam}: R$11.00 \n')

        elif tam == 'M':
            total = 16.00
            print(f'Voce pediu um açaí no tamanho {tam}: R$16.00 \n')

        else:
            tam == 'G'
            total = 20.00
            print(f'Voce pediu um açaí no tamanho {tam}: R$20.00 \n')

    valor = valor + total
    
    cont = input('Deseja mais alguma coisa? (S/N)\n')

    if cont == 'S':
        continue

    elif cont == 'N':
        break

print(f'{valor}')
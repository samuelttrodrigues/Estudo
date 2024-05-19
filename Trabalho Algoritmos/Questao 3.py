# Questão 3/4

print('\nBoas vindas a copiadora do Samuel Thiago Telles Rodrigues\n')

def escolha_servico():

    print('Abaixo estão os serviços disponiveis:\n')
    print('DIG - Digitalização\nICO - Impressão Colorida')
    print('IPB - Impressão Preto e Branco\nFOT - Fotocópia')

    while True:

        global servico

        servico = input('\nQual serviço gostaria de escolher?\nServiço de: ')

        if (servico == 'DIG'):
            print('Você escolheu o serviço de Digitalização que tem um custo de R$ 1.10 reais para cada página\n')
            servico = 1.10
            break

        elif (servico == 'ICO'):
            print('Você escolheu o serviço de Impressão Colorida que tem um custo de R$ 1.00 real para cada página\n')
            servico = 1
            break

        elif (servico == 'IPB'):
            print('Você escolheu o serviço de Impressão Preto e Branco que tem um custo de R$ 0.40 centavos para cada página\n')
            servico = 0.4
            break

        elif (servico == 'FOT'):
            print('Você escolheu o serviço de Fotocópia que tem um custo de R$ 0.20 centavos para cada página\n')
            servico = 0.2
            break

        else:
            print('Você digitou algo de errado. Por favor tente novamente.\n')
            continue
    #Retorna o novo valor que servico assumiu 
    return servico  

def num_pagina():

    global paginas

    while True: #Verificando se o valor vai ser maior que 20000 
        try:
            paginas = (int(input('Entre com o número de páginas: ')))

            if paginas > 20000:
                print('Oops! Não aceitamos tantas páginas de uma vez. Por favor, tente novamente.')
                continue

            break

        except ValueError:
            print('Oops! Parece que você não digitou um número. Por favor, tente novamente')
    
    if paginas < 20:
        print(f'Com {paginas} páginas você não recebera nenhum desconto na hora da impressão\n')
        paginas = paginas

    elif 20 <= paginas < 200:
        print(f'Com {paginas} páginas você recebera um desconto de 15% em cima do número de páginas\n')
        paginas = paginas - (paginas * 0.15)

    elif 200 <= paginas < 2000:
        print(f'Com {paginas} páginas você recebera um desconto de 20% em cima do número de páginas\n')
        paginas = paginas - (paginas * 0.20)
    #Como só serão aceitos valores abaixo de 20000, não é necessario explicitar para o ultimo 'se'
    else:
        print(f'Com {paginas} páginas você recebera um desconto de 25% em cima do número de páginas\n')
        paginas = paginas - (paginas * 0.25)
    #retorna o valor de paginas com o desconto ja aplicado
    return paginas

def servico_extra():

    global extra

    print('Tabela de serviços extras abaixo:\n')
    print('1 - Encadernação Simples - R$ 15.00')
    print('2 - Encadernação Capa Dura - R$ 40.00')
    print('0 - Não desejo mais nada\n')

    while True:
        try:
            extra = int(input('Deseja adicionar algum serviço?\nServiço de número: '))
            #verificando se extra vai receber um valor adequado
            if (extra != 1 and extra != 2 and extra != 0):
                print('Digite um número entre 0, 1 e 2. Por favor.')
                continue

            elif extra == 1:
                extra = 15
                break

            elif extra == 2:
                extra = 40
                break

            else:
                extra = 0
                break

        except ValueError:
            print('Ops você digitou algo de errado. Por favor digite um número\n')
    #Retorna o valor que extra assumiu nessa função de acordo com a opção selecionada
    return extra

#Programa principal
#setando as variaveis para serem globais e assumirem novos valores após chamar a sequencia de funções

servico = escolha_servico()
paginas = num_pagina()
extra = servico_extra()

total = (servico * paginas) + extra

print(f'\nTotal: R$ {total:.2f}.\nDetalhamento de custos abaixo:\nServiço: R$ {servico} ("por página") * Páginas: R$ {paginas:.2f} ("com o desconto aplicado no número de páginas") + serviço adicional (encadernação): R$ {extra}')

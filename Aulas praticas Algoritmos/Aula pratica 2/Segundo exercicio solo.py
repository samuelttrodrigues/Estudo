# Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário qual operação ele deseja realizar: adição (+), subtração (-), multiplicação (*) ou divisão (/). Exiba na tela o resultado da operação desejada.

A = int(input('Escreva o primeiro número: '))
B = int(input('Escreva o segundo número: '))
operacao = input('\nQue operação gostaria de realizar?\nEscolha o simbolo na tabela abaixo \n\nAdição: + \nSubtração: - \nMultiplicação: * \nDivisão: / \nMinha escolha: ')

simbolo = operacao
if simbolo == "+":
    simbolo = ("adição")
elif simbolo == "-":
    simbolo = ("subtração")
elif simbolo == "*":
    simbolo = ("multiplicação")
elif simbolo == "/":
    simbolo = "divisão"


print(f'\nVocê escolheu a operação de {simbolo}!\n ')

if (operacao == "+"):
    print(f'O valor resultante da soma: {A} {operacao} {B}, é de {A + B}.')
    print('Encerrando o programa...')
elif (operacao == "-"):
    print(f'O valor resultante da subtração: {A} {operacao} {B}, é de {A - B}.')
    print('Encerrando o programa...')
elif (operacao == "*"):
    print(f'O valor resultante da multiplicação: {A} {operacao} {B}, é de {A * B}.')
    print('Encerrando o programa...')
elif (operacao == "/"):
    print(f'O valor resultante da divisão: {A} {operacao} {B}, é de {A / B}.')
    print('Encerrando o programa...')
else:
    print('A operação selecionada não é suportada no momento')
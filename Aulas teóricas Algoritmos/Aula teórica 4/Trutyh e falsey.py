#falsey = numero zero para int ou string vazia para strings
#truthy = qualquer outro dado

nome = '' #Falsey pois é uma string vazia
while not nome:
    #! Encerra quando o nome não estiver vazio
    nome = input('Digite seu nome: ')

valor = int(input("Digite um número qualquer: "))
if valor:  #! Equivalente: if valor != 0
           # ? Se digitar valor 0, ira retornar como false e ira para o else. Se for diferente
           # ? de 0, ira retornar como true e prosseguir para o if em vez do else.
    print('Você escolheu um valor diferente de zero.')
else:
    print('Você digitou zero.')
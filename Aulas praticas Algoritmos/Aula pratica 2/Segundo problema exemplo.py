#EVITAR COLOCAR COMENTARIOS COLORIDOS NA PRIMEIRA LINHA
    # !
    # *
    # ? 
    # TODO: escrever os codigos
    # // Só nos compiuter

ano = int(input("Digite o ano: "))
                                    # ! print(ano % 4) < Retorna valores diferentes de 0 quando não divisivel
if (ano % 4 == 0):
    print('Pode ser um ano bissexto')
else:
    print('Definitivamente não é um ano bissexto')

# ----------------

cima = True
baixo = True
if (cima == True and baixo == True):
    print('Decida-se!')
else:
    print('Você escolheu um caminho!')
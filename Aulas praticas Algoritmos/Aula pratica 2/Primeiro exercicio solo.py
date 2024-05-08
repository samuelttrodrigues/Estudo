# Faça um algoritmo que receba três valores, representando os lados de um triângulo fornecidos pelo usuário. Verifique se os valores formam um triângulo e classifique como
# A) Equilátero (Três lados iguais)
# B) Isósceles (Dois lados iguais)
# C) Escaleno (Tr~es lados diferentes)

A = float(input('Escreva a medida do primeiro lado em cm: '))
B = float(input('Escreva a medida do segundo lado em cm: '))
C = float(input('Escreva a medida do terceiro lado em cm: '))


if((A > 0 and B > 0 and C > 0) and (A + B > C and A + C > B and B + C > A)):
    #Se o programa chegou até aqui, é por que o triângulo é valido.
    if (A != B and A != C and B != C):
        print('O triângulo é Escaleno')
    else:
        if (A == B and B == C):
            print('O triângulo é Equilátero')
        else:
            print('O triângulo é Isósceles')
else:
    print('O triângulo não é válido.')
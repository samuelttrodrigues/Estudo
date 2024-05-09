# Escreva um algoritmo que imprima na tela somente valores dentro de um intervalo especificado pelo usuário e que sejam números pares

i = int(input("Escreva o valor inicial: ")) # ! i = Inicial
f = int(input("Escreva o valor final: "))   # ! f = Final

while ((i <= f)):
    if (i % 2 == 0): #// Utiliza o if para verificar se é par
        print(i)     # se for par, printa o valor. Se não for, pula o print e executa a soma
    i = i + 1        # adiciona 1 ao valor e volta para o começo do while


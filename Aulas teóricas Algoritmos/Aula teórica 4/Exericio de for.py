# Escreva um algoritmo que calcule a média dos números pares de 1 até 100. Impelemente usando
# o laço for

soma = 0
qtd = 0

for i in range(1,101):
    if (i % 2 == 0):
        soma += i
        qtd += 1
media = soma / qtd
print(f'A média dos pares de 1 até 100 é: {media}.')
print(soma)
print(qtd)
#!--------------------------------------------------------------------
for e in range(0,101,2):
    e += 2
print(f'A média dos pares de 1 até 100 é: {e / 2}.')
print(e)

#! Nesse exemplo não calculei a média. Somente a soma do ultimo valor com 2 / 2
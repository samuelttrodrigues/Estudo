# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalão: R para residências, I para indústrias e C para comércios
# Residencial= Até 500: R$ 0,40 por kWh. Acima de 500: R$ 0,65 por kWh.
# Comercial= Até 1000: R$ 0,55 por kWh. Acima de 1000: R$ 0,60 por kWh.
# Industrial= Até 5000: R$ 0,55 por kWh. Acima de 5000: R$ 0,60 por kWh.

print("Qual o seu tipo de instalação elétrica?")
print("Selecione R para residências")
print("Selecione I para industrias")
print("Selecione C para comércios")

instalacao = input("Minha instalação elétrica é: ")
consumo = int(input("Qual foi o seu consumo em kWh? \nConsumo:"))

if (instalacao == "R" or instalacao == "r"):
    if(consumo <= 500):
        preco = 0.4
    else:
        preco = 0.65
    print(f'Total a pagar: R${consumo * preco}')

elif (instalacao == "I" or instalacao == "i"):
    if(consumo <= 5000):
        preco = 0.55
    else:
        preco = 0.60
    print(f'Total a pagar: R${consumo * preco}')

elif (instalacao == "C" or instalacao == "c"):
    if(consumo <= 1000):
        preco = 0.55
    else:
        preco = 0.60
    print(f'Total a pagar: R${consumo * preco}')

else:
    print('Instalação inválida. Encerrando...')
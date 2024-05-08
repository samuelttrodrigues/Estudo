# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalão: R para residências, I para indústrias e C para comércios
# Residencial= Até 500: R$ 0,40 por kWh. Acima de 500: R$ 0,65 por kWh.
# Comercial= Até 1000: R$ 0,55 por kWh. Acima de 1000: R$ 0,60 por kWh.
# Industrial= Até 5000: R$ 0,55 por kWh. Acima de 5000: R$ 0,60 por kWh.

print("Qual o seu tipo de instalação elétrica?")
print("Selecione R para residências")
print("Selecione I para industrias")
print("Selecione C para comércios")
instalacao = input("Minha instalação elétrica é: ")
consumo = int(input("Qual foi o seu consumo em kWh? \nMeu consumo foi de "))
# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.

tempo = int(input("Quantos dias você andou ficou com o carro?\n"))
km = float(input("Quantos Km você dirigiu?\n"))
calculo_tempo = tempo * 60
calculo_km = km * 0.15
calculo_total = (calculo_tempo) + (calculo_km)
print(f'Sua divida é de R$ {calculo_total}.')
print(f'Sendo R$ {calculo_tempo} pela quantidade de dias.\nE R$ {calculo_km} pela kilometragem rodada.')
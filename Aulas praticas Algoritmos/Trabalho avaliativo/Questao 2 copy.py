#Enunciado: Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para uma loja que vende Açaí e Cupuaçu. Você ficou com a parte de desenvolver a interface do cliente para retirada do produto.

#A Loja possui seguinte relação:
#!•	Tamanho P de Cupuaçu (CP) custa 9 reais e o Açaí (AC) custa 11 reais;
#*•	Tamanho M de Cupuaçu (CP) custa 14 reais e o Açaí (AC) custa 16 reais;
#?•	Tamanho G de Cupuaçu (CP) custa 18 reais e o Açaí (AC) custa 20 reais;


print('Bem-vindo a gelateria do Samuel Thiago Telles Rodrigues.\n')

# Fazer um cardapio mostrando o preço dos items

while True:    
    sabor = input('Qual o sabor desejado? (CP/AP): ')
    if ((sabor == 'CP') or (sabor == 'AP')):
        print('Sabor inválido. Tente novamente\n')
        continue # Volta para o começo do laço
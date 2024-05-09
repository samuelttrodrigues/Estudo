# Crie um algoritmo que receba um valor do tipo inteiro via teclado
# No entanto, o programa só deve aceitar, obrigatoriamente, valores inteiros e positivos
# Qualquer valor negativo, ou igual a zero, deve ser rejeitado pelo programa e um novo valor deve ser solicitado

valor = int(input("Escreva um valor numérico inteiro que seja > 0: "))

while (valor <= 0):
    valor = int(input("Escreva um valor numérico inteiro que seja > 0: "))
print(f"Valor {valor}. Encerrando...")

# Overcomplicated apenas. 
# ! Prestar atenção na possibilidade dos operadores relacionais


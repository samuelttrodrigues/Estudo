# Exercícios de condicional simples

idade = int(input("Digita a idade: "))
if (idade > 60):
    print("Você tem direito aos benefícios")

# ------------

dano = int(input("Digite o dano: "))
escudo = int(input("Digite o valor do escudo: "))
if (dano > 10 and escudo == 0):
    print("Você está morto!")

# ---------

norte = True
sul = False
leste = False
oeste = True

if (norte or sul or leste or oeste == true):
    print('Você escapou!')
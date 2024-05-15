

# Validação das opções do Menu
def valida_opcao(pergunta,min,max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x
# Cadastro de livro
def cadastrar_livro(id):

    global id_global
    id_global += 1

    nome = input('Digite o nome do livro: ')
    autor = input('Digite o Autor: ')
    editora = input('Digite a editora: ')
    
    livro = {'id': id,'Nome':nome,'Autor':autor,'Editora':editora}

    lista_livro.append(livro)

def listar_livro():
    menu_consulta()
    opcao = valida_opcao('>> ',1 ,4)

    if opcao == 1:
        print('-' * 60)
        for chave,valor in lista_livro.items():
            print(f'{chave}: {valor}')
    


def remover_livro():
    id = 0
    


def menu_principal():
    print('-'* 56)
    print('-' * 20,'MENU PRINCIPAL','-'*20)
    #Opções do menu
    print('Escolha a opção desejada:')
    print('1 - Cadastrar Livro')
    print('2 - Consultar Livros(s)')
    print('3 - Remover Livro')
    print('4 - Sair')

def menu_cadastro():
    print('-'* 56)
    print('-' * 20,'CADASTRAR LIVRO','-'*20)

def menu_consulta():
    print('-'* 56)
    print('-' * 20,'CONSULTAR LIVRO','-'*20)    
    print('Escolha a opção desejada:')
    print('1 - Consultar todos os livros')
    print('2 - Consultar Livro por id')
    print('3 - Consultar Livro(s) por autor')
    print('4 - Retornar')

lista_livro = []
id_global = 0

while True:

    menu_principal()

    opcao = valida_opcao('>> ',1,4)

    if(opcao == 1): #Cadastrar Livro
        print('Opção de cadastrar novo item selecionada...\nPor favor siga as instruções')
        menu_cadastro()
        cadastrar_livro(id_global)
        continue


    elif(opcao == 2): #Consultar Livros(s)
        print('Opção de listar selecionada...\n')
        listar_livro()
        
        
        


    elif(opcao == 3): #Remover Livro
        print('Encerrando o programa...')
        break


    elif(opcao == 4): #Sair
        print('Encerrando o programa...')
        break
# Questão 4/4

# Validação das opções do Menu
def valida_opcao(pergunta,min,max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x


# Opção 1 - Cadastro de livro
def cadastrar_livro(id):


    global id_global
    id_global += 1


    nome = input('Digite o nome do livro: ')
    autor = input('Digite o Autor: ')
    editora = input('Digite a editora: ')
    # Cria um dicionario com as informações do livro e adiciona a lista de livros
    livro = {'ID': id,'Nome':nome,'Autor':autor,'Editora':editora}


    lista_livro.append(livro)


# Opção 2 - Listar Livros por: Todos, ID e autor
def consultar_livro():
    while True:
        menu_consulta()
        opcao = valida_opcao('>> ',1 ,4)


        #Lista todos os livros
        if opcao == 1:
            print('-' * 60)
            for livro in lista_livro:
                print('\nInformações sobre o livro: ')
                for chave,valor in livro.items():
                    print(f'{chave}: {valor}')
            continue


        #Consulta livros por ID especifico    
        elif opcao == 2:
            consultar_id = int(input('\nDigite o ID do livro: '))
            for livro in lista_livro:
                if livro['ID'] == consultar_id:                    
                    print(f'\nDetalhes sobre o livro de ID: {consultar_id} \n')
                    for chave,valor in livro.items():
                        print(f'{chave}: {valor}')
                    continue


        #Consulta livros por autor
        elif opcao == 3:
            consultar_por_autor = input ('\nDigite o nome do autor do(s) livro(s): ')
            print(f'Livros do autor {consultar_por_autor}\n')
            for livro in lista_livro:
                    if livro['Autor'] == consultar_por_autor:    
                        for chave,valor in livro.items():
                            print(f'{chave}: {valor}')
            continue


        else:
            break


# Opção 3 - Remove livro por ID somente
def remover_livro():
    while True:
        remover = int(input('Digite o ID do livro que gostaria de remover: '))
        for livro in lista_livro:
            if livro['ID'] == remover:
                lista_livro.remove(livro)
                print('O livro foi removido')
                return
        else:
            print('ID inválido. Tente novamente')


# Sequencia de menus utilizado no código
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


def menu_remover():
    print('-'* 56)
    print('-' * 20,'REMOVER LIVRO','-'*20)


# Programa principal

print('Bem vindo a biblioteca do Samuel Thiago Telles Rodrigues')

lista_livro = []
id_global = 0


while True:
    menu_principal()


    opcao = valida_opcao('>> ',1,4)


    if(opcao == 1): #Cadastrar Livro
        print('\nOpção de cadastrar novo item selecionada...\nPor favor siga as insira os dados corretamente.\n')
        menu_cadastro()
        cadastrar_livro(id_global)
        continue


    elif(opcao == 2): #Consultar Livros(s)
        print('\nOpção de consular livros selecionada...\n')
        consultar_livro()
 
    elif(opcao == 3): #Remover Livro
        print('\nOpção de remover livro selecionada ...\n')
        menu_remover()
        remover_livro()


    elif(opcao == 4): #Sair
        print('Encerrando o programa... Tchau Tchau')
        break
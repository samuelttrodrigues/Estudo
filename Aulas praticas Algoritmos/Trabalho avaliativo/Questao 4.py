#1)	Cadastrar Livro
#2)	Consultar Livro
#   1.	Consultar Todos 
#   2.	Consultar por Id
#   3.	Consultar por Autor
#   4.	Retornar ao menu
#3)	Remover Livro
#4)	Encerrar Programa

#Boas vindas
print('Bem vindo a Livraria do Samuel Thiago Telles Rodrigues')
#Menu principal

lista_livro = []
id_global = 0

def cadastrar_livro(id):
    
    nome = input('Digite o nome do livro: ')
    autor = input('Digite o Autor: ')
    editora = input('Digite a editora: ')
    
    id = [nome,autor,editora]
    lista_livro.append([nome,autor,editora])
    return id

print('-'* 56)
print('-' * 20,'MENU PRINCIPAL','-'*20)
#Opções do menu
print('Escolha a opção desejada:')
print('1 - Cadastrar Livro')
print('2 - Consultar Livros(s)')
print('3 - Remover Livro')
print('4 - Sair')

cadastrar_livro()
print (lista_livro)


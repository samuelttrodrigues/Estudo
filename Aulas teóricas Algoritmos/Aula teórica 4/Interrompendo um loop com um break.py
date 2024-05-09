# Um algoritmo que pede inputs de um usuario até ele digitar "sair"


print ('Digite uma mensagem que repetirei ela para você.\nDigite \"sair\" para encerrar o programa.')
while True:
    txt = input('')
    print(txt)
    if (txt == 'Sair' or txt == 'sair'):
        break
print('Encerrando o programa.')
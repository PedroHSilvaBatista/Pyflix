import os
import json
from functions.menu import menu
from functions.cadastro_login import cadastro, login

diretorio_atual = os.path.dirname(__file__)
caminho_usuarios = os.path.join(diretorio_atual, 'data', 'usuarios.json')

status_de_login = False

while True:
    menu()
    opcao_usuario = input('Digite a opção desejada: ')

    match opcao_usuario:
        case '1':
            with open(caminho_usuarios, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
            cadastro(dados)
        case '2':
            login(status_de_login)
        case '3':
            pass
        case '4':
            pass
        case '5':
            pass
        case '6':
            pass
        case '7':
            pass
        case '8':
            print('Volte sempre :)')
            print('Encerrando o programa...')
            break
        case _:
            print('Por favor! Digite umas das opções disponíveis')

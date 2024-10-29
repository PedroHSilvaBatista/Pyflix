import os
import json
from functions.menu import menu
from functions.cadastro_login import cadastro, login
from models.filme import Filme
from models.serie import Serie
from models.documentario import Documentario

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
            # Ajustar a formatação de saída
            # Talvez seja uma boa ideia criar uma função que seja o menu de titulos para encurtar o código abaixo
            print('Digite qual título que gostaria de ser exibido: ')
            print('1 - Filme')
            print('2 - Série')
            print('3 - Documentário')
            opcao_usuario_titulo = input('Digite sua opção: ')
            match opcao_usuario_titulo:
                case '1':
                    print('Aqui estão todos os filmes já catalogados')
                    Filme.listar_filmes()
                case '2':
                    print('Aqui estão todos as séries já catalogadas')
                    Serie.listar_series()
                case '3':
                    print('Aqui estão todos os documentários já catalogados')
                    Documentario.listar_documentarios()
                case _:
                    print('Por favor! Digite uma opção válida')
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

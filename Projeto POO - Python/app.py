import os
import json
from functions.menus import menu, exibir_categorias
from functions.cadastro_login import cadastro, login
from functions.subir_dados import subir_dados_filme
from models.filme import Filme
from models.serie import Serie
from models.documentario import Documentario

diretorio_atual = os.path.dirname(__file__)
caminho_usuarios = os.path.join(diretorio_atual, 'data', 'usuarios.json')
caminho_arquivo_filme = os.path.join(diretorio_atual, 'data', 'filmes.json')

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
            print('Digite qual categoria que gostaria que fosse exibida: ')
            exibir_categorias()
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
                    print('Por favor, digite uma opção válida')
        case '4':
            # Verificar se o título já se encontra no catálogo
            print('Digite qual categoria que gostaria de recomendar um novo título')
            exibir_categorias()
            opcao_usuario_adicao = input('Digite sua opção: ')
            match opcao_usuario_adicao:
                case '1':
                    print('Para que a adição de um filme seja efetuada, é necessário informar alguns dados antes')
                    
                    nome_do_filme = input('Digite o nome do filme: ')
                    ano_de_lancamento = input('Digite o ano de lançamento: ')
                    tempo_de_duracao = input('Digite o tempo de duração aproximado do filme em minutos: ')
                    
                    print('Digite três categorias que mais combinam com o filme selecionado')
                    generos = []
                    for c in range(3):
                        if c == 0:
                            generos.append(input('Digite a categoria principal do filme: '))
                        elif c == 1:
                            generos.append(input('Digite outra categoria do filme: '))
                        else:
                            generos.append(input('Digite a última categoria do filme: '))
                    
                    sinopse = input('Diga a sinopse do filme: ')
                    diretor = input('Diga um dos diretores do filme: ')
                    estudio = input('Diga o estúdio em que foi produzido o filme: ')
                    Filme(nome_do_filme, ano_de_lancamento, tempo_de_duracao, generos, sinopse, diretor, estudio)
                    subir_dados_filme(Filme.catalogo_de_filmes)
                    print('Filme recomendado com sucesso!')
                case '2':
                    pass
                case '3':
                    pass
                case _:
                    print('Por favor, digite uma opção válida')
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

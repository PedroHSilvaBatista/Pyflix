import os
import json
from functions.menus import menu, exibir_categorias
from functions.cadastro_login import cadastro, login
from functions.subir_dados import subir_dados_filmes, subir_dados_series, subir_dados_documentario
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
                    ano_de_lancamento_filme = input('Digite o ano de lançamento: ')
                    tempo_de_duracao_filme = input('Digite o tempo de duração aproximado do filme em minutos: ')
                    
                    print('Digite três categorias que mais combinam com o filme selecionado')
                    generos_filme = []
                    for c in range(3):
                        if c == 0:
                            generos_filme.append(input('Digite a categoria principal do filme: '))
                        elif c == 1:
                            generos_filme.append(input('Digite outra categoria do filme: '))
                        else:
                            generos_filme.append(input('Digite a última categoria do filme: '))
                    
                    sinopse_filme = input('Diga a sinopse do filme: ')
                    diretor_filme = input('Diga um dos diretores do filme: ')
                    estudio_filme = input('Diga o estúdio em que foi produzido o filme: ')
                    Filme(nome_do_filme, ano_de_lancamento_filme, tempo_de_duracao_filme, generos_filme, sinopse_filme, diretor_filme, estudio_filme)
                    subir_dados_filmes(Filme.catalogo_de_filmes)
                    print('Filme recomendado com sucesso!')
                case '2':
                    print('Para que a adição de uma série seja efetuada, é necessário informar alguns dados antes')

                    nome_da_serie = input('Digite o nome da série: ')
                    ano_de_lancamento_serie = input('Digite o ano em que a série foi lançada: ')
                    tempo_de_duracao_serie = input('Digite o tempo de duração total da série (pode ser um valor estimado): ')

                    print('Digite três categorias que mais combinam com a série selecionada')
                    generos_serie = []
                    for c in range(3):
                        if c == 0:
                            generos_serie.append(input('Digite a categoria principal da série: '))
                        elif c == 1:
                            generos_serie.append(input('Digite outra categoria da série: '))
                        else:
                            generos_serie.append(input('Digite a última categoria da série: '))
                    
                    sinopse_serie = input('Diga a sinopse da série: ')
                    numero_de_temporadas_serie = input('Diga quantas temporadas a série possui: ')
                    numero_de_episodios_serie = input('Digite quantos episódios a série possui ao total (pode ser um valor aproximado): ')
                    Serie(nome_da_serie, ano_de_lancamento_serie, tempo_de_duracao_serie, generos_serie, sinopse_serie, numero_de_temporadas_serie, numero_de_episodios_serie)
                    subir_dados_series(Serie.catalogo_de_series)
                    print('Série recomendada com sucesso!')
                case '3':
                    print('Para que a adição de um documentário seja efetuada, é necessário informar alguns dados antes')

                    nome_do_documentario = input('Digite o nome do documentário: ')
                    ano_de_lancamento_documentario = input('Digite o ano em que o documentário foi lançado: ')
                    tempo_de_duracao_documentario = input('Digite o tempo de duração do documentário em minutos: ')
                    categoria_documentario = input('Digite a categoria do documentário (Ex: Biografia, História): ')
                    sinopse_documentario = input('Diga a sinpose do documentário: ')
                    autor_documentario = input('Digite o autor, roteirista ou produtor do documentário: ')
                    tema_documentario = input('Digite o tema a qual o documentário se trata: ')
                    Documentario(nome_do_documentario, ano_de_lancamento_documentario, tempo_de_duracao_documentario, categoria_documentario, sinopse_documentario, autor_documentario, tema_documentario)
                    subir_dados_documentario(Documentario.catalogo_de_documentarios)
                    print('Documentário recomendado com sucesso!')
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

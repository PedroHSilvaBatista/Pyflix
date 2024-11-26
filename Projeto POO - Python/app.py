import os
import json
from functions.menus import menu, exibir_categorias
from functions.cadastro_login import cadastro, login
from functions.subir_dados import subir_dados_filmes, subir_dados_series, subir_dados_documentario
from functions.verificadores import encontrar_filme_no_catalogo, encontrar_serie_no_catalogo, encontrar_documentario_no_catalogo
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
                    Filme.listar_catalogo_de_filmes()
                case '2':
                    print('Aqui estão todos as séries já catalogadas')
                    Serie.listar_catalogo_de_series()
                case '3':
                    print('Aqui estão todos os documentários já catalogados')
                    Documentario.listar_documentarios()
                case _:
                    print('Por favor, digite uma opção válida')
        case '4':
            print('Digite qual categoria que gostaria de recomendar um novo título')
            exibir_categorias()
            opcao_usuario_adicao = input('Digite sua opção: ')
            match opcao_usuario_adicao:
                case '1':
                    print('Para que a adição de um filme seja efetuada, é necessário informar alguns dados antes')
                    
                    nome_do_filme = input('Digite o nome do filme: ').title()
                    encontrar_filme = encontrar_filme_no_catalogo(nome_do_filme)

                    if encontrar_filme:
                        print('O filme que você está tentando cadastrar já se encontra no catálogo')
                        print('Por favor, tente recomendar um filme que ainda não esteja cadastrado no sistema')
                    else:
                        try:
                            ano_de_lancamento_filme = int(input('Digite o ano de lançamento: '))
                            tempo_de_duracao_filme = int(input('Digite o tempo de duração aproximado do filme em minutos: '))
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
                        except ValueError:
                            print('Erro, o valor informado não é um valor inteiro')
                        except Exception as mensagem_erro_geral:
                            print('Ocorreu um erro inesperado! Verifique se um dos campos foi digitado corretamante')
                case '2':
                    print('Para que a adição de uma série seja efetuada, é necessário informar alguns dados antes')

                    nome_da_serie = input('Digite o nome da série: ').title()
                    encontrar_serie = encontrar_serie_no_catalogo(nome_da_serie)

                    if encontrar_serie:
                        print('A série que você está tentando cadastrar já se encontra no catálogo')
                        print('Por favor, tente recomendar uma série que ainda não esteja cadastrada no sistema')
                    else:
                        try:
                            ano_de_lancamento_serie = int(input('Digite o ano em que a série foi lançada: '))
                            tempo_de_duracao_serie = int(input('Digite o tempo de duração total da série (pode ser um valor estimado): '))
                            numero_de_temporadas_serie = int(input('Diga quantas temporadas a série possui: '))
                            numero_de_episodios_serie = int(input('Digite quantos episódios a série possui ao total (pode ser um valor aproximado): '))
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
                            Serie(nome_da_serie, ano_de_lancamento_serie, tempo_de_duracao_serie, generos_serie, sinopse_serie, numero_de_temporadas_serie, numero_de_episodios_serie)
                            subir_dados_series(Serie.catalogo_de_series)
                            print('Série recomendada com sucesso!')
                        except ValueError:
                            print('Erro, o valor informado não é um valor inteiro')
                        except Exception as mensagem_erro_geral:
                            print('Ocorreu um erro inesperado! Verifique se um dos campos foi digitado corretamante')
                case '3':
                    print('Para que a adição de um documentário seja efetuada, é necessário informar alguns dados antes')

                    nome_do_documentario = input('Digite o nome do documentário: ').title()
                    encontrar_documentario = encontrar_documentario_no_catalogo(nome_do_documentario)

                    if encontrar_documentario:
                        print('O documentário que você está tentando cadastrar já se encontra no catálogo')
                        print('Por favor, tente recomendar um documentário que ainda não esteja cadastrado no sistema')
                    else:
                        try:
                            ano_de_lancamento_documentario = int(input('Digite o ano em que o documentário foi lançado: '))
                            tempo_de_duracao_documentario = int(input('Digite o tempo de duração do documentário em minutos: '))
                            categoria_documentario = input('Digite a categoria do documentário (Ex: Biografia, História): ')
                            sinopse_documentario = input('Diga a sinpose do documentário: ')
                            autor_documentario = input('Digite o autor, roteirista ou produtor do documentário: ')
                            tema_documentario = input('Digite o tema a qual o documentário se trata: ')
                            Documentario(nome_do_documentario, ano_de_lancamento_documentario, tempo_de_duracao_documentario, categoria_documentario, sinopse_documentario, autor_documentario, tema_documentario)
                            subir_dados_documentario(Documentario.catalogo_de_documentarios)
                            print('Documentário recomendado com sucesso!')
                        except ValueError:
                            print('Erro, o valor informado não é um valor inteiro')
                        except Exception as mensagem_erro_geral:
                            print('Ocorreu um erro inesperado! Verifique se um dos campos foi digitado corretamante')
                case _:
                    print('Por favor, digite uma opção válida')
        case '5':
            print('Digite qual categoria que gostaria de avaliar')
            exibir_categorias()
            opcao_usuario_avaliar = input('Digite sua opção: ')
            match opcao_usuario_avaliar:
                case '1':
                    print('Para que se possa avaliar um filme, é necessário primeiro digitar o nome do filme a qual se quer avaliar')

                    usuario_nome_do_filme = input('Digite o nome do filme aqui: ').title()
                    encontrar_filme_para_avaliar = encontrar_filme_no_catalogo(usuario_nome_do_filme)

                    if encontrar_filme_para_avaliar:
                        pass
                    else:
                        print('O filme digitado não foi encontrado')
                        print('Por favor, verique se o nome do filme foi inserido corretamente')
                case '2':
                    pass
                case '3':
                    pass
                case _:
                    print('Por favor, digite uma opção válida')
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

# Importações feitas
import os
import json
from functions.menus import menu, exibir_categorias
from functions.cadastro_login import cadastro, login
from functions.subir_dados import subir_dados_filmes, subir_dados_series, subir_dados_documentario
from functions.verificadores import encontrar_filme_no_catalogo, encontrar_serie_no_catalogo, encontrar_documentario_no_catalogo
from models.filme import Filme
from models.serie import Serie
from models.documentario import Documentario

# Caminhos que levam até seus respectivos arquivos
diretorio_atual = os.path.dirname(__file__)
caminho_usuarios = os.path.join(diretorio_atual, 'data', 'usuarios.json')
caminho_filmes = os.path.join(diretorio_atual, 'data', 'filmes.json')
caminho_series = os.path.join(diretorio_atual, 'data', 'series.json')
caminho_documentarios = os.path.join(diretorio_atual, 'data', 'documentarios.json')


def app():
    # Variável de controle do status de login do usuário
    status_de_login = False

    while True:
        menu()
        # Variável que armazena a opção desejada do usuário perante as funcionalidades que o sistema oferece
        opcao_usuario = input('Digite a opção desejada: ')

        # Estrutura Match Case para as diferentes respostas do usuário
        match opcao_usuario:
            case '1':
                # Estrutura que cadastra um novo usuário
                with open(caminho_usuarios, 'r', encoding='utf-8') as arquivo:
                    dados = json.load(arquivo)
                cadastro(dados)
            case '2':
                # Estrutura que permite o usuário logar em sua conta
                retorno = login(status_de_login)
                if type(retorno) == tuple:
                    status_de_login = retorno[0]
                    nome_de_usuario_logado = retorno[1]
                else:
                    status_de_login = retorno
            case '3':
                # Estrutura que permite o usuário listar uma das categorias do sistema
                print('Digite qual categoria que gostaria que fosse exibida: ')
                exibir_categorias()
                # Variável que armazena qual categoria o usuário quer visualizar
                opcao_usuario_titulo = input('Digite sua opção: ')
                match opcao_usuario_titulo:
                    case '1':
                        # Estrutura que exibe a lista de filmes em catálogo
                        print('Aqui estão todos os filmes já catalogados')
                        Filme.listar_catalogo_de_filmes()
                    case '2':
                        # Estrutura que exibe a lista de séries em catálogo
                        print('Aqui estão todos as séries já catalogadas')
                        Serie.listar_catalogo_de_series()
                    case '3':
                        # Estrutura que exibe a lista de documentários em catálogo
                        print('Aqui estão todos os documentários já catalogados')
                        Documentario.listar_documentarios()
                    case _:
                        print('Por favor, digite uma opção válida')
            case '4':
                # Estrutura que permite o usuário adicionar um novo título ao sistema
                # Estrutura condicional que verifica se o usuário está logado para fazer uma adição
                if status_de_login:
                    print('Digite qual categoria que gostaria de recomendar um novo título')
                    exibir_categorias()
                    # Variável que armazena qual categoria o usuário deseja adicionar
                    opcao_usuario_adicao = input('Digite sua opção: ')
                    match opcao_usuario_adicao:
                        case '1':
                            # Estrutura que exige as informações do filme antes que o título possa ser adicionado ao banco de dados
                            print('Para que a adição de um filme seja efetuada, é necessário informar alguns dados antes')
                            
                            nome_do_filme = input('Digite o nome do filme: ').title()
                            # Função que verifica se o filme digitado já se encontra no banco de dados
                            encontrar_filme = encontrar_filme_no_catalogo(nome_do_filme)
                            
                            if encontrar_filme:
                                # Caso o filme seja encontrado, o usuário deverá digitar o nome de outro filme
                                print('O filme que você está tentando cadastrar já se encontra no catálogo')
                                print('Por favor, tente recomendar um filme que ainda não esteja cadastrado no sistema')
                            else:
                                # Caso o filme não seja encontrado, o usuário poderá prosseguir com a adição do filme
                                try:
                                    # Tratamento de exceção para verificar se o usuário irá digitar o valor do tipo correto
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
                                    nota_filme = float(input('Indique uma nota de 0 a 10 que gostaria de atribuir ao filme: '))
                                    
                                    # Estrutura condicional para ver se o usuário digitou a nota corretamente
                                    if type(nota_filme) == float or type(nota_filme) == int:
                                        if nota_filme < 0 or nota_filme > 10:
                                            print('Nota inválida. Verifique se a nota digitada pertence ao intervalo de 0 a 10')
                                            print('Por favor, tente novamente mais tarde.')
                                        else:
                                            # Caso o usuário tenha digitado tudo corretamente, o filme informado subirá ao banco de dados
                                            Filme(nome_do_filme, ano_de_lancamento_filme, tempo_de_duracao_filme, generos_filme, sinopse_filme, diretor_filme, estudio_filme, nota_filme)
                                            subir_dados_filmes(Filme.catalogo_de_filmes)
                                            print('Filme recomendado com sucesso!')
                                    else:
                                        print('Erro. Por favor, digite um valor real para a atribuição da nota')
                                except ValueError:
                                    print('Ocorreu um erro inesperado! Verifique se um dos campos foi digitado corretamante')
                        case '2':
                            # Estrutura que exige as informações da série antes que o título possa ser adicionado ao banco de dados
                            print('Para que a adição de uma série seja efetuada, é necessário informar alguns dados antes')

                            nome_da_serie = input('Digite o nome da série: ').title()
                            # Função que verifica se a série digitada já se encontra no banco de dados
                            encontrar_serie = encontrar_serie_no_catalogo(nome_da_serie)

                            if encontrar_serie:
                                # Caso a série seja encontrada, o usuário deverá digitar o nome de outra série
                                print('A série que você está tentando cadastrar já se encontra no catálogo')
                                print('Por favor, tente recomendar uma série que ainda não esteja cadastrada no sistema')
                            else:
                                # Caso a série não seja encontrada, o usuário poderá prosseguir com a adição da série
                                try:
                                    # Tratamento de exceção para verificar se o usuário irá digitar o valor do tipo correto
                                    ano_de_lancamento_serie = int(input('Digite o ano em que a série foi lançada: '))
                                    tempo_de_duracao_serie = int(input('Digite o tempo de duração total da série (pode ser um valor estimado): '))
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
                                    numero_de_temporadas_serie = int(input('Diga quantas temporadas a série possui: '))
                                    numero_de_episodios_serie = int(input('Digite quantos episódios a série possui ao total (pode ser um valor aproximado): '))
                                    nota_serie = float(input('Indique uma nota de 0 a 10 que gostaria de atribuir a série: '))

                                    # Estrutura condicional para ver se o usuário digitou a nota corretamente
                                    if type(nota_serie) == float or type(nota_serie) == int:
                                        if nota_serie < 0 or nota_serie > 10:
                                            print('Nota inválida. Verifique se a nota digitada pertence ao intervalo de 0 a 10')
                                            print('Por favor, tente novamente mais tarde.')
                                        else:
                                            # Caso o usuário tenha digitado tudo corretamente, a série informada subirá ao banco de dados
                                            Serie(nome_da_serie, ano_de_lancamento_serie, tempo_de_duracao_serie, generos_serie, sinopse_serie,numero_de_temporadas_serie, numero_de_episodios_serie, nota_serie)
                                            subir_dados_series(Serie.catalogo_de_series)
                                            print('Série recomendada com sucesso!')
                                    else:
                                        print('Erro. Por favor, digite um valor real para a atribuição da nota')
                                except ValueError:
                                    print('Ocorreu um erro inesperado! Verifique se um dos campos foi digitado corretamante')
                        case '3':
                            # Estrutura que exige as informações do documentário antes que o título possa ser adicionado ao banco de dados
                            print('Para que a adição de um documentário seja efetuada, é necessário informar alguns dados antes')

                            nome_do_documentario = input('Digite o nome do documentário: ').title()
                            # Função que verifica se o documentário digitado já se encontra no banco de dados
                            encontrar_documentario = encontrar_documentario_no_catalogo(nome_do_documentario)

                            if encontrar_documentario:
                                # Caso o documentário seja encontrado, o usuário deverá digitar o nome de outro documentário
                                print('O documentário que você está tentando cadastrar já se encontra no catálogo')
                                print('Por favor, tente recomendar um documentário que ainda não esteja cadastrado no sistema')
                            else:
                                try:
                                    # Tratamento de exceção para verificar se o usuário irá digitar o valor do tipo correto
                                    ano_de_lancamento_documentario = int(input('Digite o ano em que o documentário foi lançado: '))
                                    tempo_de_duracao_documentario = int(input('Digite o tempo de duração do documentário em minutos: '))
                                    categoria_documentario = input('Digite a categoria do documentário (Ex: Biografia, História): ')
                                    sinopse_documentario = input('Diga a sinpose do documentário: ')
                                    autor_documentario = input('Digite o autor, roteirista ou produtor do documentário: ')
                                    tema_documentario = input('Digite o tema a qual o documentário se trata: ')
                                    nota_documentario = float(input('Indique uma nota de 0 a 10 que gostaria de atribuir o documentário: '))

                                    # Estrutura condicional para ver se o usuário digitou a nota corretamente
                                    if nota_documentario < 0 or nota_documentario > 10:
                                        print('Nota inválida. Verifique se a nota digitada pertence ao intervalo de 0 a 10')
                                        print('Por favor, tente novamente mais tarde.')
                                    else:
                                        # Caso o usuário tenha digitado tudo corretamente, o documentário informada subirá ao banco de dados
                                        Documentario(nome_do_documentario, ano_de_lancamento_documentario, tempo_de_duracao_documentario,categoria_documentario, sinopse_documentario, autor_documentario, tema_documentario, nota_documentario)
                                        subir_dados_documentario(Documentario.catalogo_de_documentarios)
                                        print('Documentário recomendado com sucesso!')
                                except ValueError:
                                    print('Ocorreu um erro inesperado! Verifique se um dos campos foi digitado corretamante')
                        case _:
                            print('Por favor, digite uma opção válida')
                else:
                    print('Para que se possa recomendar um título, é necessário primeiro estar logado')
            case '5':
                # Estrutura que permite o usuário avaliar um título presente no banco de dados
                # Estrutura condicional que verifica se o usuário está logado para fazer uma avaliação
                if status_de_login:
                    print('Digite qual categoria que gostaria de avaliar')
                    exibir_categorias()
                    # Variável que armazena qual categoria o usuário deseja avaliar
                    opcao_usuario_avaliar = input('Digite sua opção: ')
                    match opcao_usuario_avaliar:
                        case '1':
                            print('Para que se possa avaliar um filme, é necessário primeiro digitar o nome do filme a qual se quer avaliar')

                            usuario_nome_do_filme = input('Digite o nome do filme aqui: ').title()
                            # Função que verifica se o filme digitado pelo usuário existe no banco de dados
                            encontrar_filme_para_avaliar = encontrar_filme_no_catalogo(usuario_nome_do_filme)

                            # Se o filme existir, o processo de avaliação prossegue, caso contrário, o usuário é informado que o filme digitado não foi encontrado
                            if encontrar_filme_para_avaliar:
                                try:
                                    # Estrutura que verifica se a nota digitada pelo usuário é válida
                                    avaliacao_do_usuario_filme = float(input(f'Indique aqui a nota que gostaria de atribuir ao filme "{usuario_nome_do_filme}": '))
                                    if avaliacao_do_usuario_filme < 0 or avaliacao_do_usuario_filme > 10:
                                        print('Nota inválida. Verifique se a nota digitada pertence ao intervalo de 0 a 10')
                                        print('Por favor, tente novamente mais tarde.')
                                    else:
                                        # Se tudo ocorrer certo, a avaliação será registrada no banco de dados
                                        for filme in Filme.catalogo_de_filmes:
                                            if filme["nome"] == usuario_nome_do_filme:
                                                filme["avaliacoes"].append(avaliacao_do_usuario_filme)
                                                filme["nota"] = float(f'{sum(filme["avaliacoes"]) / len(filme["avaliacoes"]):.2f}')
                                        subir_dados_filmes(Filme.catalogo_de_filmes)
                                        print('Avaliação cadastrada com sucesso!')
                                except ValueError:
                                    print('Erro! Verifique se o valor da avaliação é um número real')
                            else:
                                print('O filme digitado não foi encontrado')
                                print('Por favor, verique se o nome do filme foi inserido corretamente')
                        case '2':
                            print('Para que se possa avaliar uma série, é necessário primeiro digitar o nome da série a qual que se avaliar')

                            usuario_nome_da_serie = input('Digite o nome da série aqui: ').title()
                            # Função que verifica se a série digitada pelo usuário existe no banco de dados
                            encontrar_serie_para_avaliar = encontrar_serie_no_catalogo(usuario_nome_da_serie)

                            # Se a série existir, o processo de avaliação prossegue, caso contrário, o usuário é informado que a série digitada não foi encontrada
                            if encontrar_serie_para_avaliar:
                                try:
                                    # Estrutura que verifica se a nota digitada pelo usuário é válida
                                    avaliacao_do_usuario_serie = float(input(f'Indique aqui a nota que gostaria de atribuir ao filme "{usuario_nome_da_serie}": '))
                                    if avaliacao_do_usuario_serie < 0 or avaliacao_do_usuario_serie > 10:
                                        print('Nota inválida. Verifique se a nota digitada pertence ao intervalo de 0 a 10')
                                        print('Por favor, tente novamente mais tarde.')
                                    else:
                                        # Se tudo ocorrer certo, a avaliação será registrada no banco de dados
                                        for serie in Serie.catalogo_de_series:
                                            if serie["nome"] == usuario_nome_da_serie:
                                                serie["avaliacoes"].append(avaliacao_do_usuario_serie)
                                                serie["nota"] = float(f'{(sum(serie["avaliacoes"]) / len(serie["avaliacoes"]) / 2):.2f}')
                                        subir_dados_series(Serie.catalogo_de_series)
                                        print('Avaliação cadastrada com sucesso!')
                                except ValueError:
                                    print('Erro! Verifique se o valor da avaliação é um número real')
                            else:
                                print('A série digitada não foi encontrada')
                                print('Por favor, verifique se o nome da série foi inserida corretamente')
                        case '3':
                            print('Para que se possa avaliar um documentário, é necessário primeiro digitar o nome do documentário a qual se quer avaliar')

                            usuario_nome_do_documentario = input('Digite o nome do documentário aqui: ').title()
                            # Função que verifica se o documentário digitado pelo usuário existe no banco de dados
                            encontrar_documentario_para_avaliar = encontrar_documentario_no_catalogo(usuario_nome_do_documentario)

                            # Se o documentário existir, o processo de avaliação prossegue, caso contrário, o usuário é informado que o documentário digitado não foi encontrado
                            if encontrar_documentario_para_avaliar:
                                try:
                                    # Estrutura que verifica se a nota digitada pelo usuário é válida
                                    avaliacao_do_usuario_documentario = float(input(f'Indique aqui a nota que gostaria de atribuir ao documentário "{usuario_nome_do_documentario}": '))
                                    if avaliacao_do_usuario_documentario < 0 or avaliacao_do_usuario_documentario > 10:
                                        print('Nota inválida. Verifique se a nota digitada pertence ao intervalo de 0 a 10')
                                        print('Por favor, tente novamente mais tarde.')
                                    else:
                                        # Se tudo ocorrer certo, a avaliação será registrada no banco de dados
                                        for documentario in Documentario.catalogo_de_documentarios:
                                            if documentario["nome"] == usuario_nome_do_documentario:
                                                documentario["avaliacoes"].append(avaliacao_do_usuario_documentario)
                                                media_avaliacoes = float(f'{(sum(documentario["avaliacoes"]) / len(documentario["avaliacoes"])):.2f}')
                                                if media_avaliacoes >= 9.0:
                                                    documentario["nota"] = 'É um dos documentários campeões do catálogo 🏅'
                                                elif 7.5 <= media_avaliacoes < 9.0:
                                                    documentario["nota"] = 'É um documentário muito bem avaliado por quem já assistiu 🤩'
                                                elif 6.0 <= media_avaliacoes < 7.5:
                                                    documentario["nota"] = 'É um documentário que agrada diferentes parcelas 🙂'
                                                else:
                                                    documentario["nota"] = 'É um documentário que divide opiniões 😐'
                                        subir_dados_documentario(Documentario.catalogo_de_documentarios)
                                        print('Avaliação cadastrada com sucesso!')
                                except ValueError:
                                    print('Erro! Verifique se o valor da avaliação é um número real')
                            else:
                                print('O documentário digitado não foi encontrado')
                                print('Por favor, verifique se o nome do documentário foi inserido corretamente')
                        case _:
                            print('Por favor, digite uma opção válida')
                else:
                    print('Para que você possa avaliar um título, é necessário primeiro estar logado')
            case '6':
                # Estrutura que permite adicionar um título à lista de desejos
                # Estrutura condicional que verifica se o usuário está logado
                if status_de_login:
                    print('Digite qual categoria que gostaria de adicionar à lista de desejos')
                    exibir_categorias()
                    # Variável que armazena qual categoria o usuário deseja adicionar à lista de desejos
                    opcao_usuario_lista_de_desejos = input('Digite sua opção: ')
                    match opcao_usuario_lista_de_desejos:
                        case '1':
                            print('Lista de filmes disponíveis em catálogo:')
                            # Função que permite o usuário visualizar o catálogo de filmes disponíveis
                            Filme.listar_catalogo_de_filmes()
                            usuario_nome_do_filme_lista = input('Digite aqui o nome do filme que queira adicionar à lista de desejos: ').title()
                            # Função que verifica se o filme digitado pelo usuário existe no catálogo
                            encontrar_filme_lista = encontrar_filme_no_catalogo(usuario_nome_do_filme_lista)
                            # Se o filme existir, o processo de adição à lista de desejos prossegue, caso contrário, o usuário é informado que o filme digitado não foi encontrado
                            if encontrar_filme_lista:
                                # Estrutura que adiciona o filme desejado à lista de desejos do usuário
                                for filme in Filme.catalogo_de_filmes:
                                    if filme["nome"] == usuario_nome_do_filme_lista:
                                        with open(caminho_usuarios, 'r', encoding='utf-8') as arquivo_leitura_filme_usuarios:
                                            dados_usuarios_filme = json.load(arquivo_leitura_filme_usuarios)
                                        dados_usuarios_filme[nome_de_usuario_logado]["lista_de_desejos"][filme["nome"]] = filme["tempo_de_duracao_em_minutos"]
                                with open(caminho_usuarios, 'w', encoding='utf-8') as arquivo_alteracao_filme_usuarios:
                                    json.dump(dados_usuarios_filme, arquivo_alteracao_filme_usuarios, indent=4, ensure_ascii=False)
                                print('Filme adicionado à lista de desejos com sucesso!')
                            else:
                                print('O filme digitado não foi encontrado')
                                print('Por favor, verifique se o nome do filme foi inserido corretamente')
                        case '2':
                            print('Lista de séris disponíveis em catálogo:')
                            # Função que permite o usuário visualizar o catálogo de séries disponíveis
                            Serie.listar_catalogo_de_series()
                            usuario_nome_da_serie_lista = input('Digite aqui o nome da série que queira adicionar à lista de desejos: ').title()
                            # Função que verifica se a série digitada pelo usuário existe no catálogo
                            encontrar_serie_lista = encontrar_serie_no_catalogo(usuario_nome_da_serie_lista)
                            # Se a série existir, o processo de adição à lista de desejos prossegue, caso contrário, o usuário é informado que a série digitada não foi encontrada
                            if encontrar_serie_lista:
                                # Estrutura que adiciona a série desejada à lista de desejos do usuário
                                for serie in Serie.catalogo_de_series:
                                    if serie["nome"] == usuario_nome_da_serie_lista:
                                        with open(caminho_usuarios, 'r', encoding='utf-8') as arquivo_leitura_series_usuarios:
                                            dados_usuarios_serie = json.load(arquivo_leitura_series_usuarios)
                                        dados_usuarios_serie[nome_de_usuario_logado]["lista_de_desejos"][serie["nome"]] = serie["tempo_de_duracao_aproximado_em_minutos"]
                                with open(caminho_usuarios, 'w', encoding='utf-8') as arquivo_alteracao_serie_usuarios:
                                    json.dump(dados_usuarios_serie, arquivo_alteracao_serie_usuarios, indent=4, ensure_ascii=False)
                                print('Série adicionada à lista de desejos com sucesso!')
                            else:
                                print('A série digitada não foi encontrada')
                                print('Por favor, verifique se o nome da série foi inserida corretamente')
                        case '3':
                            print('Lista de documentários em catálogo:')
                            # Função que permite o usuário visualizar o catálogo de documentários disponíveis
                            Documentario.listar_documentarios()
                            usuario_nome_do_documentario_lista = input('Digite aqui o nome do documentário que queira adicionar à lista de desejos: ').title()
                            # Função que verifica se o documentário digitado pelo usuário existe no catálogo
                            encontrar_documentario_lista = encontrar_documentario_no_catalogo(usuario_nome_do_documentario_lista)
                            # Se o documentário existir, o processo de adição à lista de desejos prossegue, caso contrário, o usuário é informado que o documentário digitado não foi encontrado
                            if encontrar_documentario_lista:
                                # Estrutura que adiciona o documentário desejado à lista de desejos do usuário
                                for documentario in Documentario.catalogo_de_documentarios:
                                    if documentario["nome"] == usuario_nome_do_documentario_lista:
                                        with open(caminho_usuarios, 'r', encoding='utf-8') as arquivo_leitura_documentarios_usuarios:
                                            dados_usuarios_documentario = json.load(arquivo_leitura_documentarios_usuarios)
                                        dados_usuarios_documentario[nome_de_usuario_logado]["lista_de_desejos"][documentario["nome"]] = documentario["tempo_de_duracao_em_minutos"] 
                                with open(caminho_usuarios, 'w', encoding='utf-8') as arquivo_alteracao_documentario_usuarios:
                                    json.dump(dados_usuarios_documentario, arquivo_alteracao_documentario_usuarios, indent=4, ensure_ascii=False)
                                print('Documentário adicionado à lista de desejos com sucesso!')
                            else:
                                print('O documentário digitado não foi encontrado')
                                print('Por favor, verifique se o nome do documentário foi inserido corretamente')
                else:
                    print('Para que você possa adicionar um título à lista de desejos, é necessário primeiro estar logado')
            case '7':
                # Estrutura que exibe ao usuário os títulos adicionados à lista de desejos e permite visualizar o tempo de reprodução de todas as obras
                # Estrutura condicional que verifica se o usuário está logado
                if status_de_login:
                    print('Aqui estão todos os títulos que você já adicionou até o momento à sua lista de desejos:')
                    with open(caminho_usuarios, 'r', encoding='utf-8') as arquivo_leitura_tempo_de_maratona:
                        dados_usuarios_tempo_de_maratona = json.load(arquivo_leitura_tempo_de_maratona)
                    tempo_de_maratona = 0
                    for titulo in dados_usuarios_tempo_de_maratona[nome_de_usuario_logado]["lista_de_desejos"].keys():
                        print(titulo)
                        tempo_de_maratona += dados_usuarios_tempo_de_maratona[nome_de_usuario_logado]["lista_de_desejos"][titulo]
                    print(f'O tempo total para maratonar todos os títulos é de {tempo_de_maratona} min')
                else:
                    print('Para que você possa ver o tempo de reprodução total dos títulos adicionados à lista de desejos é necessário primeiro estar logado')
            case '8':
                # Estrutura que permite o usuário sair da conta caso o indivíduo esteja logado
                if status_de_login:
                    status_de_login = False
                    print('Deslogado com sucesso!')
                else:
                    print('Não é possível deslogar se você não estiver logado')
            case '9':
                # Estrutura que permite o usuário sair do programa
                print('Volte sempre :)')
                print('Encerrando o programa...')
                break
            case _:
                print('Por favor! Digite umas das opções disponíveis')


if __name__ == '__main__':
    app()

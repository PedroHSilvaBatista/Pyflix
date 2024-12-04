import os, json

# Caminhos que levam até seus respectivos arquivos
diretorio_atual = os.path.dirname(__file__)
caminho_filmes = os.path.join(diretorio_atual, '..', 'data', 'filmes.json')
caminho_series = os.path.join(diretorio_atual, '..', 'data', 'series.json')
caminho_documentarios = os.path.join(diretorio_atual, '..', 'data', 'documentarios.json')


def encontrar_filme_no_catalogo(nome_do_filme: str) -> bool:
    """Esta função verifica se o nome do filme digitado pelo usuário se encontra no banco de dados
    retorna True se o filme foi encontrado
    retorna False se o filme não foi encontrado"""
    with open(caminho_filmes, 'r', encoding='utf-8') as arquivo_filmes:
        dados_filmes = json.load(arquivo_filmes)
    for filme in dados_filmes:
        if filme["nome"].replace(' ', '') == nome_do_filme.replace(' ', ''):
            return True
    return False


def encontrar_serie_no_catalogo(nome_da_serie: str) -> bool:
    """Esta função verifica se o nome da série digitada pelo usuário se encontra no banco de dados
    retorna True se o filme foi encontrado
    retorna False se o filme não foi encontrado"""
    with open(caminho_series, 'r', encoding='utf-8') as arquivo_series:
        dados_series = json.load(arquivo_series)
    for serie in dados_series:
        if serie["nome"].replace(' ', '') == nome_da_serie.replace(' ', ''):
            return True
    return False


def encontrar_documentario_no_catalogo(nome_do_documentario: str) -> bool:
    """Esta função verifica se o nome do documentário digitado pelo usuário se encontra no banco de dados
    retorna True se o filme foi encontrado
    retorna False se o filme não foi encontrado"""
    with open(caminho_documentarios, 'r', encoding='utf-8') as arquivo_documentarios:
        dados_documentarios = json.load(arquivo_documentarios)
    for documentario in dados_documentarios:
        if documentario["nome"].replace(' ', '') == nome_do_documentario.replace(' ', ''):
            return True
    return False

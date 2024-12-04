import os, json

# Caminhos que levam até seu respectivo arquivo
diretorio_atual = os.path.dirname(__file__)
caminho_filme = os.path.join(diretorio_atual, '..', 'data', 'filmes.json')
caminho_serie = os.path.join(diretorio_atual, '..', 'data', 'series.json')
caminho_documentario = os.path.join(diretorio_atual, '..', 'data', 'documentarios.json')

def subir_dados_filmes(catalogo_de_filmes) -> None:
    """Esta função sobrescreve o banco de dados com qualquer tipo de alteração feita pelo usuário por meio das funncionalidade do menu
    e não possui retorno"""
    dados = [filme for filme in catalogo_de_filmes]
    with open(caminho_filme, 'w', encoding='utf-8') as arquivo_filme:
        json.dump(dados, arquivo_filme, indent=4, ensure_ascii=False)


def subir_dados_series(catalogo_de_series) -> None:
    """Esta função sobrescreve o banco de dados com qualquer tipo de alteração feita pelo usuário por meio das funncionalidade do menu
    e não possui retorno"""
    dados = [serie for serie in catalogo_de_series]
    with open(caminho_serie, 'w', encoding='utf-8') as arquivo_serie:
        json.dump(dados, arquivo_serie, indent=4, ensure_ascii=False)


def subir_dados_documentario(catalogo_de_documentarios) -> None:
    """Esta função sobrescreve o banco de dados com qualquer tipo de alteração feita pelo usuário por meio das funncionalidade do menu
    e não possui retorno"""
    dados = [documentario for documentario in catalogo_de_documentarios]
    with open(caminho_documentario, 'w', encoding='utf-8') as arquivo_documentario:
        json.dump(dados, arquivo_documentario, indent=4, ensure_ascii=False)

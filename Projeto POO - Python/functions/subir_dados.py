import os, json

diretorio_atual = os.path.dirname(__file__)
caminho_filme = os.path.join(diretorio_atual, '..', 'data', 'filmes.json')


def subir_dados_filme(catalogo_de_filmes):
    dados = [filme.serializar_objeto() for filme in catalogo_de_filmes]
    with open(caminho_filme, 'w', encoding='utf-8') as arquivo_filme:
        json.dump(dados, arquivo_filme, indent=4, ensure_ascii=False)

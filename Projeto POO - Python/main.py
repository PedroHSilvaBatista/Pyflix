from fastapi import FastAPI
import os, json

diretorio_atual = os.path.dirname(__file__)
caminho_usuarios = os.path.join(diretorio_atual, 'data', 'usuarios.json')
caminho_filmes = os.path.join(diretorio_atual, 'data', 'filmes.json')
caminho_series = os.path.join(diretorio_atual, 'data', 'series.json')
caminho_documentarios = os.path.join(diretorio_atual, 'data', 'documentarios.json')

app = FastAPI()

with open(caminho_usuarios, 'r', encoding='utf-8') as arquivo_usuarios:
    dados_usuarios_api = json.load(arquivo_usuarios)

with open(caminho_filmes, 'r', encoding='utf-8') as arquivo_filmes:
    dados_filmes_api = json.load(arquivo_filmes)

with open(caminho_series, 'r', encoding='utf-8') as arquivo_series:
    dados_series_api = json.load(arquivo_series)

with open(caminho_documentarios, 'r', encoding='utf-8') as arquivo_documentarios:
    dados_documentarios_api = json.load(arquivo_documentarios)


@app.get('/api/usuarios/')
def usuarios():
    return dados_usuarios_api

@app.get('/api/filmes/')
def filmes():
    return dados_filmes_api

@app.get('/api/series/')
def series():
    return dados_series_api

@app.get('/api/documentarios/')
def documentarios():
    return dados_documentarios_api

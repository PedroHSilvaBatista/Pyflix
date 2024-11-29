from models.titulo import Titulo

import os, json

diretorio_atual = os.path.dirname(__file__)
caminho_documentarios = os.path.join(diretorio_atual, '..', 'data', 'documentarios.json')


class Documentario(Titulo):

    with open(caminho_documentarios, 'r', encoding='utf-8') as arquivo_leitura:
        dados_json = json.load(arquivo_leitura)

    if dados_json:
        catalogo_de_documentarios = [documentario for documentario in dados_json]
    else:
        catalogo_de_documentarios = []

    def __init__(self, nome, ano_de_lancamento, tempo_de_duracao, categoria, sinopse, autor, tema, primeira_nota):
        super().__init__(nome, ano_de_lancamento, tempo_de_duracao, categoria, sinopse)
        self._autor = autor
        self._tema = tema
        self._avaliacoes = [primeira_nota]
        Documentario.catalogo_de_documentarios.append(self.serializar_objeto())

    def __str__(self) -> str:
        """Esta função retorna uma representação em string do documentário com algumas informações importantes"""
        return f'Nome: {self._nome} | Ano de Lançamento: {self._ano_de_lancamento} | Tema: {self._tema}'
    
    @classmethod
    def listar_documentarios(cls) -> None:
        """Esta função lista todos os documentários já registradas e não possui retorno"""
        if cls.catalogo_de_documentarios:
            print(f'{"Nome".ljust(25)} | {"Autor".ljust(25)} | {"Tema".ljust(25)} | {"Nota".ljust(25)}')
            for documentario in cls.catalogo_de_documentarios:
                print(f'{documentario["nome"].ljust(25)} | {documentario["autor"].ljust(25)} | {documentario["tema"].ljust(25)} | {documentario["nota"]}')
        else:
            print('Nenhuma série registrada até o momento 😕')
    
    @property
    def getclassificacao(self) -> str:
        """Esta função calcula a média de avaliações da lista de avaliações e retorna uma mensagem em forma de string
        com base na média obtida"""
        if not self.getavaliacoes:
            return 'Nenhuma avaliação registrada no momento 😕'
        avaliacao_media = sum(self._avaliacoes) / len(self._avaliacoes)
        if avaliacao_media >= 9.0:
            return 'É um dos documentários campeões do catálogo 🏅'
        elif 7.5 <= avaliacao_media < 9.0:
            return 'É um documentário muito bem avaliado por quem já assistiu 🤩'
        elif 6.0 <= avaliacao_media < 7.5:
            return 'É um documentário que agrada diferentes parcelas 🙂'
        else:
            return 'É um documentário que divide opiniões 😐'

    @property
    def getnome(self):
        return self._nome
    
    @property
    def getanodelancamento(self):
        return self._ano_de_lancamento
    
    @property
    def gettempodeduracao(self):
        return self._tempo_de_duracao
    
    @property
    def getcategoria(self):
        return self._categoria
    
    @property
    def getsinopse(self):
        return self._sinopse
    
    @property
    def getautor(self):
        return self._autor
    
    @property
    def gettema(self):
        return self._tema
    
    @property
    def getavaliacoes(self):
        return self._avaliacoes

    def serializar_objeto(self):
        return {
            "nome": self.getnome,
            "ano_de_lancamento": self.getanodelancamento,
            "tempo_de_duracao_em_minutos": self.gettempodeduracao,
            "categoria": self.getcategoria,
            "sinopse": self.getsinopse,
            "autor": self.getautor,
            "tema": self.gettema,
            "avaliacoes": self.getavaliacoes,
            "nota": self.getclassificacao
        }

from models.titulo import Titulo

import os, json

diretorio_atual = os.path.dirname(__file__)
caminho_filmes = os.path.join(diretorio_atual, '..', 'data', 'filmes.json')


class Filme(Titulo):

    with open(caminho_filmes, 'r', encoding='utf-8') as arquivo_leitura:
        dados_json = json.load(arquivo_leitura)
    if dados_json:
        catalogo_de_filmes = [filme for filme in dados_json]
    else:
        catalogo_de_filmes = []

    def __init__(self, nome, ano_de_lancamento, tempo_de_duracao, categoria, sinopse, diretor, estudio, primeira_nota):
        super().__init__(nome, ano_de_lancamento, tempo_de_duracao, categoria, sinopse)
        self._diretor = diretor
        self._estudio = estudio
        self._avaliacoes = [primeira_nota]
        Filme.catalogo_de_filmes.append(self.serializar_objeto())

    @property
    def getclassificacao(self) -> float:
        """Esta função calcula a média de avaliações da lista de avaliações e retorna o resultado"""
        if self.getavaliacoes:
            return float(f'{sum(self.getavaliacoes) / len(self.getavaliacoes):2f}')
        print('Nenhuma avaliação registrada no momento 😕')
    
    def __str__(self) -> str:
        """Esta função retorna uma representação em string do filme com algumas informações importantes"""
        return f'Nome: {self._nome} | Ano de Lançamento: {self._ano_de_lancamento}'
    
    @classmethod
    def listar_catalogo_de_filmes(cls) -> None:
        """Esta função lista todos os filmes já registrados e não possui retorno"""
        if cls.catalogo_de_filmes:
            print(f'{"Nome".ljust(25)} | {"Ano de Lançamento".ljust(25)} | {"Gênero Principal".ljust(25)}')
            for filme in cls.catalogo_de_filmes:
                print(f'{filme["nome"].ljust(25)} | {str(filme["ano_de_lancamento"]).ljust(25)} | {filme["categorias"][0].ljust(25)}')
        else:
            print('Nenhum filme registrado até o momento 😕')

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
    def getdiretor(self):
        return self._diretor
    
    @property
    def getestudio(self):
        return self._estudio

    @property
    def getavaliacoes(self):
        return self._avaliacoes
    
    def serializar_objeto(self):
        return {
            "nome": self.getnome,
            "ano_de_lancamento": self.getanodelancamento,
            "tempo_de_duracao_em_minutos": self.gettempodeduracao,
            "categorias": self.getcategoria,
            "sinopse": self.getsinopse,
            "diretor": self.getdiretor,
            "estudio": self.getestudio,
            "avaliacoes": self.getavaliacoes,
            "nota": self.getclassificacao,
        }

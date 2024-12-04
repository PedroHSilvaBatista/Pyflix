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
    def get_classificacao(self) -> float:
        """Esta função calcula a média de avaliações da lista de avaliações e retorna o resultado"""
        if self.get_avaliacoes:
            return float(f'{sum(self.get_avaliacoes) / len(self.get_avaliacoes):2f}')
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
    def get_nome(self):
        return self._nome
    
    @property
    def get_anodelancamento(self):
        return self._ano_de_lancamento
    
    @property
    def get_tempodeduracao(self):
        return self._tempo_de_duracao

    @property
    def get_categoria(self):
        return self._categoria
    
    @property
    def get_sinopse(self):
        return self._sinopse
    
    @property
    def get_diretor(self):
        return self._diretor
    
    @property
    def get_estudio(self):
        return self._estudio

    @property
    def get_avaliacoes(self):
        return self._avaliacoes
    
    def serializar_objeto(self):
        """Esta função serializa um objeto e retorna um dicionário que contém as informações de cada atributo"""
        return {
            "nome": self.get_nome,
            "ano_de_lancamento": self.get_anodelancamento,
            "tempo_de_duracao_em_minutos": self.get_tempodeduracao,
            "categorias": self.get_categoria,
            "sinopse": self.get_sinopse,
            "diretor": self.get_diretor,
            "estudio": self.get_estudio,
            "avaliacoes": self.get_avaliacoes,
            "nota": self.get_classificacao,
        }

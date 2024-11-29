from models.titulo import Titulo

import os, json

diretorio_atual = os.path.dirname(__file__)
caminho_series = os.path.join(diretorio_atual, '..', 'data', 'series.json')


class Serie(Titulo):
    
    with open(caminho_series, 'r', encoding='utf-8') as arquivo_leitura:
        dados_json = json.load(arquivo_leitura)
    
    if dados_json:
        catalogo_de_series = [serie for serie in dados_json]
    else:
        catalogo_de_series = []

    def __init__(self, nome, ano_de_lancamento, tempo_de_duracao, categoria, sinopse, numero_de_temporadas, numero_de_episodios, primeira_nota):
        super().__init__(nome, ano_de_lancamento, tempo_de_duracao, categoria, sinopse)
        self._numero_de_temporadas = numero_de_temporadas
        self._numero_de_episodios = numero_de_episodios
        self._avaliacoes = [primeira_nota]
        Serie.catalogo_de_series.append(self.serializar_objeto())

    def __str__(self) -> str:
        """Esta função retorna uma representação em string da série com algumas informações importantes"""
        return f'Nome: {self._nome} | Ano de Lançamento: {self._ano_de_lancamento} | Gênero:  {self._categoria}'

    @classmethod
    def listar_catalogo_de_series(cls) -> None:
        """Esta função lista todos as séries já registradas e não possui retorno"""
        if cls.catalogo_de_series:
            print(f'{"Nome".ljust(25)} |{"Ano de Lancamento".ljust(25)} | {"Gênero".ljust(25)} | {"Nota".ljust(25)}')
            for serie in cls.catalogo_de_series:
                print(f'{serie["nome"].ljust(25)} |{str(serie["ano_de_lancamento"]).ljust(25)} | {serie["categorias"][0].ljust(25)} | {serie["nota"]}')
        else:
            print('Nenhuma série registrada até o momento 😕')
    
    @property
    def getclassificacao(self) -> str:
        """Esta função calcula a média de avaliações da lista de avaliações e retorna o resultado em forma de string"""
        if self.getavaliacoes:
            return float(f'{(sum(self._avaliacoes) / len(self._avaliacoes) / 2):.2f}')
        return 'Nenhuma avaliação registrada no momento 😕'
    
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
    def getnumerodetemporadas(self):
        return self._numero_de_temporadas
    
    @property
    def getnumerodeepisodios(self):
        return self._numero_de_episodios
    
    @property
    def getavaliacoes(self):
        return self._avaliacoes
    
    def serializar_objeto(self):
        return {
            "nome": self.getnome,
            "ano_de_lancamento": self.getanodelancamento,
            "tempo_de_duracao_aproximado_em_minutos": self.gettempodeduracao,
            "categorias": self.getcategoria,
            "sinopse": self.getsinopse,
            "numero_de_temporadas": self.getnumerodetemporadas,
            "numero_aproximado_de_episodios": self.getnumerodeepisodios,
            "avaliacoes": self.getavaliacoes,
            "nota": self.getclassificacao,
        }

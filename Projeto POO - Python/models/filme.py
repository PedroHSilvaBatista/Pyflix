from models.titulo import Titulo

import os, json

diretorio_atual = os.path.dirname(__file__)
caminho_filmes = os.path.join(diretorio_atual, '..', 'data', 'filmes.json')


class Filme(Titulo):

    with open(caminho_filmes, 'r', encoding='utf-8') as arquivo_leitura:
        dados_json = json.load(arquivo_leitura)
    catalogo_de_filmes = [filme for filme in dados_json]

    def __init__(self, nome, ano_de_lancamento, tempo_de_duracao, categoria, sinopse, diretor, estudio):
        super().__init__(nome, ano_de_lancamento, tempo_de_duracao, categoria, sinopse)
        self._diretor = diretor
        self._estudio = estudio
        self._avaliacoes = []
        Filme.catalogo_de_filmes.append(self.serializar_objeto())

    def __str__(self) -> str:
        """Esta função retorna uma representação em string do filme com algumas informações importantes"""
        return f'Nome: {self._nome} | Ano de Lançamento: {self._ano_de_lancamento}'
    
    def avaliar(self, nota) -> None:
        """Esta função atribui uma nota a lista de avaliações do objeto e não possui retorno"""
        if type(nota) == float or type(nota) == int:
            if nota < 0 or nota > 10:
                print('Nota inválida. Verifique se a nota digitada pertence ao intervalo de 0 a 10')
                print('Por favor, tente novamente mais tarde.')
            else:
                self._avaliacoes.append(nota)
        else:
            print('Erro. Por favor, digite um valor real para a atribuição da nota')

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
    def getclassificacao(self) -> float:
        """Esta função calcula a média de avaliações da lista de avaliações e retorna o resultado"""
        if not self._avaliacoes:
            return 'Nenhuma avaliação registrada no momento 😕'
        return f'{sum(self._avaliacoes) / len(self._avaliacoes):2f}'

    # Criar uma classmethod para listar todos os filmes do catálogo
    @classmethod
    def listar_catalogo_de_filmes(cls) -> None:
        """Esta função lista todos os filmes já registrados e não possui retorno"""
        with open(caminho_filmes, 'r', encoding='utf-8') as arquivo_ler_filmes:
            dados_json = json.load(arquivo_ler_filmes)
        print(f'{"Nome".ljust(25)} | {"Ano de Lançamento".ljust(25)} | {"Gênero Principal".ljust(25)}')
        for filme in dados_json:
            print(f'{filme["nome"].ljust(25)} | {str(filme["ano_de_lancamento"]).ljust(25)} | {filme["categorias"][0].ljust(25)}')

    # Montar uma ficha técnica do filme, de modo a exibir todas as informações do filme
    def exibir_ficha_tecnica(self) -> None:
        """Esta função exibe a ficha técnica completa de um filme e não possui retorno"""
        print('-=' * 35)
        print(f'Filme: {self._nome}')
        print(f'Ano: {self._ano_de_lancamento}')

        print(f'Gênero: ', end='')
        generos = self._categoria
        for i in range(len(generos)):
            if i == len(generos) - 1:
                print(f'{generos[i]}', end='')
            else:
                print(f'{generos[i]} ● ', end='')

        print(f'\nDiretor: {self._diretor}')
        print(f'Stúdio: {self._estudio}')
        print(f'Sinopse: {self._sinopse}')
        print('-=' * 35)
    
    def serializar_objeto(self):
        return {
            "nome": self.getnome,
            "ano_de_lancamento": self.getanodelancamento,
            "tempo_de_duracao_em_minutos": self.gettempodeduracao,
            "categorias": self.getcategoria,
            "sinopse": self.getsinopse,
            "diretor": self.getdiretor,
            "estudio": self.getestudio,
            "nota": self.getclassificacao,
        }

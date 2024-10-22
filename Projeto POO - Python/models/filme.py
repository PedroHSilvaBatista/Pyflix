from titulo import Titulo

class Filme(Titulo):

    catalogo_de_filmes = []

    def __init__(self, nome, ano_de_lancamento, tempo_de_duracao, categoria, sinopse, diretor, studio):
        super().__init__(nome, ano_de_lancamento, tempo_de_duracao, categoria, sinopse)
        self._diretor = diretor
        self._studio = studio
        self._avaliacoes = []
        Filme.catalogo_de_filmes.append(self)

    def __str__(self):
        return f'Nome: {self._nome} | Ano de Lançamento: {self._ano_de_lancamento}'
    
    def avaliar(self, nota):
        self._avaliacoes.append(nota)

    @property
    def getclassificacao(self):
        return sum(self._avaliacoes) / len(self._avaliacoes)

    # Criar uma classmethod para listar todos os filmes do catálogo

    @classmethod
    def listar_filmes(cls):
        print('Nome do filme | Ano de lançamento | Categoria')
        for filme in cls.catalogo_de_filmes:
            print(f'{filme._nome} | {filme._ano_de_lancamento} | {filme._categoria}')
        


filme1 = Filme('Homem-Aranha: Através do Aranhaverso', 2023, 140, 'Animação', 'Depois de se reunir com Gwen Stacy, Homem-Aranha é jogado no multiverso. Lá, o super-herói aracnídeo encontra uma numerosa equipe encarregada de proteger sua própria existência.', 'Joaquim Dos Santos', 'Sony Pictures Animation')

#print(filme1)

Filme.listar_filmes()

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
        print(f'{"Nome".ljust(25)} | {"Ano de Lançamento".ljust(25)} | {"Gênero".ljust(25)}')
        for filme in cls.catalogo_de_filmes:
            print(f'{filme._nome.ljust(25)} | {str(filme._ano_de_lancamento).ljust(25)} | {filme._categoria.ljust(25)}')

    # Montar uma ficha técnica do filme, de modo a exibir todas as informações do filme

    def exibir_ficha_tecnica(self):
        ficha_tecnica = f'''
        Filme: {str(self._nome)}
        Ano: {str(self._ano_de_lancamento)}
        Gênero: {str(self._categoria)}
        Sinopse: {str(self._sinopse)}
        Diretor: {str(self._diretor)}
        Stúdio: {str(self._studio)}
        '''
        print('-=' * 35)
        print(ficha_tecnica)
        print('-=' * 35)
        


filme1 = Filme('O Poderoso Chefão', 1972, 275, 'Crime', 'Uma família mafiosa luta para estabelecer sua supremacia nos Estados Unidos depois da Segunda Guerra Mundial. Uma tentativa de assassinato deixa o chefão Vito Corleone incapacitado e força os filhos Michael e Sonny a assumir os negócios.', 'Francis Ford Coppola', 'Paramount Pictures')


Filme.listar_filmes()
filme1.avaliar(10)

print(filme1.getclassificacao)

filme1.exibir_ficha_tecnica()
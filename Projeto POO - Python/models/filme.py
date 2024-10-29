from models.titulo import Titulo

class Filme(Titulo):

    catalogo_de_filmes = []

    def __init__(self, nome, ano_de_lancamento, tempo_de_duracao, categoria, sinopse, diretor, studio):
        super().__init__(nome, ano_de_lancamento, tempo_de_duracao, categoria, sinopse)
        self._diretor = diretor
        self._studio = studio
        self._avaliacoes = []
        Filme.catalogo_de_filmes.append(self)

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
    def getclassificacao(self) -> float:
        """Esta função calcula a média de avaliações da lista de avaliações e retorna o resultado"""
        if not self._avaliacoes:
            return 'Nenhuma avaliação registrada no momento 😕'
        return sum(self._avaliacoes) / len(self._avaliacoes)

    # Criar uma classmethod para listar todos os filmes do catálogo

    @classmethod
    def listar_filmes(cls) -> None:
        """Esta função lista todos os filmes já registrados e não possui retorno"""
        print(f'{"Nome".ljust(25)} | {"Ano de Lançamento".ljust(25)} | {"Gênero Principal".ljust(25)}')
        for filme in cls.catalogo_de_filmes:
            print(f'{filme._nome.ljust(25)} | {str(filme._ano_de_lancamento).ljust(25)} | {filme._categoria[0].ljust(25)}')

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
        print(f'Stúdio: {self._studio}')
        print(f'Sinopse: {self._sinopse}')
        print('-=' * 35)


# Não se esqueça que os objetos da classe serão salvos em arquivos json

generos = ['Crime', 'Ação', 'Clássico']

filme1 = Filme('O Poderoso Chefão', 1972, 275, generos, 'Uma família mafiosa luta para estabelecer sua supremacia nos Estados Unidos depois da Segunda Guerra Mundial. Uma tentativa de assassinato deixa o chefão Vito Corleone incapacitado e força os filhos Michael e Sonny a assumir os negócios.', 'Francis Ford Coppola', 'Paramount Pictures')

Filme.listar_filmes()
filme1.avaliar(10)

print(filme1.getclassificacao)

filme1.exibir_ficha_tecnica()

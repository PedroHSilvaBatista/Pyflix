from models.titulo import Titulo

class Filme(Titulo):

    catalogo_de_filmes = []

    def __init__(self, nome, ano_de_lancamento, tempo_de_duracao, categoria, sinopse, diretor, estudio):
        super().__init__(nome, ano_de_lancamento, tempo_de_duracao, categoria, sinopse)
        self._diretor = diretor
        self._estudio = estudio
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


filme1 = Filme('O Poderoso Chefão', 1972, 175, ['Crime', 'Ação', 'Clássico'], 'Uma família mafiosa luta para estabelecer sua supremacia nos Estados Unidos depois da Segunda Guerra Mundial. Uma tentativa de assassinato deixa o chefão Vito Corleone incapacitado e força os filhos Michael e Sonny a assumir os negócios.', 'Francis Ford Coppola', 'Paramount Pictures')
filme1.avaliar(10)
filme1.avaliar(9.75)
filme1.avaliar(9.50)

filme2 = Filme('Matrix', 1999, 136, ['Ação', 'Sci-Fi', 'Cyberpunk'], 'Um hacker aprende com os misteriosos rebeldes sobre a verdadeira natureza de sua realidade e seu papel na guerra contra seus controladores.', 'Lana Wachowski', 'Warner Bros. Entertainment')
filme2.avaliar(9.0)
filme2.avaliar(8.5)
filme2.avaliar(9.50)

filme3 = Filme('Oppenheimer', 2023, 180, ['Drama', 'History', 'Biografia'], 'A história do cientista americano J. Robert Oppenheimer e seu papel no desenvolvimento da bomba atômica.', 'Christopher Nolan', 'Universal Studios')
filme3.avaliar(9.0)
filme3.avaliar(8.0)
filme3.avaliar(8.8)

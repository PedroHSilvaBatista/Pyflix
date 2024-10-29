from models.titulo import Titulo

class Serie(Titulo):
    
    catalogo_series = []

    def __init__(self, nome, ano_de_lancamento, tempo_de_duracao, categoria, sinopse, numero_de_temporadas, numero_de_episodios):
        super().__init__(nome, ano_de_lancamento, tempo_de_duracao, categoria, sinopse)
        self._numero_de_temporadas = numero_de_temporadas
        self._numero_de_episodios = numero_de_episodios
        self._avaliacoes = []
        Serie.catalogo_series.append(self)

    
    def __str__(self) -> str:
        """Esta função retorna uma representação em string da série com algumas informações importantes"""
        return f'Nome: {self._nome} | Ano de Lançamento: {self._ano_de_lancamento} | Gênero:  {self._categoria}'
    
    # Nota não pode ser acima de 10 e muito menos negativa (Faça a validação)
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
    def _getclassificacao(self) -> str:
        """Esta função calcula a média de avaliações da lista de avaliações e retorna o resultado em forma de string"""
        if not self._avaliacoes:
            return 'Nenhuma avaliação registrada no momento 😕'
        return f'{(sum(self._avaliacoes) / len(self._avaliacoes) / 2):.2f}'

    @classmethod
    def listar_series(cls) -> None:
        """Esta função lista todos as séries já registradas e não possui retorno"""
        print(f'{"Nome".ljust(25)} |{"Ano de Lancamento".ljust(25)} | {"Gênero".ljust(25)} | {"Nota".ljust(25)}')
        for serie in cls.catalogo_series:
            print(f'{serie._nome.ljust(25)} |{str(serie._ano_de_lancamento).ljust(25)} | {serie._categoria[0].ljust(25)} | {serie._getclassificacao} ⭐')
    
    def exibir_ficha_tecnica(self) -> None:
        """Esta função exibe a ficha técnica completa de uma série e não possui retorno"""
        print('-=' * 35)
        print(f'Série: {self._nome}')
        print(f'Ano: {self._ano_de_lancamento}')
        print(f'Gêneros: ', end='')

        generos = self._categoria
        for i in range(len(generos)):
            if i == len(generos) - 1:
                print(f'{generos[i]}', end='')
            else:
                print(f'{generos[i]} ● ', end='')
        
        print(f'\nTemporadas: {self._numero_de_temporadas}')
        print(f'Número de episódios: {self._numero_de_episodios}')
        print(f'Sinopse: {self._sinopse}')
        print('-=' * 35)
       

# Não se esqueça que os objetos da classe serão salvos em arquivos json

genero = ['Comédia', 'Irreverente', 'Sitcom']

serie = Serie('The Office', 2005, 2000, genero, 'Esta adaptação americana se passa em uma empresa de papel em Scranton, Pensilvânia e tem um estilo de documentário semelhante ao original britânico estrelado por Ricky Gervais.', 9, 201)
serie.avaliar(10)


serie2 = Serie('Vikings', 2013, 2500, ['Aventura'], 'A série acompanha a saga dos navegadores nórdicos que exploram - e conquistam - novos territórios nos tempos medievais.', 6, 14)
serie2.avaliar(9)

Serie.listar_series()

serie.exibir_ficha_tecnica()

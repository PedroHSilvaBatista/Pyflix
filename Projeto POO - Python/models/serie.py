from models.titulo import Titulo

class Serie(Titulo):
    
    catalogo_de_series = []

    def __init__(self, nome, ano_de_lancamento, tempo_de_duracao, categoria, sinopse, numero_de_temporadas, numero_de_episodios):
        super().__init__(nome, ano_de_lancamento, tempo_de_duracao, categoria, sinopse)
        self._numero_de_temporadas = numero_de_temporadas
        self._numero_de_episodios = numero_de_episodios
        self._avaliacoes = []
        Serie.catalogo_de_series.append(self)

    
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

    
    def serializar_objeto(self):
        return {
            "nome": self.getnome,
            "ano_de_lancamento": self.getanodelancamento,
            "tempo_de_duracao_aproximado_em_minutos": self.gettempodeduracao,
            "categorias": self.getcategoria,
            "sinopse": self.getsinopse,
            "numero_de_temporadas": self.getnumerodetemporadas,
            "numero_aproximado_de_episodios": self.getnumerodeepisodios,
            "nota": self._getclassificacao,
        }
       

# Não se esqueça que os objetos da classe serão salvos em arquivos json

serie1 = Serie('The Office', 2005, 4560, ['Comédia', 'Irreventes', 'Sitcom'], 'Esta adaptação americana se passa em uma empresa de papel em Scranton, Pensilvânia e tem um estilo de documentário semelhante ao original britânico estrelado por Ricky Gervais.', 9, 201)
serie1.avaliar(9.5)
serie1.avaliar(8.5)
serie1.avaliar(9.0)

serie2 = Serie('Vikings', 2013, 3916, ['História', 'Ação', 'Drama'], 'A série acompanha a saga dos navegadores nórdicos que exploram - e conquistam - novos territórios nos tempos medievais.', 6, 89)
serie2.avaliar(8.5)
serie2.avaliar(9.0)
serie2.avaliar(8.0)

serie3 = Serie('Brooklyn Nine-Nine', 2013, 3366, ['Comédia', 'Sitcom', 'Policial'], 'Jake Peralta é um detetive brilhante e ao mesmo tempo imaturo, que nunca precisou se preocupar em respeitar as regras. Tudo muda quando um capitão exigente assume o comando de seu esquadrão e Jake deve aprender a trabalhar em equipe.', 8, 153)
serie3.avaliar(9.1)
serie3.avaliar(7.9)
serie3.avaliar(8.4)

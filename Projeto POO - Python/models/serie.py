from titulo import Titulo

class Serie(Titulo):
    
    catalogo_series = []

    def __init__(self, nome, ano_de_lancamento, tempo_de_duracao, categoria, sinopse, numero_de_temporadas, numero_de_episodios_temporada):
        super().__init__(nome, ano_de_lancamento, tempo_de_duracao, categoria, sinopse)
        self._numero_de_temporadas = numero_de_temporadas
        self._numero_de_episodios_temporada = numero_de_episodios_temporada
        self._avaliacoes = []
        Serie.catalogo_series.append(self)

    
    def __str__(self):
        return f'Nome: {self._nome} | Ano de Lançamento: {self._ano_de_lancamento} | Gênero:  {self._categoria}'
    
    def avaliar(self, nota):
        self._avaliacoes.append(nota)

    @property
    def _getclassificacao(self):
        return f'{(sum(self._avaliacoes) / len(self._avaliacoes) / 2):.2f}'

    @classmethod
    def listar_series(cls):
        print(f'{"Nome".ljust(25)} |{"Ano de Lancamento".ljust(25)} | {"Gênero".ljust(25)} | {"Nota".ljust(25)}')
        for serie in cls.catalogo_series:
            print(f'{serie._nome.ljust(25)} |{str(serie._ano_de_lancamento).ljust(25)} | {serie._categoria.ljust(25)} | {serie._getclassificacao} ⭐')
    
    def exibir_ficha_tecnica(self):
        ficha_tecnica = f'''
        Série: {str(self._nome)}
        Ano: {str(self._ano_de_lancamento)}
        Gênero: {str(self._categoria)}
        Sinopse: {str(self._sinopse)}
        Temporadas: {str(self._numero_de_temporadas)}
        Número de episódios por temporada: {str(self._numero_de_episodios_temporada)}
        '''
        print('-=' * 35)
        print(ficha_tecnica)
        print('-=' * 35)
       
    
    # Montar uma ficha técnica da série, de modo a exibir todas as informações essencias da série
        
serie = Serie('The Office', 2005, 2000, 'Comédia', 'Esta adaptação americana se passa em uma empresa de papel em Scranton, Pensilvânia e tem um estilo de documentário semelhante ao original britânico estrelado por Ricky Gervais.', 9, 12)
serie.avaliar(10)


serie2 = Serie('Vikings', 2013, 2500, 'Aventura', 'A série acompanha a saga dos navegadores nórdicos que exploram - e conquistam - novos territórios nos tempos medievais.', 6, 14)
serie2.avaliar(9)

Serie.listar_series()

serie.exibir_ficha_tecnica()
from abc import abstractmethod

class Titulo():
    def __init__(self, nome, ano_de_lancamento, tempo_de_duracao, categoria, sinopse):
        self._nome = nome
        self._ano_de_lancamento = ano_de_lancamento
        self._tempo_de_duracao = tempo_de_duracao
        self._categoria = categoria
        self._sinopse = sinopse
    
    @abstractmethod
    def getclassificacao():
        pass

from abc import abstractmethod

class Titulo():
    def __init__(self, nome, ano_de_lancamento, tempo_de_duracao, categoria, sinopse):
        self._nome = nome
        self._ano_de_lancamento = ano_de_lancamento
        self._tempo_de_duracao = tempo_de_duracao
        self._categoria = categoria
        self._sinopse = sinopse
        self._avaliacao = 0

    @abstractmethod
    def avaliar(self, nota):
        pass
    
    @abstractmethod
    def getclassificacao():
        pass

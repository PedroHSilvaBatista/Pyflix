from models.titulo import Titulo

import os, json

diretorio_atual = os.path.dirname(__file__)
caminho_documentarios = os.path.join(diretorio_atual, '..', 'data', 'documentarios.json')


class Documentario(Titulo):

    with open(caminho_documentarios, 'r', encoding='utf-8') as arquivo_leitura:
        dados_json = json.load(arquivo_leitura)

    if dados_json:
        catalogo_de_documentarios = [documentario for documentario in dados_json]
    else:
        catalogo_de_documentarios = []

    def __init__(self, nome, ano_de_lancamento, tempo_de_duracao, categoria, sinopse, autor, tema, primeira_nota):
        super().__init__(nome, ano_de_lancamento, tempo_de_duracao, categoria, sinopse)
        self._autor = autor
        self._tema = tema
        self._avaliacoes = [primeira_nota]
        Documentario.catalogo_de_documentarios.append(self.serializar_objeto())

    def __str__(self) -> str:
        """Esta função retorna uma representação em string do documentário com algumas informações importantes"""
        return f'Nome: {self._nome} | Ano de Lançamento: {self._ano_de_lancamento} | Tema: {self._tema}'
    
    @classmethod
    def listar_documentarios(cls) -> None:
        """Esta função lista todos os documentários já registradas e não possui retorno"""
        if cls.catalogo_de_documentarios:
            print(f'{"Nome".ljust(25)} | {"Autor".ljust(25)} | {"Tema".ljust(25)} | {"Nota".ljust(25)}')
            for documentario in cls.catalogo_de_documentarios:
                print(f'{documentario["nome"].ljust(25)} | {documentario["autor"].ljust(25)} | {documentario["tema"].ljust(25)} | {documentario["nota"]}')
        else:
            print('Nenhuma série registrada até o momento 😕')
    
    @property
    def get_classificacao(self) -> str:
        """Esta função calcula a média de avaliações da lista de avaliações e retorna uma mensagem em forma de string
        com base na média obtida"""
        if not self.get_avaliacoes:
            return 'Nenhuma avaliação registrada no momento 😕'
        avaliacao_media = sum(self.get_avaliacoes) / len(self.get_avaliacoes)
        if avaliacao_media >= 9.0:
            return 'É um dos documentários campeões do catálogo 🏅'
        elif 7.5 <= avaliacao_media < 9.0:
            return 'É um documentário muito bem avaliado por quem já assistiu 🤩'
        elif 6.0 <= avaliacao_media < 7.5:
            return 'É um documentário que agrada diferentes parcelas 🙂'
        else:
            return 'É um documentário que divide opiniões 😐'

    @property
    def get_nome(self):
        return self._nome
    
    @property
    def get_anodelancamento(self):
        return self._ano_de_lancamento
    
    @property
    def get_tempodeduracao(self):
        return self._tempo_de_duracao
    
    @property
    def get_categoria(self):
        return self._categoria
    
    @property
    def get_sinopse(self):
        return self._sinopse
    
    @property
    def get_autor(self):
        return self._autor
    
    @property
    def get_tema(self):
        return self._tema
    
    @property
    def get_avaliacoes(self):
        return self._avaliacoes

    def serializar_objeto(self):
        """Esta função serializa um objeto e retorna um dicionário que contém as informações de cada atributo"""
        return {
            "nome": self.get_nome,
            "ano_de_lancamento": self.get_anodelancamento,
            "tempo_de_duracao_em_minutos": self.get_tempodeduracao,
            "categoria": self.get_categoria,
            "sinopse": self.get_sinopse,
            "autor": self.get_autor,
            "tema": self.get_tema,
            "avaliacoes": self.get_avaliacoes,
            "nota": self.get_classificacao
        }

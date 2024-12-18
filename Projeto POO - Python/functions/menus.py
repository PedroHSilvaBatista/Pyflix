def menu() -> None:
    """Esta função exibe o menu principal do programa e não possui retorno"""
    menu = '''
    - 1: Cadastro
    - 2: Login
    - 3: Listar todos os títulos em catálogo
    - 4: Sugerir um título para ser adicionado
    - 5: Avaliar um título do catálogo
    - 6: Acrescentar à lista de desejos
    - 7: Exibir o tempo de maratona para assistir todos os títulos da lista de desejos
    - 8: Sair da conta 
    - 9: Sair do programa
    '''
    print(menu)


def exibir_categorias() -> None:
    """Esta função exibe o menu de categorias e não possui retorno"""
    categorias = '''
    1 - Filme
    2 - Série
    3 - Documentário
    '''
    print('-=' * 30)
    print(categorias)
    print('-=' * 30)

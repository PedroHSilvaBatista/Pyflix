import re
import requests
import os
import json


diretorio_atual = os.path.dirname(__file__)
caminho_usuario = os.path.join(diretorio_atual, '..', 'data', 'usuarios.json')


def cadastro(dicionario_contas: dict) -> None:
    print('Área de cadastro')

    nome_de_usuario = input('Digite seu nome de usuário: ')
    while nome_de_usuario in dicionario_contas:
        print(f'O nome {nome_de_usuario} já existe. Por favor, escolha outro nome de usuário')
        nome_de_usuario = input('Digite seu nome de usuário: ')

    dicionario_contas[nome_de_usuario] = {}
    
    dicionario_contas[nome_de_usuario]["nome_completo"] = input('Digite seu nome completo: ')
    dicionario_contas[nome_de_usuario]["email"] = []

    usuario_email = input('Digite seu email: ')
    while True:
        if not ("@" in usuario_email and "." in usuario_email):
            print('Por favor, insira um email válido. Um email deve conter @ e "."')
            usuario_email = input('Digite seu email: ')
        else:
            break
    dicionario_contas[nome_de_usuario]["email"].append(usuario_email)

    dicionario_contas[nome_de_usuario]["senha"] = input('Digite sua senha: ')
    while True:
        if not re.search(r'[!@#$%^&*(),.?":{}|<>_-]', dicionario_contas[nome_de_usuario]["senha"]):
            print('A senha deve conter pelo menos um caractere especial')
            dicionario_contas[nome_de_usuario]["senha"] = input('Digite sua senha: ')
        elif not re.search(r'[A-Z]', dicionario_contas[nome_de_usuario]["senha"]):
            print('A senha deve possuir pelo menos uma letra em maiúsculo')
            dicionario_contas[nome_de_usuario]["senha"] = input('Digite sua senha: ')
        elif not re.search(r'[a-z]', dicionario_contas[nome_de_usuario]["senha"]):
            print('A senha deve possuir pelo menos uma letra minúscula')
            dicionario_contas[nome_de_usuario]["senha"] = input('Digite sua senha: ')
        elif not any(caractere.isdigit() for caractere in dicionario_contas[nome_de_usuario]["senha"]):
            print('A senha deve conter pelo menos um algarismo')
            dicionario_contas[nome_de_usuario]["senha"] = input('Digite sua senha: ')
        elif len(dicionario_contas[nome_de_usuario]["senha"]) < 8:
            print('A senha deve possuir pelo menos 8 caracteres')
            dicionario_contas[nome_de_usuario]["senha"] = input('Digite sua senha: ')
        else:
            break
    
    dicionario_contas[nome_de_usuario]["telefone"] = []
    usuario_telefone = input('Digite seu número de telefone: ')
    # Corrigir a formatação do celular
    while len(usuario_telefone) != 11:
        print('Por favor, insira um número de telefone válido. Números de telefoneia móvel celular possuem 11 digitos')
        usuario_telefone = input('Digite seu número de telefone: ')
    formatacao_telefone = f'({usuario_telefone[:2]})' + " " + f'{usuario_telefone[2:7]}' + '-' + f'{usuario_telefone[7:]}'
    dicionario_contas[nome_de_usuario]["telefone"].append(formatacao_telefone)


    dicionario_contas[nome_de_usuario]["localizacao"] = {}
    while True:
        try:
            cep = input('Digite seu CEP: ')
            url = f'https://viacep.com.br/ws/{cep}/json/'
            response = requests.get(url)

            if response.status_code == 200:
                dados = response.json()
                dicionario_contas[nome_de_usuario]["localizacao"]["cep"] = dados["cep"]
                dicionario_contas[nome_de_usuario]["localizacao"]["logradouro"] = dados["logradouro"]
                dicionario_contas[nome_de_usuario]["localizacao"]["uf"] = dados["uf"]
                break
            else:
                print('O CEP informado não é válido')
        except requests.exceptions.ConnectionError as erro:
            print(f'Erro. Erro de conexão com a API: {erro}')
        except Exception:
            print(f'Não foi possível encontrar o CEP informado. Verifique se o endereço informado é válido')


    # Estrutura para subir os dados para o banco de dados
    with open(caminho_usuario, 'a', encoding='utf-8') as arquivo:
        json.dump(dicionario_contas, arquivo, indent=4, ensure_ascii=False)

    
def login(status_login: bool) -> bool:
    with open(caminho_usuario, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    nome_de_usuario = input('Digite seu nome de usuário: ')
    while nome_de_usuario not in dados:
        print('Por favor, digite um nome de usuário válido')
        nome_de_usuario = input('Digite seu nome de usuário: ')


    print('AVISO: Você terá 3 tentativas para acertar sua senha')
    tentativas = 3
    while tentativas > 0:
        senha_usuario = input('Digite sua senha: ')
        if senha_usuario == dados[nome_de_usuario]["senha"]:
            print('Login realizado com sucesso!')
            print(f'Seja bem-vindo, {dados[nome_de_usuario]["nome_completo"]}!')
            return not status_login
        tentativas -= 1
        print(f'Senha incorreta. Tentativas restantes: {tentativas}')
    print('Você excedeu o número de tentativas permitidas')
    return status_login

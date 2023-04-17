'''Estudante: Natalia Parmesano Galhardo
     Atividade Somativa 2
     Curso: Análise e Desenvolvimento de Sistemas PUCPR
     Disciplina: Raciocinio Computacional'''

import json
import time
import os


def clean():
    '''Limpa a tela do terminal'''
    os.system('cls')


def linha_tabela():
    '''Função para criar uma linha de separação'''
    print('+' + '-' * 57 + '+')


def linha(tam=60):
    '''Função para criar uma linha de separação'''
    return '-' * tam


def titulo(txt):
    '''Função para criar os títulos'''
    print(linha())
    print(txt.center(60))
    print(linha())


def saindo():
    '''Função para a exibição ao sair do sistema'''
    for i in range(3):
        print("Saindo" + "." * i, end="\r")
        time.sleep(0.5)


def carregando():
    '''Função que simula o carregamento dos dados'''
    for i in range(3):
        print("carregando" + "." * i, end="\r")
        time.sleep(0.5)


def leia_int(msg):
    '''Função para ler se o usuário digitou uma letra ao solicitar um número'''
    while True:
        number = str(input(msg))
        if number.isnumeric():
            return int(number)
        titulo('Erro! Digite um valor válido')


def salvar_em_arquivo(lista, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(lista, arquivo)
        arquivo.close()


def carregar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            lista = json.load(arquivo)
            arquivo.close()
            return lista
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as e:
        print('Erro ao carregar arquivo: ', e)
        return []
    except Exception as e:
        print('Erro inesperado: ', e)
        return []


class Matricula:

    def __init__(self, codigo, turma, estudante):
        self.codigo = codigo
        self.turma = turma
        self.estudante = estudante
        self.lista = carregar_arquivo('matriculas.json')

    def __str__(self):
        return f'Código: {self.codigo} - Turma: {self.turma} - Estudante: {self.estudante}'

    def criar_cadastro(self):
        self.lista = carregar_arquivo('matriculas.json')
        clean()
        titulo('Cadastro de Matrícula')

        self.codigo = leia_int('Código: ')
        self.turma = input('Turma: ')
        self.estudante = input('Estudante: ')

        for matricula in self.lista:
            if matricula['codigo'] == self.codigo:
                print('Código já cadastrado')
                return

        self.lista.append({'codigo': self.codigo,
                           'turma': self.turma,
                           'estudante': self.estudante})

        salvar_em_arquivo(self.lista, 'matriculas.json')
        print('\nCadastro realizado com sucesso!')

    def listar_cadastro(self):
        self.lista = carregar_arquivo('matriculas.json')
        clean()
        titulo('Listagem de Matrículas')

        if len(self.lista) == 0:
            print('Não há matrículas cadastradas')
            return

        carregando()
        linha_tabela()
        print(f'|{"Matrícula":14}|{"Turma":^14}| {"Estudante":^14}|')
        linha_tabela()

        for matricula in self.lista:
            print(
                f'|{matricula["codigo"]:14}|{matricula["turma"]:^14}|{matricula["estudante"]:^14}|')
            linha_tabela()

    def alterar_cadastro(self):
        self.lista = carregar_arquivo('matriculas.json')
        clean()
        titulo('Alteração de Cadastro')
        codigo = int(
            input('Digite o código da matrícula que deseja alterar: '))

        for matricula in self.lista:
            if matricula['codigo'] == codigo:
                self.codigo = int(input('Código: '))
                self.turma = input('Turma: ')
                self.estudante = input('Estudante: ')

                self.lista.append({'codigo': self.codigo,
                                   'turma': self.turma,
                                   'estudante': self.estudante})
                salvar_em_arquivo(self.lista, 'matriculas.json')
                print('\nCadastro alterado com sucesso!')
                return

            else:
                print('Matrícula não encontrada')

    def excluir_cadastro(self):
        self.lista = carregar_arquivo('matriculas.json')
        clean()
        titulo('Exclusão de Cadastro')
        codigo = int(
            input('Digite o código da matrícula que deseja excluir: '))

        for matricula in self.lista:
            if matricula['codigo'] == codigo:
                encontrado = True
                break

        if encontrado:
            opcao = input(
                'Deseja realmente excluir o cadastro? [S/N]: ').upper()

            if opcao == 'S':
                self.lista.remove(matricula)
                salvar_em_arquivo(self.lista, 'matriculas.json')

                print('\nCadastro excluído com sucesso!')
            if opcao == 'N':
                print('\nCadastro não excluído')

        else:
            print('Matrícula não encontrada')


class Turma:
    def __init__(self, codigo, disciplina, professor, estudantes):
        self.codigo = codigo
        self.disciplina = disciplina
        self.professor = professor
        self.estudantes = estudantes
        self.lista = carregar_arquivo('turmas.json')

    def __str__(self):
        return f'Código: {self.codigo} - Disciplina: {self.disciplina} - Professor: {self.professor} - Estudantes: {self.estudantes}'

    def criar_cadastro(self):
        self.lista = carregar_arquivo('turmas.json')
        titulo('Cadastro de Turma')
        clean()

        self.codigo = int(input('Código: '))
        self.disciplina = input('Disciplina: ')
        self.professor = input('Professor: ')
        self.estudantes = input('Estudantes: ')

        for turma in self.lista:
            if turma['codigo'] == self.codigo:
                print('Código já cadastrado')
                return

        self.lista.append({'codigo': self.codigo,
                           'disciplina': self.disciplina,
                           'professor': self.professor,
                           'estudantes': self.estudantes})

        salvar_em_arquivo(self.lista, 'turmas.json')
        print('\nCadastro realizado com sucesso!')

    def listar_cadastro(self):
        self.lista = carregar_arquivo('turmas.json')
        clean()
        titulo('Listagem de Turmas')

        if len(self.lista) == 0:
            print('Não há turmas cadastradas')
            return

        carregando()
        linha_tabela()
        print(
            f'|{"Turma":14}|{"Disciplina":^14}| {"Professor":^14}|{"Estudantes":^14}|')
        linha_tabela()

        for turma in self.lista:
            print(
                f'|{turma["codigo"]:14}|{turma["disciplina"]:^14}| {turma["professor"]:^14}|{turma["estudantes"]:^14}|')
            linha_tabela()

    def alterar_cadastro(self):
        self.lista = carregar_arquivo('turmas.json')
        clean()
        titulo('Alteração de Cadastro')
        codigo = int(input('Digite o código da turma que deseja alterar: '))

        for turma in self.lista:
            if turma['codigo'] == codigo:
                self.codigo = int(input('Código: '))
                self.disciplina = input('Disciplina: ')
                self.professor = input('Professor: ')
                self.estudantes = input('Estudantes: ')

                self.lista.append({'codigo': self.codigo,
                                   'disciplina': self.disciplina,
                                   'professor': self.professor,
                                   'estudantes': self.estudantes})
                salvar_em_arquivo(self.lista, 'turmas.json')
                print('\nCadastro alterado com sucesso!')
                return

        print('Turma não encontrada')

    def excluir_cadastro(self):
        self.lista = carregar_arquivo('turmas.json')
        clean()

        titulo('Exclusão de Cadastro')
        codigo = int(input('Digite o código da turma que deseja excluir: '))

        for turma in self.lista:
            if turma['codigo'] == codigo:
                encontrado = True
                break

        if encontrado:
            opcao = input(
                'Deseja realmente excluir o cadastro? [S/N]: ').upper()

            if opcao == 'S':
                self.lista.remove(turma)
                salvar_em_arquivo(self.lista, 'turmas.json')

                print('\nCadastro excluído com sucesso!')

            if opcao == 'N':
                print('\nExclusão cancelada')

        else:
            print('Turma não encontrada')


class Disciplina:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.lista = carregar_arquivo('disciplinas.json')

    def __str__(self):
        return f'Nome: {self.nome} - Codigo: {self.codigo} '

    def criar_cadastro(self):
        self.lista = carregar_arquivo('disciplinas.json')
        clean()
        titulo('Cadastro de Disciplina')

        self.nome = input('Nome: ')
        self.codigo = leia_int('Código: ')

        for disciplina in self.lista:
            if disciplina['codigo'] == self.codigo:
                print('Código já cadastrado')
                return

        self.lista.append({'nome': self.nome, 'codigo': self.codigo})
        salvar_em_arquivo(self.lista, 'disciplinas.json')

        print('\nCadastro realizado com sucesso!')

    def listar_cadastro(self):
        self.lista = carregar_arquivo('disciplinas.json')
        clean()
        titulo('Listagem de Disciplinas')

        if len(self.lista) == 0:
            print('Não há disciplinas cadastradas')
            return

        carregando()
        linha_tabela()
        print(f'|{"Nome":14}|{"Código":^14}|')
        linha_tabela()

        for disciplina in self.lista:
            print(f'|{disciplina["nome"]:14}|{disciplina["codigo"]:^14}|')
            linha_tabela()

    def alterar_cadastro(self):
        self.lista = carregar_arquivo('disciplinas.json')
        clean()
        titulo('Alteração de Cadastro')
        nome = input('Digite o nome da disciplina que deseja alterar: ')

        for disciplina in self.lista:
            if disciplina['nome'] == nome:
                self.nome = input('Nome: ')
                self.codigo = leia_int('Código: ')

                self.lista.append({'nome': self.nome, 'codigo': self.codigo})
                salvar_em_arquivo(self.lista, 'disciplinas.json')

                print('\nCadastro alterado com sucesso!')
                return

        print('Disciplina não encontrada')

    def excluir_cadastro(self):
        self.lista = carregar_arquivo('disciplinas.json')
        clean()
        titulo('Exclusão de Cadastro')
        nome = input('Digite o nome da disciplina que deseja excluir: ')

        for disciplina in self.lista:
            if disciplina['nome'] == nome:
                encontrado = True
                break

        if encontrado:
            opcao = input(
                'Deseja realmente excluir o cadastro? [S/N]: ').upper()

            if opcao == 'S':
                self.lista.remove(disciplina)
                salvar_em_arquivo(self.lista, 'disciplinas.json')

                print('\nCadastro excluído com sucesso!')

            if opcao == 'N':
                print('\nCadastro não excluído')

        else:
            print('Disciplina não encontrada')


class Professor:
    def __init__(self, nome, codigo, cpf):
        self.nome = nome
        self.codigo = codigo
        self.cpf = cpf
        self.lista = carregar_arquivo('professores.json')

    def __str__(self):
        return f'Nome: {self.nome} - Codigo: {self.codigo} - CPF: {self.cpf}'

    def criar_cadastro(self):
        self.lista = carregar_arquivo('professores.json')
        clean()
        titulo('Cadastro de Professor')
        self.nome = input('Nome: ')
        self.codigo = leia_int('Código: ')

        for professor in self.lista:
            if professor['codigo'] == self.codigo:
                print('Código já cadastrado')
                return

        self.cpf = leia_int('CPF: ')

        self.lista.append({'nome': self.nome,
                           'codigo': self.codigo,
                           'cpf': self.cpf})

        salvar_em_arquivo(self.lista, 'professores.json')
        print('\nCadastro realizado com sucesso!')

    def listar_cadastro(self):
        self.lista = carregar_arquivo('professores.json')
        clean()
        titulo('Listagem de Professores')

        if len(self.lista) == 0:
            print('Não há professores cadastrados')
            return

        carregando()
        linha_tabela()
        print(f'|{"Nome":14}|{"Código":^14}|{"CPF":^14}|')
        linha_tabela()

        for professor in self.lista:
            print(
                f'|{professor["nome"]:14}|{professor["codigo"]:^14}|{professor["cpf"]:^14}|')
            linha_tabela()

    def alterar_cadastro(self):
        self.lista = carregar_arquivo('professores.json')
        clean()
        titulo('Alteração de Cadastro')
        nome = input('Digite o nome do professor que deseja alterar: ')

        for professor in self.lista:
            if professor['nome'] == nome:

                self.nome = input('Nome: ')
                self.codigo = int(input('Código: '))
                self.cpf = input('CPF: ')

                self.lista.append({'nome': self.nome,
                                   'codigo': self.codigo,
                                   'cpf': self.cpf})
                salvar_em_arquivo(self.lista, 'professores.json')

                print('\nCadastro alterado com sucesso!')
                return

        print('Professor não encontrado')

    def excluir_cadastro(self):
        self.lista = carregar_arquivo('professores.json')
        clean()
        titulo('Exclusão de Cadastro')
        nome = input('Digite o nome do professor que deseja excluir: ')

        for professor in self.lista:
            if professor['nome'] == nome:
                encontrado = True
                break

        if encontrado:
            opcao = input(
                'Deseja realmente excluir o cadastro? [S/N]: ').upper()

            if opcao == 'S':
                self.lista.remove(professor)
                salvar_em_arquivo(self.lista, 'professores.json')
                print('\nCadastro excluído com sucesso!')

            if opcao == 'N':
                return print('\nCadastro não excluído')

        else:
            print('Professor não encontrado')


class Estudante:
    def __init__(self, nome, codigo, cpf):
        self.nome = nome
        self.codigo = codigo
        self.cpf = cpf
        self.lista = carregar_arquivo('estudantes.json')

    def __str__(self):
        return f'Nome: {self.nome} - Codigo: {self.codigo} - CPF: {self.cpf}'

    def criar_cadastro(self):
        clean()
        titulo('Cadastro de Estudante')
        self.nome = input('Nome: ')
        self.codigo = leia_int('Código: ')

        for estudante in self.lista:
            if estudante['codigo'] == self.codigo:
                print('Código já cadastrado')
                return

        self.cpf = leia_int('CPF: ')

        self.lista.append({'nome': self.nome,
                           'codigo': self.codigo,
                           'cpf': self.cpf})

        salvar_em_arquivo(self.lista, 'estudantes.json')
        print('\nCadastro realizado com sucesso!')

    def listar_cadastro(self):
        self.lista = carregar_arquivo('estudantes.json')
        clean()
        titulo('Listagem de Estudantes')

        if len(self.lista) == 0:
            print('Não há estudantes cadastrados')
            return

        carregando()
        linha_tabela()
        print(f'|{"Nome":14}|{"Código":^14}|{"CPF":^14}|')
        linha_tabela()

        for estudante in self.lista:
            print(
                f'|{estudante["nome"]:14}|{estudante["codigo"]:^14}|{estudante["cpf"]:^14}|')
            linha_tabela()

    def alterar_cadastro(self):
        self.lista = carregar_arquivo('estudantes.json')
        clean()
        titulo('Alteração de Cadastro')
        nome = input('Digite o nome do estudante que deseja alterar: ')

        for estudante in self.lista:
            if estudante['nome'] == nome:

                self.nome = input('Nome: ')
                self.codigo = leia_int('Código: ')
                self.cpf = leia_int('CPF: ')

                self.lista.append({'nome': self.nome,
                                   'codigo': self.codigo,
                                   'cpf': self.cpf})
                salvar_em_arquivo(self.lista, 'estudantes.json')

                print('\nCadastro alterado com sucesso!')
                return

        print('Estudante não encontrado')

    def excluir_cadastro(self):
        self.lista = carregar_arquivo('estudantes.json')
        clean()
        titulo('Exclusão de Cadastro')
        nome = input('Digite o nome do estudante que deseja excluir: ')

        for estudante in self.lista:
            if estudante['nome'] == nome:
                encontrado = True
                break

        if encontrado:
            opcao = input(
                'Deseja realmente excluir o cadastro? [S/N]: ').upper()

            if opcao == 'S':
                self.lista.remove(estudante)
                salvar_em_arquivo(self.lista, 'estudantes.json')
                print('\nCadastro excluído com sucesso!')

            elif opcao == 'N':
                return print('Exclusão cancelada')

        else:
            print('Estudante não encontrado')


def menu_principal():
    '''Função do Menu Principal'''

    # Dicionário de opções
    opcoes = {
        1: Estudante('', '', ''),
        2: Disciplina('', ''),
        3: Professor('', '', ''),
        4: Turma('', '', '', ''),
        5: Matricula('', '', '')
    }

    # Imprime o título principal
    print('\033[1;33m')
    titulo('Bem-vindo ao Sistema de Gerenciamento Acadêmico!')

    while True:
        # Imprime o título do menu
        print('\033[1;37m')
        titulo('SISTEMA PUC')

        # Imprime as opções do menu
        print("1 - Gerenciar estudante")
        print("2 - Gerenciar disciplina")
        print("3 - Gerenciar professor")
        print("4 - Gerenciar turma")
        print("5 - Gerenciar matrícula")
        print("6 - Sair")

        # Lê a opção escolhida pelo usuário
        try:
            opcao = int(input("\nDigite sua opção: "))
        except ValueError:
            print("\nEntrada inválida! Digite um número válido.\n")
            continue

        if opcao == 6:
            # Sai do programa
            saindo()
            print('\033[1;33m')
            titulo('Até logo!')
            break

        clean()
        # Imprime o título do menu de operações
        titulo('MENU DE OPERAÇÕES')

        # Imprime as opções do menu de operações
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Alterar")
        print("4 - Excluir")
        print("5 - Voltar")

        # Lê a opção escolhida pelo usuário
        try:
            operacao = int(input("\nDigite sua opção: "))
        except ValueError:
            print("\nEntrada inválida! Digite um número válido.\n")
            continue

        # Executa a operação escolhida
        if operacao in range(1, 6):
            if operacao == 1:
                opcoes[opcao].criar_cadastro()
            elif operacao == 2:
                opcoes[opcao].listar_cadastro()
            elif operacao == 3:
                opcoes[opcao].alterar_cadastro()
            elif operacao == 4:
                opcoes[opcao].excluir_cadastro()
            elif operacao == 5:
                clean()
                continue
        else:
            print("\nEntrada inválida! Digite um número válido.\n")

        # Pausa o programa para que o usuário possa ler as informações
        input("\nPressione ENTER para continuar...")
        clean()


if __name__ == '__main__':
    menu_principal()

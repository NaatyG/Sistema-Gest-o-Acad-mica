'''  Estudante: Natalia Parmesano Galhardo
     Atividade Somativa 2
     Curso: Análise e Desenvolvimento de Sistemas PUCPR
     Disciplina: Raciocinio Computacional
     Professor: Mauricio Antonio Ferste, Turma 4 '''

import json
import time
import re
import os


def clean():
    '''Limpa a tela do terminal'''
    os.system('cls')


def salvar_lista_em_json(lista, arquivo):
    # Função para salvar os dados do dicionário e lista em JSON

    with open(arquivo, 'w+') as file:
        json.dump(lista, file)
        file.close()


def carregar_lista_de_json(arquivo):
    # Função para carregar os dados salvo nos arquivos JSON
    try:
        with open(arquivo, 'r') as file:
            return json.load(file)

    except FileNotFoundError:
        print(f'Arquivo {arquivo} não encontrado.')
        return []

    except json.JSONDecodeError as e:
        print(f"Erro de decodificação de JSON.")
        return []

    except Exception as e:
        print(f"Erro inesperado.")


def linha(tam=60):
    '''Função para criar uma linha de separação'''
    return '-' * tam


def titulo(txt):
    '''Função para criar os títulos'''
    print(linha())
    print(txt.center(60))
    print(linha())


def carregando():
    '''Função que simula o carregamento dos dados'''
    for i in range(3):
        print("carregando" + "." * i, end="\r")
        time.sleep(0.5)


def saindo():
    '''Função para a exibição ao sair do sistema'''
    for i in range(3):
        print("Saindo" + "." * i, end="\r")
        time.sleep(0.5)


def validar_nome(nome):
    '''Função para ler se o usuário digitou um número ao solicitar letra'''
    padrao = r'^[a-zA-Z\s]+$'  # Passei o padrão de string que quero aceitar no input

    return re.match(padrao, nome)


def leiaint(msg):
    '''Função para ler se o usuário digitou uma letra ao solicitar um número'''

    while True:
        number = str(input(msg))
        if number.isnumeric():
            return int(number)
        titulo('Erro! Digite um valor válido')


def buscar_na_lista(lista, chave, valor):
    for elemento in lista:
        if elemento[chave] == valor:
            return True
    return False


class Estudante:
    '''Classe para manipular estudantes'''

    def __init__(self):
        self.lista = carregar_lista_de_json('estudantes.json')

    def adicionar(self):
        '''Função para adicionar estudante'''
        clean()
        titulo('Adicionar')

        nome = input('Nome do estudante: ')

        if validar_nome(nome):
            idade = leiaint('Digite a idade: ')
            turma = leiaint('Turma: ')
            matricula = leiaint('Digite a matrícula: ')

            if buscar_na_lista(self.lista, 'matricula', matricula):
                print('Matrícula já existe!')

                return

            self.lista.append({
                "nome": nome,
                "idade": idade,
                "turma": turma,
                "matricula": matricula})

            salvar_lista_em_json(self.lista, 'estudantes.json')
            print('\nEstudante adicionado com sucesso!\n')

            input()
            clean()

        else:
            titulo("Nome inválido. Use apenas letras e espaços em branco.")

    def listar(self):
        '''Função para listar estudantes'''

        def __init__(self):
            self.lista = carregar_lista_de_json('estudantes.json')

        clean()
        titulo('ESTUDANTES')

        if not len(self.lista):
            return print('Não há estudantes cadastrados')

        carregando()
        # Criado uma tabela para a exibição dos dados
        print('+' + '-' * 57 + '+')
        print(
            f'| {"Nome":14} | {"Idade":^12} | {"Turma":^10} | {"Matricula":^10} |')
        print('+' + '-' * 57 + '+')

        for data in self.lista:
            print(
                f"| {data['nome']:14} | {data['idade']:^12} | {data['turma']:^10} | {data['matricula']:^10} |")
            print('+' + '-' * 57 + '+')

        input()
        clean()

    def excluir(self):
        '''Função para excluir estudante'''

        clean()
        titulo('EXCLUIR')
        self.lista = carregar_lista_de_json('estudantes.json')

        matricula_aluno = leiaint(
            '\nDigite a matrícula do estudante que deseja excluir: ')
        encontrado = False

        for data in self.lista:
            if buscar_na_lista(self.lista, 'matricula', matricula_aluno):
                encontrado = True
                break

        if encontrado:
            opcao = leiaint(
                '\nVocê tem certeza que deseja excluir?\n(1) SIM\n(2) Voltar ao menu\n')

            if opcao == 1:
                self.lista.remove(data)
                salvar_lista_em_json(self.lista, 'estudantes.json')
                print('\nEstudante excluído com sucesso!\n')
                input()
                clean()

            else:
                titulo('\nExclusão cancelada.\n')
                menu_principal()

        else:
            titulo('\nMatrícula não encontrada.\n')

    def alterar(self):
        '''Função para alterar algum dado do cadastro'''

        clean()
        titulo('Alterar cadastro')
        nome = input('\nDigite o nome do estudante: \n')

        for data in self.lista:
            if buscar_na_lista(self.lista, 'nome', nome):

                novo_nome = input('Digite o novo nome: ')
                nova_idade = leiaint('Digite a idade: ')
                nova_turma = input('Digite a nova turma do estudante: ')
                nova_matricula = leiaint('Digite a nova matrícula: ')

                data["nome"] = novo_nome
                data["idade"] = nova_idade
                data["turma"] = nova_turma
                data["matricula"] = nova_matricula

                salvar_lista_em_json(self.lista, 'estudantes.json')
                print('\nAlterações salvas com sucesso!\n')

                input()
                clean()

                return
        print("\nEstudante não encontrado.\n")

    def buscar(self):
        '''Função para buscar algum cadastro'''

        clean()
        titulo('Pesquisar')

        self.lista = carregar_lista_de_json('estudantes.json')
        matricula_aluno = leiaint('\nDigite a matrícula do estudante: \n')

        for data in self.lista:
            carregando()
            # Verifica se a matrícula digitada é igual a uma matrícula já cadastrada

            if data["matricula"] == matricula_aluno:
                print('+' + '-' * 57 + '+')
                print(
                    f'| {"Nome":14} | {"Idade":^12} | {"Turma":^10} | {"Matricula":^10} |')
                print('+' + '-' * 57 + '+')

                print(
                    f"| {data['nome']:14} | {data['idade']:^12} | {data['turma']:^10} | {data['matricula']:^10} |")
                print('+' + '-' * 57 + '+')

                input()
                clean()

        print('\nMatrícula não encontrada na base de dados.\n')


class Disciplina:
    '''Classe para manipular disciplina'''

    def __init__(self):
        self.lista = []
        self.lista = carregar_lista_de_json('disciplinasdata.json')

    def adicionar(self):
        '''Função para adicionar nova disciplina'''
        clean()
        titulo('Adicionar')

        nome_d = input('Nome da Disciplina: ')
        codigo_d = int(input('Código: '))

        if buscar_na_lista(self.lista, 'codigo', codigo_d):
            print('\nDisciplina já cadastrada!')

            return

        self.lista.append({
            "nome": nome_d,
            "codigo": codigo_d,
        })

        salvar_lista_em_json(self.lista, 'disciplinasdata.json')
        print('\nDisciplina adicionada com sucesso!\n')

        input()
        clean()

    def listar(self):
        '''Função para listar disciplinas'''
        self.lista = carregar_lista_de_json('disciplinasdata.json')

        clean()
        titulo('DISCIPLINAS')

        if not len(self.lista):

            return print('\nNão há disciplinas cadastradas.')

        carregando()
        # Criando uma tabela para a exibição dos dados
        print('+' + '-' * 57 + '+')
        print(f'| {"Nome":14} | {"Código":^12} |')
        print('+' + '-' * 57 + '+')

        for data in self.lista:

            print(
                f"| {data['nome']:14} | {data['codigo']:^12} |")
            print('+' + '-' * 57 + '+')

        input()
        clean()

    def excluir(self):
        '''Função para excluir disciplina'''
        clean()

        titulo('EXCLUIR')
        self.lista = carregar_lista_de_json('disciplinasdata.json')

        codigo = leiaint('\nCódigo da disciplina: ')
        encontrado = False

        for disciplina in self.lista:
            if buscar_na_lista(self.lista, 'codigo', codigo):
                encontrado = True
                break

        if encontrado:
            opcao = leiaint(
                '\nVocê tem certeza que deseja excluir?\n(1) SIM\n(2) Voltar ao menu\n')

            if opcao == 1:
                self.lista.remove(disciplina)
                salvar_lista_em_json(self.lista, 'disciplinasdata.json')
                print('\nDisciplina excluída com sucesso!\n')

                input()
                clean()

            else:
                print('\nExclusão cancelada.\n')
                input()
                clean()

        else:
            print('\nDisciplina não encontrada.\n')

    def alterar(self):
        '''Função para alterar algum dado'''

        clean()
        titulo('Alterar')

        codigo_d = leiaint('\nDigite o código da disciplina: ')
        self.lista = carregar_lista_de_json('disciplinasdata.json')

        for data in self.lista:
            if data["codigo"] == codigo_d:

                novo_nome = input('\nDigite o novo nome: ')
                novo_codigo = leiaint('Digite o novo código: ')
                data["nome"] = novo_nome
                data["codigo"] = novo_codigo

                salvar_lista_em_json(self.lista, 'disciplinasdata.json')
                print('\nAlterações salvas com sucesso!\n')

                input()
                clean()

                return

        print("\nDisciplina não encontrada.\n")

    def buscar(self):
        '''Função para buscar disciplina'''

        clean()
        titulo("Pesquisar")

        self.lista = carregar_lista_de_json('disciplinasdata.json')
        codigo = leiaint('\nDigite o código da disciplina: ')

        for disciplina in self.lista:
            carregando()
            # Verifica se a matrícula digitada é igual a uma matrícula já cadastrada

            if disciplina["codigo"] == codigo:
                print('+' + '-' * 57 + '+')
                print(
                    f'| {"Nome":14} | {"Código":^12} |')
                print('+' + '-' * 57 + '+')

                print(
                    f"| {disciplina['nome']:14} | {disciplina['codigo']:^12} |")
                print('+' + '-' * 57 + '+')

                input()
                clean()

                return
        print('\nDisciplina não encontrada na base de dados.\n')


class Professor:
    '''Classe para manipular professores'''

    def __init__(self):
        self.lista = carregar_lista_de_json('professores.json')

    def adicionar(self):
        '''Função para adicionar professor'''

        clean()
        titulo('Adicionar')

        nome_p = input('Nome do professor: ')
        codigo_pf = leiaint('Código do professor: ')
        doc = leiaint('CPF: ')

        if buscar_na_lista(self.lista, 'codigo_p', codigo_pf):
            return print('Esse professor já foi cadastrado!')

        self.lista.append({"nome_p": nome_p,
                           "codigo_p": codigo_pf,
                           "cpf": doc})

        salvar_lista_em_json(self.lista, 'professores.json')
        print('\nProfessor cadastrado com sucesso!\n')

        input()
        clean()

    def listar(self):
        '''Função para listar professores'''

        self.lista = carregar_lista_de_json('professores.json')

        clean()
        titulo('PROFESSORES')

        if not len(self.lista):

            return print('Não há professores cadastrados.')

        carregando()
        # Criado uma tabela para a exibição dos dados
        print('+' + '-' * 57 + '+')
        print(f'| {"Nome":14} | {"Código":^12} |')
        print('+' + '-' * 57 + '+')

        for data in self.lista:

            print(f"| {data['nome_p']:14} | {data['codigo_p']:^12} |")
            print('+' + '-' * 57 + '+')

        input()
        clean()

    def excluir(self):
        '''Função para excluir algum professor'''

        clean()
        titulo('EXCLUIR')
        self.lista = carregar_lista_de_json('professores.json')

        codigo_pf = leiaint('\nCódigo do professor: ')
        encontrado = False

        for data in self.lista:
            if data["codigo_p"] == codigo_pf:
                encontrado = True
                break

        if encontrado:
            opcao = leiaint(
                '\nVocê tem certeza que deseja excluir?\n(1) SIM\n(2) Voltar ao menu\n')

            if opcao == 1:
                self.lista.remove(data)
                salvar_lista_em_json(self.lista, 'professores.json')
                print('Professor excluído com sucesso!\n')
                input()
                clean()

            else:
                titulo('\nExclusão cancelada.\n')
                input()
                clean()

        else:
            titulo('Professor não encontrado.\n')

    def alterar(self):
        '''Função para alterar algum dado do professor'''

        clean()
        titulo("Alterar")
        nome_p = input('\nDigite o nome do professor: ')

        for data in self.lista:
            if data["nome_p"] == nome_p:

                novo_nome = input('Digite o novo nome: ')
                novo_codigo = leiaint('Digite o código: ')
                novo_doc = input('Digite o CPF: ')

                data["nome_p"] = novo_nome
                data["codigo_p"] = novo_codigo
                data["cpf"] = novo_doc

                salvar_lista_em_json(self.lista, 'professores.json')
                print('\nAlterações salvas com sucesso!\n')

                input()
                clean()

                return
        print("\Professor não encontrado.\n")

    def buscar(self):
        '''Função para buscar professor cadastrado'''

        clean()
        titulo("Pesquisar")
        self.lista = carregar_lista_de_json('professores.json')

        codigo_pf = leiaint('\nDigite o código do professor: ')

        for data in self.lista:
            carregando()
            # Verifica se a matrícula digitada é igual a uma matrícula já cadastrada

            if data['codigo_p'] == codigo_pf:
                print('+' + '-' * 57 + '+')
                print(
                    f'| {"Nome":14} | {"Código":^12} |')
                print('+' + '-' * 57 + '+')

                print(
                    f"| {data['nome_p']:14} | {data['codigo_p']:^12} |")
                print('+' + '-' * 57 + '+')

                input()
                clean()
                return

        print('\nProfessor não encontrado na base de dados.\n')


class Turma:
    '''Classe para manipular turmas'''

    def __init__(self):
        self.lista = carregar_lista_de_json('turmas.json')
        self.lista = [{'nome': 'Filosofia', 'codigo': 10}, {'nome': 'Matematica', 'codigo': 90},
                      {'nome': 'Raciocinio C', 'codigo': 30}, {
                          'codigo_t': 2, 'codigo_prof': 2, 'codigo_disci': 2},
                      {'codigo_t': 10, 'codigo_prof': 20, 'codigo_disci': 20}]
        del self.lista[0:3]

    def verificar_turma(self, codigo_turma):
        self.estudantes = carregar_lista_de_json('estudantes.json')

        for turma in self.estudantes:
            if turma['turma'] == codigo_turma:
                return True

        return False

    def verificar_professor(self, codigo_professor):
        self.professor = carregar_lista_de_json('professores.json')

        for professor in self.professor:
            if professor['codigo_p'] == codigo_professor:
                return True

        return False

    def verificar_disciplina(self, codigo_disciplina):
        self.disciplina = carregar_lista_de_json('disciplinasdata.json')

        for disciplina in self.disciplina:
            if disciplina['codigo'] == codigo_disciplina:
                return True

        return False

    def adicionar(self):
        '''Função para adicionar turma'''

        clean()
        titulo('Adicionar')

        while True:
            codigo_turma = leiaint('Código da turma: ')
            if not self.verificar_turma(codigo_turma):
                break
            print('Turma já cadastrada.')

        while True:
            codigo_professor = leiaint('Código do professor: ')
            if not self.verificar_professor(codigo_professor):
                break
            print('Professor já cadastrado.')

        while True:
            codigo_disciplina = leiaint('Código da disciplina: ')
            if not self.verificar_disciplina(codigo_disciplina):
                break
            print('Disciplina já cadastrada.')

        self.lista.append({
            "codigo_t": codigo_turma,
            "codigo_prof": codigo_professor,
            "codigo_disci": codigo_disciplina})

        salvar_lista_em_json(self.lista, 'turmas.json')
        print('Turma cadastrada com sucesso!')

        input()
        clean()

    def listar(self):
        '''Função para listar turmas'''

        clean()
        titulo('TURMAS')

        if not len(self.lista):

            return print('Não há turmas cadastradas.')

        carregando()
        # Criado uma tabela para a exibição dos dados
        print('+' + '-' * 57 + '+')
        print(f'| {"Turma":14} | {"Professor":^12} | {"Disciplina":^10} |')
        print('+' + '-' * 57 + '+')

        for data in self.lista:

            print(
                f"| {data['codigo_t']:14} | {data['codigo_prof']:^12} | {data['codigo_disci']:^10} |")
            print('+' + '-' * 57 + '+')

        input()
        clean()

    def excluir(self):
        '''Função para excluir alguma turma'''

        clean()
        titulo('EXCLUIR')

        codigo_turma = leiaint('\nCódigo da turma: ')
        encontrado = False

        for data in self.lista:
            if data['codigo_t'] == codigo_turma:
                encontrado = True
                break

        if encontrado:
            opcao = leiaint(
                '\nVocê tem certeza que deseja excluir?\n(1) SIM\n(2) Voltar ao menu\n')

            if opcao == 1:
                self.lista.remove(data)
                salvar_lista_em_json(self.lista, 'turmas.json')
                print('Turma excluída com sucesso!\n')

                input()
                clean()

            else:
                titulo('\nExclusão cancelada.\n')

                input()
                clean()

        else:
            titulo('\nTurma não encontrada.\n')

    def alterar(self):
        '''Função para alterar alguma informação da turma'''

        clean()
        titulo("Alterar")

        codigo_t = leiaint('\nDigite o código da turma: ')

        for data in self.lista:
            if data["codigo_t"] == codigo_t:

                novo_codigo = leiaint('Digite o novo codigo da turma: ')
                novo_prof = leiaint('Novo código do professor: ')
                novo_disci = leiaint('Novo código da disciplina: ')

                data["codigo_t"] = novo_codigo
                data["codigo_prof"] = novo_prof
                data["codigo_disci"] = novo_disci

                salvar_lista_em_json(self.lista, 'turmas.json')
                print('\nAlterações salvas com sucesso!\n')

                input()
                clean()

                return
        print("\Turma não encontrada.\n")

    def buscar(self):
        '''Função para buscar turma cadastrada'''

        clean()
        titulo("Pesquisar")

        codigo_turma = leiaint('\nDigite o código da turma: ')

        for data in self.lista:
            carregando()
            # Verifica se a matrícula digitada é igual a uma matrícula já cadastrada

            if data['codigo_t'] == codigo_turma:

                print('+' + '-' * 57 + '+')
                print(
                    f'| {"Turma":14} | {"Código Professor":^12} | {"Código Disciplina":^10} |')
                print('+' + '-' * 57 + '+')

                print(
                    f"| {data['codigo_t']:14} | {data['codigo_prof']:^16} | {data['codigo_disci']:^17} |")
                print('+' + '-' * 57 + '+')

                input()
                clean()
                return

        print('\nTurma não encontrada na base de dados.\n')


class Matricula:
    '''Classe para manipular matrículas'''

    def __init__(self):
        self.lista = carregar_lista_de_json('matriculas.json')
        self.lista = [{'codigo_t': 4, 'matricula': 1}, {'codigo_t': 6, 'codigo_aluno': 5},
                      {'codigo_t': 7, 'codigo_aluno': 7}, {
                          'codigo_t': 2, 'codigo_aluno': 2},
                      {'codigo_t': 8, 'codigo_estudante': 8}, {
                          'codigo_t': 2, 'codigo_estudante': 2},
                      {'codigo_t': 90, 'codigo_estudante': 8}]
        del self.lista[0:4]

    def verificar_turma(self, codigo_t):
        self.estudantes = carregar_lista_de_json('estudantes.json')

        for turma in self.estudantes:
            if turma['turma'] == codigo_t:
                return True

        return False

    def verificar_matricula(self, codigo_estudante):
        self.matricula = carregar_lista_de_json('estudantes.json')

        for estudante in self.matricula:
            if estudante['matricula'] == codigo_estudante:
                return True

        return False

    def adicionar(self):
        '''Função para adicionar matrícula'''

        clean()
        titulo('Adicionar')

        while True:
            codigo_t = leiaint('Código da turma: ')
            if not self.verificar_turma(codigo_t):
                break
            print('Essa turma já foi cadastrada!')

        while True:
            codigo_estudante = leiaint('Código do estudante: ')
            if not self.verificar_matricula(codigo_estudante):
                break
            print('Matrícula já cadastrada!')

        self.lista.append({
            'codigo_t': codigo_t,
            'codigo_estudante': codigo_estudante})

        salvar_lista_em_json(self.lista, 'matriculas.json')
        print('Matrículas adicionadas com sucesso!\n')

        input()
        clean()

    def listar(self):
        '''Função para listar matrículas'''

        clean()
        titulo('MATRÍCULAS')

        if not len(self.lista):
            print('Não há matrículas cadastradas')
            return

        carregando()
        # Criado uma tabela para a exibição dos dados
        try:
            print('+' + '-' * 57 + '+')
            print(f'| {"Turmas":14} | {"Estudantes":^12} |')
            print('+' + '-' * 57 + '+')

            for turma in self.lista:

                print(
                    f"| {turma['codigo_t']:14} | {turma['codigo_estudante']:^12} |")
                print('+' + '-' * 57 + '+')

            input()
            clean()

        except KeyError:
            print('Ocorreu um erro inesperado.')

    def excluir(self):
        '''Função para excluir matrículas'''

        clean()
        titulo('EXCLUIR')

        codigo_t = leiaint('\nCódigo da turma: ')
        encontrado = False

        for data in self.lista:
            if data['codigo_t'] == codigo_t:
                encontrado = True
                break

        if encontrado:
            opcao = leiaint(
                '\nVocê tem certeza que deseja excluir?\n(1) SIM\n(2) Voltar ao menu\n')

            if opcao == 1:
                self.lista.remove(data)
                salvar_lista_em_json(self.lista, 'matriculas.json')
                print('Matrícula excluída com sucesso!')

                input()
                clean()
            else:
                titulo('\nExclusão cancelada.\n')
                input()
                clean()

        else:
            titulo('\nMatrícula não encontrada.\n')

    def alterar(self):
        '''Função para alterar alguma matrícula'''

        clean()
        titulo("Alterar")

        codigo_t = leiaint('\nDigite o código da turma: ')

        for data in self.lista:
            if data["codigo_t"] == codigo_t:

                novo_codigo = leiaint('Digite o novo codigo da turma: ')
                novo_estudante = leiaint('Novo código do estudante: ')

                data["codigo_t"] = novo_codigo
                data["codigo_estudante"] = novo_estudante

                salvar_lista_em_json(self.lista, 'matriculas.json')
                print('\nAlterações salvas com sucesso!\n')

                input()
                clean()

                return
        print("\nCódigo não encontrado.\n")

    def buscar(self):
        '''Função para buscar matrícula'''

        clean()
        titulo('Buscar')
        codigo_t = leiaint('Código da turma: ')

        for turma in self.lista:
            if turma['codigo_t'] == codigo_t:
                carregando()
            # Verifica se a matrícula digitada é igual a uma matrícula já cadastrada

            print('+' + '-' * 57 + '+')
            print(
                f'| {"Turma":14} | {"Estudante":^13} |')
            print('+' + '-' * 57 + '+')

            print(
                f"| {turma['codigo_t']:14} | {turma['codigo_estudante']:^13} |")
            print('+' + '-' * 57 + '+')

            input()
            clean()
            return

        print('\nMatrícula não encontrada.\n')


def menu_principal():
    '''
    Função do Menu Principal
    '''

    # Dicionário de opções
    opcoes = {
        1: Estudante(),
        2: Disciplina(),
        3: Professor(),
        4: Turma(),
        5: Matricula()
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

        # Lê a opção de operação escolhida pelo usuário
        try:
            operacao = int(input(
                "1 - Adicionar\n2 - Listar\n3 - Excluir\n4 - Alterar\n5 - Buscar\n\nDigite uma operação: "))

        except ValueError:
            print("\nEntrada inválida! Digite um número válido.\n")

            continue

        # Executa a operação escolhida pelo usuário
        if operacao in range(1, 6):
            if operacao == 1:
                opcoes[opcao].adicionar()
            elif operacao == 2:
                opcoes[opcao].listar()
            elif operacao == 3:
                opcoes[opcao].excluir()
            elif operacao == 4:
                opcoes[opcao].alterar()
            else:
                opcoes[opcao].buscar()
        else:
            print("\nOperação inválida! Digite um número entre 1 e 5.\n")


if __name__ == '__main__':
    menu_principal()

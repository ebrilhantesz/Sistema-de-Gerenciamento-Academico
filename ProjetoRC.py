# Listas iniciais do sistema
alunos = []
disciplinas = []
professores = []
turmas = []
matriculas = []

# Funções iniciais do sistema
def mostrar_menu_principal():
    print("-- MENU PRINCIPAL --")
    print(" ")
    print("1. Gerenciamento de Alunos")
    print("2. Gerenciamento de Disciplinas")
    print("3. Gerenciamento de Professores")
    print("4. Gerenciamento de Turmas")
    print("5. Gerenciamento de Matriculas")
    print("9. Sair")
    print(" ")
    return input("Informe a Opção Desejada: ")

def mostrar_menu_alunos():
    print("-- [ALUNOS] MENU DE OPERAÇÕES --")
    print(" ")
    print("(1) Incluir")
    print("(2) Listar")
    print("(3) Atualizar")
    print("(4) Excluir")
    print("(9) Voltar ao Menu Principal")
    print(" ")
    return input("Informe a Opção Desejada: ")

def cadastrar_alunos(alunos):
    while True:
        try:
            codigo_aluno = int(input("Informe o Código do Aluno (apenas números): "))
            break
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")
    nome_aluno = input("Informe o Nome do Aluno: ")
    cpf_aluno = input("Informe o CPF do Aluno: ")
    dados_aluno = {}
    dados_aluno["Código do Aluno"] = codigo_aluno
    dados_aluno["Nome do Aluno"] = nome_aluno
    dados_aluno["CPF do Aluno"] = cpf_aluno
    alunos.append(dados_aluno)
    print(" ")
    print("Aluno incluído com sucesso!")
    print(" ")

def listar_alunos(alunos):
    if len(alunos) == 0:
        print("Não há alunos cadastrados.")
        print(" ")
    for nome_aluno in alunos:
        print(nome_aluno)

def atualizar_alunos(alunos):
    while True:
        try:
            codigo_edicao_aluno = int(input("Qual o Código do Aluno que deseja editar? (apenas números): "))
            break
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")
    aluno_para_edicao = None
    for dados_aluno in alunos:
        if dados_aluno["Código do Aluno"] == codigo_edicao_aluno:
            aluno_para_edicao = dados_aluno
            break
    if aluno_para_edicao is None:
        print(f"O Aluno com código {codigo_edicao_aluno} não foi localizado.")
        print("Os alunos cadastrados são:")
    else:
        # Validação do novo código do aluno
        while True:
            try:
                aluno_para_edicao["Código do Aluno"] = int(input("Informe o novo Código do Aluno: "))
                break
            except ValueError:
                print("Entrada inválida! Por favor, digite apenas números.")
        aluno_para_edicao["Nome do Aluno"] = input("Informe o novo Nome do Aluno: ")
        aluno_para_edicao["CPF do Aluno"] = input("Informe o novo CPF do Aluno: ")
        print("Alteração realizada com sucesso!")
        print(" ")
        print("Os alunos cadastrados são:")
    for dados_aluno in alunos:
        print(dados_aluno)

def excluir_alunos(alunos):
    while True:
        try:
            codigo_exclusao_aluno = int(input("Qual o código do Aluno que deseja excluir?: "))
            break
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")
    aluno_para_exclusao = None
    for dados_aluno in alunos:
        if dados_aluno["Código do Aluno"] == codigo_exclusao_aluno:
            aluno_para_exclusao = dados_aluno
            break
    if aluno_para_exclusao is None:
        print(f"O Aluno com o código {codigo_exclusao_aluno} não foi localizado!")
    else:
        alunos.remove(aluno_para_exclusao)
        print("Aluno excluído com sucesso!")
        print("Os alunos cadastrados são:")
    for dados_aluno in alunos:
        print(dados_aluno)
    if len(alunos) == 0:
        print("Não há alunos cadastrados.")
        print(" ")

while True:
    # Menu de seleção principal (inicial)
    opc = mostrar_menu_principal()

    # Navegando pelo menu secundário (operações)
    if opc == '1':
        print("Você escolheu a opção: 1. Gerenciamento de Alunos")
        print(" ")
        while True:
            alu = mostrar_menu_alunos()
            if alu == '1':
                print("-- [ALUNOS] INCLUSÃO --")
                print(" ")
                cadastrar_alunos(alunos)
            elif alu == '2':
                print("-- [ALUNOS] LISTAGEM --")
                print(" ")
                listar_alunos(alunos)
            elif alu == '3':
                print("-- [ALUNOS] EDIÇÃO --")
                print(" ")
                atualizar_alunos(alunos)
            elif alu == '4':
                print("-- [ALUNOS] EXCLUSÃO --")
                print(" ")
                excluir_alunos(alunos)
            elif alu == '9':
                print("Você escolheu voltar ao Menu Principal.")
                break
            else:
                print("Opção inválida, selecione outra opção!")
    elif opc == '2':
        print("Você escolheu a opção: 2. Gerenciamento de Disciplinas")
        print(" ")
        while True:
            print("-- [DISCIPLINAS] MENU DE OPERAÇÕES --")
            print(" ")
            print("(1) Incluir")
            print("(2) Listar")
            print("(3) Atualizar")
            print("(4) Excluir")
            print("(9) Voltar ao Menu Principal")
            print(" ")
            disc = input("Informe a Opção Desejada: ")
            print(" ")
            if disc == '1' or disc == '2' or disc == '3' or disc == '4':
                print("EM DESENVOLVIMENTO")
            elif disc == '9':
                print("Você escolheu voltar ao Menu Principal.")
                break
            else:
                print("Opção inválida, selecione outra opção!")
    elif opc == '3':
        print("Você escolheu a opção: 3. Gerenciamento de Professores")
        print(" ")
        while True:
            print("-- [PROFESSORES] MENU DE OPERAÇÕES --")
            print(" ")
            print("(1) Incluir")
            print("(2) Listar")
            print("(3) Atualizar")
            print("(4) Excluir")
            print("(9) Voltar ao Menu Principal")
            print(" ")
            prof = input("Informe a Opção Desejada: ")
            print(" ")
            if prof == '1' or prof == '2' or prof == '3' or prof == '4':
                print("EM DESENVOLVIMENTO")
            elif prof == '9':
                print("Você escolheu voltar ao Menu Principal.")
                break
            else:
                print("Opção inválida, selecione outra opção!")
    elif opc == '4':
        print("Você escolheu a opção: 4. Gerenciamento de Turmas")
        print(" ")
        while True:
            print("-- [TURMAS] MENU DE OPERAÇÕES --")
            print(" ")
            print("(1) Incluir")
            print("(2) Listar")
            print("(3) Atualizar")
            print("(4) Excluir")
            print("(9) Voltar ao Menu Principal")
            print(" ")
            tur = input("Informe a Opção Desejada: ")
            print(" ")
            if tur == '1' or tur == '2' or tur == '3' or tur == '4':
                print("EM DESENVOLVIMENTO")
            elif tur == '9':
                print("Você escolheu voltar ao Menu Principal.")
                break
            else:
                print("Opção inválida, selecione outra opção!")
    elif opc == '5':
        print("Você escolheu a opção: 5. Gerenciamento de Matrículas")
        print(" ")
        while True:
            print("-- [MATRÍCULAS] MENU DE OPERAÇÕES --")
            print(" ")
            print("(1) Incluir")
            print("(2) Listar")
            print("(3) Atualizar")
            print("(4) Excluir")
            print("(9) Voltar ao Menu Principal")
            print(" ")
            matr = input("Informe a Opção Desejada: ")
            print(" ")
            if matr == '1' or matr == '2' or matr == '3' or matr == '4':
                print("EM DESENVOLVIMENTO")
            elif matr == '9':
                print("Você escolheu voltar ao Menu Principal.")
                break
            else:
                print("Opção inválida, selecione outra opção!")
    elif opc == '9':
        print("Você escolheu sair.")
        break
    else:
        print("Opção inválida, selecione outra opção!")

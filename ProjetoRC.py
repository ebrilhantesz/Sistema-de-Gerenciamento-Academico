import json

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

def mostrar_menu_operacoes():
    print("(1) Incluir")
    print("(2) Listar")
    print("(3) Atualizar")
    print("(4) Excluir")
    print("(9) Voltar ao Menu Principal")
    print(" ")
    return input("Informe a Opção Desejada: ")

# Função para ler o números e tratar os erros
def ler_numero(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Entrada inválida! Por gentileza, digite apenas números.")

# Funções para salvar e ler os arquivos .json
def salvar_arquivo_em_json(lista, nome_arquivo):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False, indent=2)

def ler_arquivo_em_json(nome_arquivo):
    try:
        with open(nome_arquivo, "r" , encoding="utf-8") as arquivo:
            lista = json.load(arquivo)
        return lista
    except:
        return []

# Função para listar os cadastros nos arquivos .json
def listar_cadastros(nome_arquivo):
    cadastros = ler_arquivo_em_json(nome_arquivo)
    if len(cadastros) == 0:
        print("Não há registros cadastrados.")
        print(" ")
    for item in cadastros:
        print(item)

def processar_menu_operacoes(opcao, nome_arquivo, tipo):
    if tipo == 'alunos':
        if opcao == '1':
            print("-- [ALUNOS] INCLUSÃO --")
            print(" ")
            incluir_cadastros_alunos(nome_arquivo)
        elif opcao == '2':
            print("-- [ALUNOS] LISTAGEM --")
            print(" ")
            listar_cadastros(nome_arquivo)
        elif opcao == '3':
            print("-- [ALUNOS] EDIÇÃO --")
            print(" ")
            atualizar_cadastros_alunos(nome_arquivo)
        elif opcao == '4':
            print("-- [ALUNOS] EXCLUSÃO --")
            print(" ")
            excluir_cadastros_alunos(nome_arquivo)
        elif opcao == '9':
            print("Você escolheu voltar ao Menu Principal.")
            return False
        else:
            print("Opção inválida, selecione outra opção!")
    elif tipo == 'disciplinas':
        if opcao == '1':
            print("-- [DISCIPLINAS] INCLUSÃO --")
            incluir_cadastros_disciplinas(nome_arquivo)
        elif opcao == '2':
            print("-- [DISCIPLINAS] LISTAGEM --")
            listar_cadastros(nome_arquivo)
        elif opcao == '3':
            print("-- [DISCIPLINAS] EDIÇÃO --")
            atualizar_cadastros_disciplinas(nome_arquivo)
        elif opcao == '4':
            print("-- [DISCIPLINAS] EXCLUSÃO --")
            excluir_cadastros_disciplinas(nome_arquivo)
        elif opcao == '9':
            print("Você escolheu voltar ao Menu Principal.")
            return False
        else:
            print("Opção inválida, selecione outra opção!")
    elif tipo == 'professores':
        if opcao == '1':
            print("-- [PROFESSORES] INCLUSÃO --")
            incluir_cadastros_professores(nome_arquivo)
        elif opcao == '2':
            print("-- [PROFESSORES] LISTAGEM --")
            listar_cadastros(nome_arquivo)
        elif opcao == '3':
            print("-- [PROFESSORES] EDIÇÃO --")
            atualizar_cadastros_professores(nome_arquivo)
        elif opcao == '4':
            print("-- [PROFESSORES] EXCLUSÃO --")
            excluir_cadastros_professores(nome_arquivo)
        elif opcao == '9':
            print("Você escolheu voltar ao Menu Principal.")
            return False
        else:
            print("Opção inválida, selecione outra opção!")
    elif tipo == 'turmas':
        if opcao == '1':
            print("-- [TURMAS] INCLUSÃO --")
            incluir_cadastros_turmas(nome_arquivo)
        elif opcao == '2':
            print("-- [TURMAS] LISTAGEM --")
            listar_cadastros(nome_arquivo)
        elif opcao == '3':
            print("-- [TURMAS] EDIÇÃO --")
            atualizar_cadastros_turmas(nome_arquivo)
        elif opcao == '4':
            print("-- [TURMAS] EXCLUSÃO --")
            excluir_cadastros_turmas(nome_arquivo)
        elif opcao == '9':
            print("Você escolheu voltar ao Menu Principal.")
            return False
        else:
            print("Opção inválida, selecione outra opção!")
    elif tipo == 'matriculas':
        if opcao == '1':
            print("-- [MATRÍCULAS] INCLUSÃO --")
            incluir_cadastros_matriculas(nome_arquivo)
        elif opcao == '2':
            print("-- [MATRÍCULAS] LISTAGEM --")
            listar_cadastros(nome_arquivo)
        elif opcao == '3':
            print("-- [MATRÍCULAS] EDIÇÃO --")
            atualizar_cadastros_matriculas(nome_arquivo)
        elif opcao == '4':
            print("-- [MATRÍCULAS] EXCLUSÃO --")
            excluir_cadastros_matriculas(nome_arquivo)
        elif opcao == '9':
            print("Você escolheu voltar ao Menu Principal.")
            return False
        else:
            print("Opção inválida, selecione outra opção!")
    else:
        print("Módulo desconhecido.")
    return True

# Funções Alunos
def incluir_cadastros_alunos(nome_arquivo):
    arquivo_alunos = ler_arquivo_em_json(nome_arquivo)
    while True:
        try:
            codigo_aluno = int(input("Informe o Código do Aluno (apenas números): "))
            if any(a["Código do Aluno"] == codigo_aluno for a in arquivo_alunos):
                print(f"Já existe um aluno com o Código {codigo_aluno} cadastrado! Por gentileza, insira um código diferente.")
            else:
                break
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")
    nome_aluno = input("Informe o Nome do Aluno: ")
    cpf_aluno = input("Informe o CPF do Aluno: ")
    dados_aluno = {"Código do Aluno": codigo_aluno, "Nome do Aluno": nome_aluno, "CPF do Aluno": cpf_aluno}
    arquivo_alunos.append(dados_aluno)
    salvar_arquivo_em_json(arquivo_alunos, nome_arquivo)
    print(" ")
    print("Aluno incluído com sucesso!")
    print(" ")
    print("Os alunos cadastrados são:")
    for dados_aluno in arquivo_alunos:
        print(dados_aluno)

def atualizar_cadastros_alunos(nome_arquivo):
    arquivo_alunos = ler_arquivo_em_json(nome_arquivo)
    while True:
        try:
            codigo_edicao_aluno = int(input("Qual o Código do Aluno que deseja editar? (apenas números): "))
            break
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")
    aluno_para_edicao = None
    for dados_aluno in arquivo_alunos:
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
        salvar_arquivo_em_json(arquivo_alunos, nome_arquivo)
        print("Alteração realizada com sucesso!")
        print(" ")
        print("Os alunos cadastrados são:")
    for dados_aluno in arquivo_alunos:
        print(dados_aluno)

def excluir_cadastros_alunos(nome_arquivo):
    arquivo_alunos = ler_arquivo_em_json(nome_arquivo)
    while True:
        try:
            codigo_exclusao_aluno = int(input("Qual o código que deseja excluir?: "))
            break
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")
    aluno_para_exclusao = None
    for dados_aluno in arquivo_alunos:
        if dados_aluno["Código do Aluno"] == codigo_exclusao_aluno:
            aluno_para_exclusao = dados_aluno
            break
    if aluno_para_exclusao is None:
        print(f"O Aluno com o código {codigo_exclusao_aluno} não foi localizado!")
    else:
        arquivo_alunos.remove(aluno_para_exclusao)
        salvar_arquivo_em_json(arquivo_alunos, nome_arquivo)
        print("Aluno excluído com sucesso!")
        print("Os alunos cadastrados são:")
    for dados_aluno in arquivo_alunos:
        print(dados_aluno)
    if len(arquivo_alunos) == 0:
        print("Não há alunos cadastrados.")
        print(" ")

# Funções Disciplinas
def incluir_cadastros_disciplinas(nome_arquivo):
    arquivo_disciplinas = ler_arquivo_em_json(nome_arquivo)
    while True:
        try:
            codigo_disciplina = int(input("Informe o Código da Disciplina (apenas números): "))
            if any(d["Código da Disciplina"] == codigo_disciplina for d in arquivo_disciplinas):
                print(f"Já existe uma disciplina com o Código {codigo_disciplina} cadastrado! Por gentileza, insira um código diferente.")
            else:
                break
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")
    nome_disciplina = input("Informe o Nome da Disciplina: ")
    dados_disciplina = {"Código da Disciplina": codigo_disciplina, "Nome da Disciplina": nome_disciplina}
    arquivo_disciplinas.append(dados_disciplina)
    salvar_arquivo_em_json(arquivo_disciplinas, nome_arquivo)
    print(" ")
    print("Disciplina incluída com sucesso!")
    print(" ")
    print("As disciplinas cadastradas são:")
    for dados_disciplina in arquivo_disciplinas:
        print(dados_disciplina)

def atualizar_cadastros_disciplinas(nome_arquivo):
    arquivo_disciplinas = ler_arquivo_em_json(nome_arquivo)
    while True:
        try:
            codigo_edicao_disciplina = int(input("Qual o Código da Disciplina que deseja editar? (apenas números): "))
            break
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")
    disciplina_para_edicao = None
    for dados_disciplina in arquivo_disciplinas:
        if dados_disciplina["Código da Disciplina"] == codigo_edicao_disciplina:
            disciplina_para_edicao = dados_disciplina
            break
    if disciplina_para_edicao is None:
        print(f"A disciplina com código {codigo_edicao_disciplina} não foi localizada.")
        print("As disciplinas cadastradas são:")
    else:
        # Validação do novo código da disciplina
        while True:
            try:
                disciplina_para_edicao["Código da Disciplina"] = int(input("Informe o novo Código da Disciplina: "))
                break
            except ValueError:
                print("Entrada inválida! Por favor, digite apenas números.")
        disciplina_para_edicao["Nome da Disciplina"] = input("Informe o novo Nome da Disciplina: ")
        salvar_arquivo_em_json(arquivo_disciplinas, nome_arquivo)
        print("Alteração realizada com sucesso!")
        print(" ")
        print("As disciplinas cadastradas são:")
    for dados_disciplina in arquivo_disciplinas:
        print(dados_disciplina)

def excluir_cadastros_disciplinas(nome_arquivo):
    arquivo_disciplinas = ler_arquivo_em_json(nome_arquivo)
    while True:
        try:
            codigo_exclusao_disciplina = int(input("Qual o código que deseja excluir?: "))
            break
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")
    disciplina_para_exclusao = None
    for dados_disciplina in arquivo_disciplinas:
        if dados_disciplina["Código da Disciplina"] == codigo_exclusao_disciplina:
            disciplina_para_exclusao = dados_disciplina
            break
    if disciplina_para_exclusao is None:
        print(f"A Disciplina com o código {codigo_exclusao_disciplina} não foi localizado!")
    else:
        arquivo_disciplinas.remove(disciplina_para_exclusao)
        salvar_arquivo_em_json(arquivo_disciplinas, nome_arquivo)
        print("Disciplina excluída com sucesso!")
        print("As disciplinas cadastradas são:")
    for dados_disciplina in arquivo_disciplinas:
        print(dados_disciplina)
    if len(arquivo_disciplinas) == 0:
        print("Não há disciplinas cadastrados.")
        print(" ")

# Funções Professores
def incluir_cadastros_professores(nome_arquivo):
    arquivo_professores = ler_arquivo_em_json(nome_arquivo)
    while True:
        try:
            codigo_professor = int(input("Informe o Código do Professor (apenas números): "))
            if any(p["Código do Professor"] == codigo_professor for p in arquivo_professores):
                print(f"Já existe um professor com o Código {codigo_professor} cadastrado! Por gentileza, insira um código diferente.")
            else:
                break
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")
    nome_professor = input("Informe o Nome do Professor: ")
    cpf_professor = input("Informe o CPF do Professor: ")
    dados_professor = {"Código do Professor": codigo_professor, "Nome do Professor": nome_professor, "CPF do Professor": cpf_professor}
    arquivo_professores.append(dados_professor)
    salvar_arquivo_em_json(arquivo_professores, nome_arquivo)
    print(" ")
    print("Professor incluído com sucesso!")
    print(" ")
    print("Os professores cadastrados são:")
    for dados_professor in arquivo_professores:
        print(dados_professor)

def atualizar_cadastros_professores(nome_arquivo):
    arquivo_professores = ler_arquivo_em_json(nome_arquivo)
    while True:
        try:
            codigo_edicao_professor = int(input("Qual o Código do Professor que deseja editar? (apenas números): "))
            break
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")
    professor_para_edicao = None
    for dados_professor in arquivo_professores:
        if dados_professor["Código do Professor"] == codigo_edicao_professor:
            professor_para_edicao = dados_professor
            break
    if professor_para_edicao is None:
        print(f"O Professor com código {codigo_edicao_professor} não foi localizado.")
        print("Os professores cadastrados são:")
    else:
        # Validação do novo código do professor
        while True:
            try:
                professor_para_edicao["Código do Professor"] = int(input("Informe o novo Código do Professor: "))
                break
            except ValueError:
                print("Entrada inválida! Por favor, digite apenas números.")
        professor_para_edicao["Nome do Professor"] = input("Informe o novo Nome do Professor: ")
        professor_para_edicao["CPF do Professor"] = input("Informe o novo CPF do Professor: ")
        salvar_arquivo_em_json(arquivo_professores, nome_arquivo)
        print("Alteração realizada com sucesso!")
        print(" ")
        print("Os professores cadastrados são:")
    for dados_professor in arquivo_professores:
        print(dados_professor)

def excluir_cadastros_professores(nome_arquivo):
    arquivo_professores = ler_arquivo_em_json(nome_arquivo)
    while True:
        try:
            codigo_exclusao_professor = int(input("Qual o código que deseja excluir?: "))
            break
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")
    professor_para_exclusao = None
    for dados_professor in arquivo_professores:
        if dados_professor["Código do Professor"] == codigo_exclusao_professor:
            professor_para_exclusao = dados_professor
            break
    if professor_para_exclusao is None:
        print(f"O Professor com o código {codigo_exclusao_professor} não foi localizado!")
    else:
        arquivo_professores.remove(professor_para_exclusao)
        salvar_arquivo_em_json(arquivo_professores, nome_arquivo)
        print("Professor excluído com sucesso!")
        print("Os professores cadastrados são:")
    for dados_professor in arquivo_professores:
        print(dados_professor)
    if len(arquivo_professores) == 0:
        print("Não há professores cadastrados.")
        print(" ")

# Funções Turmas
def incluir_cadastros_turmas(nome_arquivo):
    arquivo_turmas = ler_arquivo_em_json(nome_arquivo)
    while True:
        codigo_turma = ler_numero("Informe o Código da Turma (apenas números): ")
        if any(t["Código da Turma"] == codigo_turma for t in arquivo_turmas):
            print(f"Código {codigo_turma} já existe! Por gentileza, insira um código diferente.")
        else:
            break
        # validar professor
    while True:
        codigo_prof = ler_numero("Informe o Código do Professor responsável pela turma (apenas números): ")
        professores_lista = ler_arquivo_em_json(arquivo_professores)
        if not professores_lista:
            print("Não há professores cadastrados. Cadastre um professor antes de criar turmas.")
            return
        if any(p["Código do Professor"] == codigo_prof for p in professores_lista):
            break
        else:
            print(f"Professor com código {codigo_prof} não encontrado. Cadastre o professor antes ou digite outro código.")
        # validar disciplina
    while True:
        codigo_disc = ler_numero("Informe o Código da Disciplina dessa turma (apenas números): ")
        disciplinas_lista = ler_arquivo_em_json(arquivo_disciplinas)
        if not disciplinas_lista:
            print("Não há disciplinas cadastradas. Cadastre uma disciplina antes de criar turmas.")
            return
        if any(d["Código da Disciplina"] == codigo_disc for d in disciplinas_lista):
            break
        else:
            print(f"Disciplina com código {codigo_disc} não encontrada. Cadastre a disciplina antes ou digite outro código.")
    dados_turma = {"Código da Turma": codigo_turma, "Código do Professor": codigo_prof, "Código da Disciplina": codigo_disc}
    arquivo_turmas.append(dados_turma)
    salvar_arquivo_em_json(arquivo_turmas, nome_arquivo)
    print(" ")
    print("Turma incluída com sucesso!")
    print(" ")
    print("As turmas cadastrados são:")
    for dados_turma in arquivo_turmas:
        print(dados_turma)

def atualizar_cadastros_turmas(nome_arquivo):
    arquivo_turmas = ler_arquivo_em_json(nome_arquivo)
    codigo_edicao_turma = ler_numero("Qual o Código da Turma que deseja editar? (apenas números): ")
    turma_para_edicao = None
    for t in arquivo_turmas:
        if t["Código da Turma"] == codigo_edicao_turma:
            turma_para_edicao = t
            break
    if turma_para_edicao is None:
        print(f"A Turma com código {codigo_edicao_turma} não foi localizada.")
    else:
        while True:
            novo_codigo = ler_numero("Informe o novo Código da Turma: ")
            if novo_codigo != codigo_edicao_turma and any(x["Código da Turma"] == novo_codigo for x in arquivo_turmas):
                print(f"Código {novo_codigo} já existe! Tente outro.")
            else:
                turma_para_edicao["Código da Turma"] = novo_codigo
                break
        # validar professor e disciplina novamente
        while True:
            codigo_prof = ler_numero("Informe o novo Código do Professor responsável pela turma (apenas números): ")
            professores_lista = ler_arquivo_em_json(arquivo_professores)
            if not professores_lista:
                print("Não há professores cadastrados. Cadastre um professor antes de editar turmas.")
                return
            if any(p["Código do Professor"] == codigo_prof for p in professores_lista):
                turma_para_edicao["Código do Professor"] = codigo_prof
                break
            else:
                print(f"Professor com código {codigo_prof} não encontrado.")
        while True:
            codigo_disc = ler_numero("Informe o novo Código da Disciplina dessa turma (apenas números): ")
            disciplinas_lista = ler_arquivo_em_json(arquivo_disciplinas)
            if not disciplinas_lista:
                print("Não há disciplinas cadastradas. Cadastre uma disciplina antes de editar turmas.")
                return
            if any(d["Código da Disciplina"] == codigo_disc for d in disciplinas_lista):
                turma_para_edicao["Código da Disciplina"] = codigo_disc
                break
            else:
                print(f"Disciplina com código {codigo_disc} não encontrada.")
        salvar_arquivo_em_json(arquivo_turmas, nome_arquivo)
        print("Alteração realizada com sucesso!")
        print(" ")
        print("Os professores cadastrados são:")
    for dados_turma in arquivo_turmas:
        print(dados_turma)

def excluir_cadastros_turmas(nome_arquivo):
    arquivo_turmas = ler_arquivo_em_json(nome_arquivo)
    while True:
        try:
            codigo_exclusao_turma = int(input("Qual o código da turma que deseja excluir?: "))
            break
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")
    turma_para_exclusao = None
    for dados_turma in arquivo_turmas:
        if dados_turma["Código da Turma"] == codigo_exclusao_turma:
            turma_para_exclusao = dados_turma
            break
    if turma_para_exclusao is None:
        print(f"A Turma com o código {codigo_exclusao_turma} não foi localizado!")
    else:
        arquivo_turmas.remove(turma_para_exclusao)
        salvar_arquivo_em_json(arquivo_turmas, nome_arquivo)
        print("Turma excluída com sucesso!")
        print("As turmas cadastradas são:")
    for dados_turma in arquivo_turmas:
        print(dados_turma)
    if len(arquivo_turmas) == 0:
        print("Não há turmas cadastradass.")
        print(" ")

# Funções Matricuals
def incluir_cadastros_matriculas(nome_arquivo):
    arquivo_matriculas = ler_arquivo_em_json(nome_arquivo)
    while True:
        codigo_turma = ler_numero("Informe o Código da Turma para a Matrícula (apenas números): ")
        turmas_lista = ler_arquivo_em_json(arquivo_turmas)
        if not any(t["Código da Turma"] == codigo_turma for t in turmas_lista):
            print(f"Turma com o Código {codigo_turma} não encontrada! Por gentileza, insira um código diferente.")
            continue
        codigo_aluno = ler_numero("Informe o Código do Aluno para a Matrícula (apenas números): ")
        alunos_lista = ler_arquivo_em_json(arquivo_alunos)
        if not any(a["Código do Aluno"] == codigo_aluno for a in alunos_lista):
            print(f"Aluno com código {codigo_aluno} não encontrado! Por gentileza, insira um código diferente.")
            continue
        if any(m["Código da Turma"] == codigo_turma and m["Código do Aluno"] == codigo_aluno for m in
               arquivo_matriculas):
            print("A matrícula selecionada já existe! Por gentileza, insira uma combinação diferente.")
            continue
        dados_matricula = {"Código da Turma": codigo_turma, "Código do Aluno": codigo_aluno}
        arquivo_matriculas.append(dados_matricula)
        salvar_arquivo_em_json(arquivo_matriculas, nome_arquivo)
        print(" ")
        print("Matricula incluída com sucesso!")
        print(" ")
        print("As matrículas cadastrados são:")
        for dados_matricula in arquivo_matriculas:
            print(dados_matricula)
        break

def atualizar_cadastros_matriculas(nome_arquivo):
    arquivo_matriculas = ler_arquivo_em_json(nome_arquivo)
    codigo_turma_busca_edicao = ler_numero("Informe o Código da Turma da matrícula que deseja editar (apenas números): ")
    codigo_aluno_busca_edicao = ler_numero("Informe o Código do Aluno da matrícula que deseja editar (apenas números): ")
    matricula_para_edicao = None
    for m in arquivo_matriculas:
        if m["Código da Turma"] == codigo_turma_busca_edicao and m["Código do Aluno"] == codigo_aluno_busca_edicao:
            matricula_para_edicao = m
            break
    if matricula_para_edicao is None:
        print("Matrícula não localizada.")
    else:
        # Validar e atualizar a nova turma e o novo aluno
        while True:
            novo_codigo_turma = ler_numero("Informe o novo Código da Turma (apenas números): ")
            turmas_lista = ler_arquivo_em_json(arquivo_turmas)
            if not any(t["Código da Turma"] == novo_codigo_turma for t in turmas_lista):
                print(f"Turma com código {novo_codigo_turma} não foi localizada.")
            else:
                break
        while True:
            novo_codigo_aluno = ler_numero("Informe o novo Código do Aluno (apenas números): ")
            alunos_lista = ler_arquivo_em_json(arquivo_alunos)
            if not any(a["Código do Aluno"] == novo_codigo_aluno for a in alunos_lista):
                print(f"Aluno com código {novo_codigo_aluno} não foi localizado.")
            else:
                break
        # verificar duplicidade (ignora a própria matrícula sendo editada)
        if any(m["Código da Turma"] == novo_codigo_turma and m["Código do Aluno"] == novo_codigo_aluno for m in arquivo_matriculas if m is not matricula_para_edicao):
            print("Já existe outra matrícula com essa turma e estudante. Operação cancelada.")
        else:
            matricula_para_edicao["Código da Turma"] = novo_codigo_turma
            matricula_para_edicao["Código do Aluno"] = novo_codigo_aluno
            salvar_arquivo_em_json(arquivo_matriculas, nome_arquivo)
            print("Alteração realizada com sucesso!")
    print("Matrículas cadastradas:")
    for m in arquivo_matriculas:
        print(m)

def excluir_cadastros_matriculas(nome_arquivo):
    arquivo_matriculas = ler_arquivo_em_json(nome_arquivo)
    codigo_turma = ler_numero("Informe o Código da Turma da matrícula que deseja excluir (apenas números): ")
    codigo_aluno = ler_numero("Informe o Código do Estudante da matrícula que deseja excluir (apenas números): ")
    matricula_para_exclusao = None
    for m in arquivo_matriculas:
        if m["Código da Turma"] == codigo_turma and m["Código do Aluno"] == codigo_aluno:
            matricula_para_exclusao = m
            break
    if matricula_para_exclusao is None:
        print("Matrícula não localizada.")
    else:
        arquivo_matriculas.remove(matricula_para_exclusao)
        salvar_arquivo_em_json(arquivo_matriculas, nome_arquivo)
        print("Matrícula excluída com sucesso.")
    print("As Matrículas cadastradas são: ")
    for m in arquivo_matriculas:
        print(m)
    if len(arquivo_matriculas) == 0:
        print("Não há matrículas cadastradas.")
        print(" ")

# Listas iniciais do sistema
arquivo_alunos = "alunos.json"
arquivo_disciplinas = "disciplinas.json"
arquivo_professores = "professores.json"
arquivo_turmas = "turmas.json"
arquivo_matriculas = "matriculas.json"

while True:
    # Menu de seleção principal (inicial)
    opcao = mostrar_menu_principal()
    # Navegando pelo menu secundário (operações)
    if opcao == '1':
        print("Você escolheu a opção: 1. Gerenciamento de Alunos")
        print(" ")
        while True:
            print("-- [ALUNOS] MENU DE OPERAÇÕES --")
            print(" ")
            alu = mostrar_menu_operacoes()
            if not processar_menu_operacoes(alu, arquivo_alunos, 'alunos'):
                break
    elif opcao == '2':
        print("Você escolheu a opção: 2. Gerenciamento de Disciplinas")
        print(" ")
        while True:
            print("-- [DISCIPLINAS] MENU DE OPERAÇÕES --")
            print(" ")
            disc = mostrar_menu_operacoes()
            if not processar_menu_operacoes(disc, arquivo_disciplinas, 'disciplinas'):
                break
    elif opcao == '3':
        print("Você escolheu a opção: 3. Gerenciamento de Professores")
        print(" ")
        while True:
            print("-- [PROFESSORES] MENU DE OPERAÇÕES --")
            print(" ")
            prof = mostrar_menu_operacoes()
            if not processar_menu_operacoes(prof, arquivo_professores, 'professores'):
                break
    elif opcao == '4':
        print("Você escolheu a opção: 4. Gerenciamento de Turmas")
        print(" ")
        while True:
            print("-- [TURMAS] MENU DE OPERAÇÕES --")
            print(" ")
            tur = mostrar_menu_operacoes()
            if not processar_menu_operacoes(tur, arquivo_turmas, 'turmas'):
                break
    elif opcao == '5':
        print("Você escolheu a opção: 5. Gerenciamento de Matrículas")
        print(" ")
        while True:
            print("-- [MATRÍCULAS] MENU DE OPERAÇÕES --")
            print(" ")
            matr = mostrar_menu_operacoes()
            if not processar_menu_operacoes(matr, arquivo_matriculas, 'matriculas'):
                break
    elif opcao == '9':
        print("Você escolheu sair.")
        break
    else:
        print("Opção inválida, selecione outra opção!")
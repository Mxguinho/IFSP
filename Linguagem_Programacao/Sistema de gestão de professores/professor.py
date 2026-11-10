from conexao import conectar


def cadastrar_professor():
    # solicitar as informações
    nome = input("Digite o nome do professor: ")
    email = input("Digite o email do professor: ")
    disciplinas = input("Digite as disciplinas: ")

    if not nome or not email or not disciplinas:
        print("Preencha os campos corretamente!!!")
    else:
        # fazer a conexao
        conexao = conectar()
        # criamos o comunicador
        cursor = conexao.cursor()

        # instrução SQL
        sql = "insert into professores(nome, email, disciplinas) values(%s, %s, %s)"

        # tupla de valores

        valores = (nome, email, disciplinas)

        cursor.execute(sql, valores)

        # confirmar a gravação

        conexao.commit()

        print("professor cadastrado com sucesso!")
        print("ID do professor: ", cursor.lastrowid)

        conexao.close()
        cursor.close()


def listar_professores():
    # fazer a conexao
    conexao = conectar()
    # criamos o comunicador
    cursor = conexao.cursor()

    # instrução sql de consulta
    sql = "select * from professores"

    # executar consulta

    cursor.execute(sql)

    # recuperar os dados

    professores = cursor.fetchall()

    if professores:
        print("Lista de Professores")
        for registro in professores:
            print(
                f"ID: {registro[0]}, professor: {registro[1]}, email: {registro[2]}, disciplinas: {registro[3]}"
            )
        print("\n\n")
    else:
        print("nenhum professor encontrado!!!")

    conexao.close()
    cursor.close()


def buscar_professor_id():
    conexao = conectar()
    cursor = conexao.cursor()

    id = int(input("Informe o ID do professor: "))

    sql = "SELECT * FROM professores WHERE id_prof = %s"
    # criando a tupla com o id informado
    parametro = (id,)
    # executar a intrução sql
    cursor.execute(sql, parametro)

    professor = cursor.fetchone()

    if professor:
        print("Dados do professor: ")
        print(
            f"ID: {professor[0]} - Nome: {professor[1]} - Email: {professor[2]} - Disciplinas: {professor[3]}"
        )
    else:
        print("Não existe professor com o ID informado!!!")

    conexao.close()
    cursor.close()


def buscar_professor_nome():
    conexao = conectar()
    cursor = conexao.cursor()

    nome = input("Informe o nome do professor: ")

    sql = "SELECT * FROM professores WHERE nome LIKE %s"
    # criando a tupla com o id informado
    parametro = (f"%{nome}%",)

    # executar a intrução sql
    cursor.execute(sql, parametro)

    professores = cursor.fetchall()

    if professores:
        print("Lista de Professores")
        for registro in professores:
            print(
                f"ID: {registro[0]}, professor: {registro[1]}, email: {registro[2]}, disciplinas: {registro[3]}"
            )
        print("\n\n")
    else:
        print("Não existe professor com o nome informado!!!")

    conexao.close()
    cursor.close()


def alterar_professor():
    conexao = conectar()
    cursor = conexao.cursor()

    id = int(input("Informe o ID do professor que deseja alterar: "))

    # solicitar as informações
    nome = input("Digite o novo nome do professor: ")
    email = input("Digite o novo email do professor: ")
    disciplinas = input("Digite a nova disciplinas: ")

    if not nome or not email or not disciplinas:
        print("Preencha os campos corretamente!!!")
    else:
        # instrução SQL
        sql = "UPDATE professores SET nome = %s, email = %s, disciplinas = %s WHERE id_prof = %s"

        # tupla de valores

        parametros = (nome, email, disciplinas, id)

        cursor.execute(sql, parametros)

        # confirmar a gravação

        conexao.commit()

        if cursor.rowcount > 0:
            print("professor atualizado com sucesso!")
        else:
            print("Não existe professor com o ID informado!!!")

    conexao.close()
    cursor.close()


def excluir_professor():
    conexao = conectar()
    cursor = conexao.cursor()

    id = int(input("Informe o ID do professor que deseja deletar: "))
    confirmação = input('Tem certeza(digite "SIM")???: ')
    if confirmação.upper == "SIM":
        sql = "DELETE FROM professores WHERE id_prof = %s"
        # criando a tupla com o id informado
        parametro = (id,)

        # executar a intrução sql
        cursor.execute(sql, parametro)

        professor = cursor.fetchone()

        conexao.commit()

        if cursor.rowcount > 0:
            print("professor deletado com sucesso!")
        else:
            print("Não existe professor com o ID informado!!!")
    else:
        print("Operação cancelada!")

    conexao.close()
    cursor.close()

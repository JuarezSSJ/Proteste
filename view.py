# importando SQLite
import sqlite3

# CRUD
# -> Creaty = inserir / criar
# -> Ready = acessar / mostrar
# -> Update = atualizar /
# -> Delete = deletar / apagar

# criando a conexão com o bd
conexao = sqlite3.connect("db_proteste.db")


# função cadastrar
def cadastrar_info(table, campos_tabela, inf):
    with conexao:
        cur = conexao.cursor()
        # comandos do SQL
        campos = ""
        valores = ""
        interrogacao = "?, "
        for campo in campos_tabela:
            campos += campo + ", "
            valores += interrogacao
        campos = campos[:-2]
        valores = valores[:-2]
        query = f"INSERT INTO {table} ({campos}) VALUES ({valores})"
        print(query)
        # comando para executar o query
        cur.execute(query, inf)


def verificar_cadastro(login, senha):
    with conexao:
        cur = conexao.cursor()
        query = "SELECT * FROM tb_login WHERE login = ? AND senha = ?"
        cur.execute(query, (login, senha))
        resultado = cur.fetchone()

        if resultado is not None:
            # O usuário e senha estão cadastrados
            return True
        else:
            # O usuário e senha não estão cadastrados
            return False


def esqueci_senha(email, cpf):
    with conexao:
        cur = conexao.cursor()
        query = "SELECT * FROM tb_login WHERE email = ? AND cpf = ?"
        cur.execute(query, (email, cpf))
        resultado = cur.fetchone()

        if resultado is not None:
            # O usuário e senha estão cadastrados
            return True
        else:
            # O usuário e senha não estão cadastrados
            return False


# acessar informações
def apresentar_info(tabela):
    lista_apresentar = []
    with conexao:
        cur = conexao.cursor()
        # * - sig tudo
        query = f"SELECT * FROM {tabela}"
        cur.execute(query)
        info = cur.fetchall()
        # corre toda a lista da info e mandar para a lista_apresentar
        for i in info:
            lista_apresentar.append(i)
    return lista_apresentar


# função atualizar
def atualizar_info(i):
    with conexao:
        cur = conexao.cursor()
        query = "UPDATE formulario SET nome=?, email=?, telefone=?, data_consulta=?, situacao=?, observacao=? WHERE id=?"
        cur.execute(query, i)


# função deletar
def deletar_info(i):
    with conexao:
        cur = conexao.cursor()
        query = "DELETE FROM formulario WHERE id=?"
        cur.execute(query, i)


# acessar informações para analisar
def analisar_info():
    lista_coluna_analisar = []
    with conexao:
        cur = conexao.cursor()
        # * - sig tudo
        query = "SELECT COUNT (DISTINCT situacao) FROM formulario"
        cur.execute(query)
        info = cur.fetchall()
        # corre toda a lista da info e mandar para a lista_apresentar
        for i in info:
            lista_coluna_analisar.append(i)
    return lista_coluna_analisar


tb_login_vars = ['nome', 'cpf', 'email', 'login', 'senha']
tb_plano_vars = ['nome', 'id_login']
tb_casoteste_vars = ['fase_desenvolvimento', 'fase_teste', 'id_plano']
tb_abordagem_vars = ['descricao', 'id_caso']
tb_artefatos_vars = ['entrada', 'saida', 'id_caso']
tb_projeto_vars = ['nome', 'requisitante',
                   'gerente_projeto', 'id_plano', 'cenario_operacional']
tb_marcos_vars = ['descricao', 'id_projeto']
tb_premissas_vars = ['descricao', 'id_plano']
tb_recursos_vars = ['tipo_recurso', 'quantidade', 'descricao', 'id_projeto']
tb_recursoshumanos_vars = ['nome', 'papel', 'responsabilidade', 'id_projeto']
tb_relatorios_vars = ['tipo_relatorio', 'objetivo',
                      'destinatario', 'periodicidade', 'id_projeto']
tb_restricoes_vars = ['descricao', 'id_plano']
tb_riscos_vars = ['descricao', 'id_projeto']

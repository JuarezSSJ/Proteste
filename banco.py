# importando SQLite3
import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('db_proteste.db')
cur = conn.cursor()

# Criar tabela tb_login
cur.execute('''CREATE TABLE IF NOT EXISTS tb_login (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf TEXT NOT NULL,
                email TEXT NOT NULL,
                login TEXT,
                senha TEXT,
                UNIQUE(cpf),
                UNIQUE(login),
                FOREIGN KEY(id) REFERENCES tb_plano(id_login)
            )''')

# Criar tabela tb_plano
cur.execute('''CREATE TABLE IF NOT EXISTS tb_plano (
                create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                update_at TIMESTAMP,
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                id_login INT NOT NULL,
                FOREIGN KEY(id_login) REFERENCES tb_login(id) ON DELETE CASCADE ON UPDATE CASCADE
            )''')

# Criar tabela tb_casoteste
cur.execute('''CREATE TABLE IF NOT EXISTS tb_casoteste (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fase_desenvolvimento VARCHAR(255),
                fase_teste VARCHAR(255),
                id_plano INT NOT NULL,
                FOREIGN KEY(id_plano) REFERENCES tb_plano(id) ON DELETE CASCADE ON UPDATE CASCADE
            )''')

# Criar tabela tb_abordagem
cur.execute('''CREATE TABLE IF NOT EXISTS tb_abordagem (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao VARCHAR(255),
                id_caso INT NOT NULL,
                FOREIGN KEY(id_caso) REFERENCES tb_casoteste(id) ON DELETE CASCADE ON UPDATE CASCADE
            )''')

# Criar tabela tb_artefatos
cur.execute('''CREATE TABLE IF NOT EXISTS tb_artefatos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                entrada VARCHAR(255) NOT NULL,
                saida VARCHAR(255) NOT NULL,
                id_caso INT NOT NULL,
                FOREIGN KEY(id_caso) REFERENCES tb_casoteste(id) ON DELETE CASCADE ON UPDATE CASCADE
            )''')

# Criar tabela tb_projeto
cur.execute('''CREATE TABLE IF NOT EXISTS tb_projeto (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(100) NOT NULL,
                requisitante VARCHAR(45) NOT NULL,
                gerente_projeto VARCHAR(45) NOT NULL,
                id_plano INT NOT NULL,
                cenario_operacional VARCHAR(255),
                FOREIGN KEY(id_plano) REFERENCES tb_plano(id) ON DELETE CASCADE ON UPDATE CASCADE
            )''')

# Criar tabela tb_marcos
cur.execute('''CREATE TABLE IF NOT EXISTS tb_marcos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao VARCHAR(255) NOT NULL,
                id_projeto INT NOT NULL,
                FOREIGN KEY(id_projeto) REFERENCES tb_projeto(id) ON DELETE NO ACTION ON UPDATE NO ACTION
            )''')

# Criar tabela tb_premissas
cur.execute('''CREATE TABLE IF NOT EXISTS tb_premissas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao VARCHAR(255) NOT NULL,
                id_plano INT NOT NULL,
                FOREIGN KEY(id_plano) REFERENCES tb_plano(id) ON DELETE CASCADE ON UPDATE CASCADE
            )''')

# Criar tabela tb_recursos
cur.execute('''CREATE TABLE IF NOT EXISTS tb_recursos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo_recurso INT NOT NULL,
                quantidade INT NOT NULL,
                descricao VARCHAR(255),
                id_projeto INT NOT NULL,
                FOREIGN KEY(id_projeto) REFERENCES tb_projeto(id) ON DELETE CASCADE ON UPDATE CASCADE
            )''')

# Criar tabela tb_recursoshumanos
cur.execute('''CREATE TABLE IF NOT EXISTS tb_recursoshumanos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(45) NOT NULL,
                papel VARCHAR(45) NOT NULL,
                responsabilidade VARCHAR(255),
                id_projeto INT NOT NULL,
                FOREIGN KEY(id_projeto) REFERENCES tb_projeto(id) ON DELETE CASCADE ON UPDATE CASCADE
            )''')

# Criar tabela tb_relatorios
cur.execute('''CREATE TABLE IF NOT EXISTS tb_relatorios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo_relatorio VARCHAR(45) NOT NULL,
                objetivo VARCHAR(100) NOT NULL,
                destinatario VARCHAR(45) NOT NULL,
                periodicidade VARCHAR(45) NOT NULL,
                id_projeto INT NOT NULL,
                FOREIGN KEY(id_projeto) REFERENCES tb_projeto(id) ON DELETE CASCADE ON UPDATE CASCADE
            )''')

# Criar tabela tb_restricoes
cur.execute('''CREATE TABLE IF NOT EXISTS tb_restricoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao VARCHAR(255),
                id_plano INT NOT NULL,
                FOREIGN KEY(id_plano) REFERENCES tb_plano(id) ON DELETE CASCADE ON UPDATE CASCADE
            )''')

# Criar tabela tb_riscos
cur.execute('''CREATE TABLE IF NOT EXISTS tb_riscos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao VARCHAR(255) NOT NULL,
                id_projeto INT NOT NULL,
                FOREIGN KEY(id_projeto) REFERENCES tb_projeto(id) ON DELETE CASCADE ON UPDATE CASCADE
            )''')

# Fechar a conexão com o banco de dados
conn.close()

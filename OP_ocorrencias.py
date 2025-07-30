# Sistema de Cadastro de Ocorrências - IEMA Timon
#Importando um banco de dados local - SQlite3
import sqlite3

# Criação e conexão com o banco de dados SQLite
try:
    con = sqlite3.connect('System_PL')
    print("Conexão com banco de dados realizada com sucesso!")
except sqlite3.Error as e:
    print("ERRO: conexão falhada!", e)

# Criação da tabela de ocorrências de alunos
try:
    with con:
        alu = con.cursor()
        alu.execute("""
            CREATE TABLE IF NOT EXISTS dados_ocorrencias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                data_ocorrencia DATE,
                curso TEXT,
                codigo_ocorrencia TEXT,
                turma INT,
                professor TEXT,
                disciplina TEXT
            )
        """)
        print("Tabela 'dados_ocorrencias' criada com sucesso!")
except sqlite3.Error as e:
    print("ERRO ao criar tabela 'dados_ocorrencias':", e)

# Criação da tabela de dados das ocorrências
try:
    with con:
        alu = con.cursor()
        alu.execute("""
            CREATE TABLE IF NOT EXISTS dados_ocorrencia (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                disciplina TEXT,
                data DATE,
                professor_responsavel TEXT,
                codigo TEXT,
                frequencia INT,
                FOREIGN KEY (codigo) REFERENCES dados_ocorrencias (codigo_ocorrencia) 
                    ON UPDATE CASCADE 
                    ON DELETE CASCADE
            )
        """)
        print("Tabela 'dados_ocorrencia' criada com sucesso!")
except sqlite3.Error as e:
    print("ERRO ao criar tabela 'dados_ocorrencia':", e)

#Funções para operacoes com a tabela 'dados_ocorrencias'
def inserir_aluno(dados):
    with con:
        cursor = con.cursor()
        query = """
            INSERT INTO dados_ocorrencias
            (nome, data_ocorrencia, curso, codigo_ocorrencia, turma, professor, disciplina)
            VALUES (?, ?, ?, ?, ?, ?, ?)"""
        cursor.execute(query, dados)


def ver_alunos():
    with con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM dados_ocorrencias")
        return cursor.fetchall()
    

def modificar_aluno(dados):
    with con:
        cursor = con.cursor()
        query = """
            UPDATE dados_ocorrencias
            SET nome=?, data_ocorrencia=?, curso=?, codigo_ocorrencia=?, turma=?, professor=?, disciplina=?
            WHERE id=?"""
        cursor.execute(query, dados)


def deletar_aluno(id_aluno):
    with con:
        cursor = con.cursor()
        query = "DELETE FROM dados_ocorrencias WHERE id=?"
        cursor.execute(query, (id_aluno,))


# Funções para a tabela 'dados_ocorrencia'
def criar_ocorrencia(dados):
    with con:
        cursor = con.cursor()
        query = """
            INSERT INTO dados_ocorrencia 
            (disciplina, data, professor_responsavel, codigo, frequencia) 
            VALUES (?, ?, ?, ?, ?)"""
        cursor.execute(query, dados)


def ver_ocorrencias():
    with con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM dados_ocorrencia")
        return cursor.fetchall()


def modificar_ocorrencia(dados):
    with con:
        cursor = con.cursor()
        query = """
            UPDATE dados_ocorrencia 
            SET disciplina=?, data=?, professor_responsavel=?, codigo=?, frequencia=? 
            WHERE id=?"""
        cursor.execute(query, dados)


def deletar_ocorrencia(id_ocorrencia):
    with con:
        cursor = con.cursor()
        query = "DELETE FROM dados_ocorrencia WHERE id=?"
        cursor.execute(query, (id_ocorrencia,))

def buscar_aluno_por_nome(nome):
    with con:
        cursor = con.cursor()
        query = "SELECT * FROM dados_ocorrencias WHERE nome LIKE ?"
        cursor.execute(query, (f"%{nome}%",))
        return cursor.fetchall()



# Exemplo de uso (descomente para testar)
# inserir_aluno(["Ana Paula", "2025-06-01", "Informática", "A01", 303, "Prof. Marcos", "Matemática"])
# print(ver_alunos())
# modificar_aluno(["João Silva", "2025-05-30", "Química", "A02", 304, "Prof. Carlos", "Química", 1])
# deletar_aluno(1)
# criar_ocorrencia(["Matemática", "2025-06-02", "Prof. Marcos", "A01", 2])
# print(ver_ocorrencias())

# importando banco de dados com SQLITE3

import sqlite3

#criando conexao

try: 
    con = sqlite3.connect('System_PL')
    print("conexão com banco de dados realizada com sucesso!")
except sqlite3.Error as e:
    print("ERROR: conexão falhada!", e)

#criando tabela com dados dos alunos

try:
    with con:
        alu = con.cursor()
        alu.execute("""
             CREATE TABLE IF NOT EXISTS 
    dados_Alunos(
             id INTEGER PRIMARY KEY
    AUTOINCREMENT,
                    nome TEXT,
                    data DATE,
                    curso TEXT,
                    serie INT, 
                    codigo_ocorrencia TEXT,
                    turma INT
            )
        """)
        print("Tabela de alunos criada com sucesso!")
except sqlite3.Error as e:
    print("ERRO ao criar tabela de alunos", e)

#criando tabela com dados da ocorrencia

try:
    with con:
        alu = con.cursor()
        alu.execute("""
             CREATE TABLE IF NOT EXISTS dados_Ocorrencia(
             id INTEGER PRIMARY KEY AUTOINCREMENT,
                    disciplina TEXT,
                    data DATE,
                    professor responsavel TEXT,
                    codigo INT,
                    frequencia INT,
                    FOREIGN KEY (codigo) REFERENCES dados_alunos (codigo_ocorrencia) ON UPDATE CASCADE ON DELETE CASCADE              
            )
        """)
        print("Tabela ocorrencias criada com sucesso!")
except sqlite3.Error as e:
    print("ERRO ao criar tabela de ocorrencia", e)
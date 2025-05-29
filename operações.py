# importando banco de dados com SQLITE3

import sqlite3 as lite

#criando conexao

try: 
    con = lite.connect('System_PL')
    print("conexão com banco de dados realizada com sucesso!")
except sqlite3.Error as e:
    print("ERROR: conexão falhada!", e)

# Trabalhando com a tabela de alunos-------------------------

#Inserindo alunos na tabela "Dados_Alunos" (CRIAR)
def inserir_alunos(i):
    with con:
        alu = con.cursor()
         #Recebe os comando insert do SQL
        query = "INSERT INTO dados_Alunos (nome, data, curso, serie, codigo_ocorrencia, turma) VALUES (?,?,?,?,?,?)"
        alu.execute(query,i)

#inserir_alunos(['Lucas' , '2025-05-28' , 'Informatica' , '3' , '01' , '303'])
#modelo padrão para preeenchimento da tabela alunos

#Ver todos os alunos cadastrados (SELECT) (LER)
def ver_alunos():
    lista = []
    with con:
        alu = con.cursor()
        #Comando SQL para o SELECT
        alu.execute('SELECT * FROM dados_Alunos')
        linha = alu.fetchall()

        for i in linha:
            lista.append(i)
    return lista
print(ver_alunos())

#Modificar dados dos alunos (MODIFICAR)

def mod_alunos(i):
    with con:
        alu = con.cursor()
         #Recebe os comando UPDATE do SQL
        query = "UPDATE dados_Alunos SET nome=?, data=?, curso=?, serie=?, codigo_ocorrencia=?, turma=? WHERE id = ?"
        alu.execute(query,i)

#Teste de modificação utilizando a função "mod_alunos"
l = ['Francisco Henzo', '2025-05-28', 'Informatica', 3, 0.2, 303, 2] #ID vai por ultimo quando listar as modificações
mod_alunos(l)    

#Função DELETAR 
def deletar_alunos(i):
    with con:
        alu = con.cursor()
         #Recebe os comando DELETE do SQL
        query = "DELETE FROM dados_Alunos WHERE id=?"
        alu.execute(query,i)

deletar_alunos([1])    
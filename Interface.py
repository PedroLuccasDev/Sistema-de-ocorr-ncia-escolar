#Importanto TKinter (Responsavel por criar a interface grafica)

from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
from tkcalendar import DateEntry

#Importando pillow (Utilização dos icons durante a aplicação
from PIL import ImageTk, Image

#Importando "operações" com o banco de dados (Crucial para o funcionamento do sistema)
from OP_ocorrencias import *

#Importando biblioteca responsavel por criar um arquivo pdf com os registros (Presente na função "salvar")
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import datetime


#Cores Utilizadas durante a aplicação
cor0 = "#030303" #PRETO
cor1 = "#feffff" #BRANCO
cor2 = "#857e7eb4" #CINZA
cor3 = "#00a095" #CIANO
cor4 = "#403d3d" #CINZA ESCURO (LETRA)
cor5 = "#003452" #AZUL
cor6 = "#f90905" #VERMELHO
cor7 = "#038cfc" #AZUL CLARO
cor8 = "#0BBB3D" #VERDE CLARO
cor9 = "#FC16A0" #ROSA

#"Criando janela", definindo suas dimensões e seu título
janela = Tk()
janela.title("SISTEMA DE OCORRÊNCIA IEMA - PL")
janela.geometry("850x620")
janela.configure(background=cor1)
janela.resizable(width=FALSE, height=FALSE)
style = Style(janela)
style.theme_use("clam")

#Criando frames (Separando a janela em "pedaços" para melhor administração dos componentes)
#foram utilizados quatro frames, principais: Logo, Dados, Detalhes e Tabela. aparecendo de forma respectiva durante o .
#Frame logo: esta presente a tonalidade azul, com o titulo do sistema e a foto da logo do IEMA. 
frame_logo = Frame(janela, width=850, height=52, bg=cor7)
frame_logo.grid (row=0, column= 0, pady=0, padx=0, sticky=NSEW)

#criando linha para separar um frame do outro 
ttk.Separator(janela, orient=HORIZONTAL).grid (row=1, columnspan=1, ipadx=680)

frame_dados = Frame(janela, width=850, height=65, bg=cor1)
frame_dados.grid (row=2, column= 0, pady=0, padx=0, sticky=NSEW)

#criando linha para separar um frame do outro 
ttk.Separator(janela, orient=HORIZONTAL).grid (row=3, columnspan=1, ipadx=680)

frame_detalhes = Frame(janela, width=850, height=200, bg=cor1)
frame_detalhes.grid (row=4, column= 0, pady=0, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=850, height=200, bg=cor1)
frame_tabela.grid (row=5, column= 0, pady=0, padx=10, sticky=NSEW)

#Trabalhando com o frame logo (IMAGEM IEMA)------------------------
app_logo = Image.open('IEMA - LOGO.png')
app_logo = app_logo.resize((80,80))
app_logo = ImageTk.PhotoImage(app_logo)
app_lg = Label(frame_logo, image=app_logo,
                text= "                           SISTEMA DE OCORRÊNCIA",
                  width=1000,
                    compound=LEFT,
                    relief=RAISED,
                      anchor=NW,
                        font=("Ivy 18 bold"), bg=cor7, fg= cor1) #Font utilizada durante toda aplicação "Ivy".
app_lg.place(x=0, y=0)

#Função de control------------------------------------
#Responsável por fazer os botões funcionarem

def control(i):

#Função Botão de cadastro de ocorrências
#Cadastro de ocorrências
    if i == 'cadastro de ocorrencias':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

#Faz com que toda vez que clicamos em botão uma janela se "destrua" e seja construida outra (Evita sobreposições)

        for widget in frame_tabela.winfo_children():
            widget.destroy()

        #Chamando a função para adicionar as ocorrências no sistema
        ocorrencia()

#Salvar
    if i == 'salvar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()
        #Chamando a função para adicionar as ocorrências no sistema
        salvar() 


#BOTÃO DE REGISTRAR OCORRÊNCIAS DENTRO DO FRAME "DADOS"--------------------------------------

app_img_oco = Image.open('Confirmed.png') #Imagem utilizada para "Comfirmação"
app_img_oco = app_img_oco.resize((18,18))
app_img_oco = ImageTk.PhotoImage(app_img_oco)
app_ocorrencia = Button(frame_dados, command=lambda:control('cadastro de ocorrencias'), image=app_img_oco, text= "Registrar Ocorrências", width=170, compound=LEFT, overrelief=RIDGE, font=("Ivy 11"), bg=cor1, fg= cor0)
app_ocorrencia.place(x=10, y=30)

#--------------------------------------------------------------------------

#BOTÃO DE "SALVAR", DENTRO DO FRAME (Responsável por criar um arquivo PDF dos registros do sistema)
app_img_sav = Image.open('Save.png') #Importando imagem utilizada para simbolizar salvamento
app_img_sav = app_img_sav.resize((18,18))
app_img_sav = ImageTk.PhotoImage(app_img_sav)
app_save = Button(frame_dados, command=lambda:control('salvar'), image=app_img_sav, text= "Salvar", width=70, compound=LEFT, overrelief=RIDGE, font=("Ivy 11"), bg=cor1, fg= cor0)
app_save.place(x=190, y=30)

#Função para adicionar ocorrência------------------------------------
#quando clicamos em registrar ocorrencia, chamamos a função "ocorrencia", inicializando o formulario.

def ocorrencia():
    
#Inserindo os dados nas tabelas   (SALVAR DADOS DA OCORRENCIA)----------------

    def nova_ocorrencia():
        aluno = e_aluno.get()
        disciplina = e_disciplina.get()
        curso = e_curso.get()
        turma = e_turma.get()
        codigo = cb_cod.get()
        data_ocorrencia = e_data_ocorrencia.get()
        prof = e_prof.get()
        
        lista = [aluno, data_ocorrencia, curso, codigo, int(turma), prof, disciplina]

        #Verifcando se todos os campos foram preenchidos ou nao -----------------
        #Todos os campos devem ser preenchidos para que o sistema permita continuar
            
        if  "" in lista:

            messagebox.showerror('Erro', 'Preencha todos os campos!')
            return
        inserir_aluno(lista)
        #Exibindo mensagem de confirmação
        messagebox.showinfo('Sucesso', 'Ocorrência registrada com sucesso!')
        mostrar_ocorrencia()

#AÇÃO DO BOTÃO ATUALIZAR--------------------------------------------------
#Função responsavel pela atualização dos dados 
#Para que essa função funcione é necessario o usuario dê dois cliques em cima do registro que ele deseja modificar. 

    def preencher_campos(event): #Função responsavel por preencher os campos conforme ja esta no registro
        for selected_item in tree_Aluno.selection():
            valores = tree_Aluno.item(selected_item, 'values')
            if valores:
                e_aluno.delete(0, END)
                e_aluno.insert(0, valores[1])
                e_curso.delete(0, END)
                e_curso.insert(0, valores[2])
                e_turma.delete(0, END)
                e_turma.insert(0, valores[3])
                cb_cod.set(valores[4])
                dados = [x for x in ver_alunos() if str(x[0]) == str(valores[0])][0]
                e_data_ocorrencia.set_date(dados[2])
                e_prof.delete(0, END)
                e_prof.insert(0, dados[6])
                e_disciplina.delete(0, END)
                e_disciplina.insert(0, dados[7])
                e_aluno.id_atual = dados[0]

    def confirmar_alteracao(): #Exibe uma mensagem para que o usuario confirme sua alteração
        id_atual = getattr(e_aluno, 'id_atual', None)
        if not id_atual:
            messagebox.showwarning("Aviso", "Selecione uma ocorrência para atualizar.")
            return
        lista = [
            e_aluno.get(), e_data_ocorrencia.get(), e_curso.get(), cb_cod.get(),
            int(e_turma.get()), e_prof.get(), e_disciplina.get(), id_atual
        ]
        modificar_aluno(lista)
        messagebox.showinfo("Sucesso", "Ocorrência atualizada.")
        mostrar_ocorrencia()

#AÇÃO DO BOTÃO "DELETAR"------------------------------------------------------------------
#Função responsavel pela remoção dos registros 

    def deletar_ocorrencia():
        for item in tree_Aluno.selection():
            valores = tree_Aluno.item(item, 'values')
            if valores and messagebox.askyesno("Confirmar", "Deseja deletar esta ocorrência?"):
                deletar_aluno(int(valores[0]))
                messagebox.showinfo("Sucesso", "Ocorrência deletada.")
                mostrar_ocorrencia()

#AÇÃO DO BOTÃO "PROCURAR"
#Função responsavel por procurar o aluno dentro dos registros da tabela
    def procurar_Aluno():
        nome_procurado = e_procurar.get().strip()
        if not nome_procurado:
            messagebox.showwarning("Aviso", "Digite um nome para procurar.")
            return

        resultados = buscar_aluno_por_nome(nome_procurado)

        if resultados:
            for widget in frame_tabela.winfo_children():
                widget.destroy()

            list_header = ['ID','Nome','Curso','Turma', 'Código'] 
            global tree_Aluno
            tree_Aluno = ttk.Treeview(frame_tabela, selectmode="browse",columns=list_header, show="headings")

            vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_Aluno.yview)
            hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_Aluno.xview)

            tree_Aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
            tree_Aluno.grid(column=0, row=1, sticky='nsew')

            vsb.grid(column=2, row=1, sticky='ns')
            hsb.grid(column=0, row=2, sticky='ew')
            frame_tabela.grid_rowconfigure(0, weight=6)

            hd=["nw","nw","e","e","e"]
            h=[80,950,85,50,90]

            for i, col in enumerate (list_header):
                tree_Aluno.heading(col, text=col.title(), anchor=NW)
                tree_Aluno.column(col, width=h[i],anchor=hd[i])

            for item in resultados:
                id = item[0]
                nome = item[1]
                curso = item[3]
                turma = item[5]
                codigo = item[4]
                tree_Aluno.insert('', 'end', values=(id, nome, curso, turma, codigo))

            tree_Aluno.bind("<Double-1>", preencher_campos)

            messagebox.showinfo("Resultado", f"{len(resultados)} aluno(s) encontrado(s).")
        else:
            messagebox.showinfo("Nenhum resultado", "Nenhum aluno encontrado com esse nome.")

#Inserindo os dados
        inserir_aluno(lista)

        messagebox.showinfo('SUCESSO')
            
        e_aluno.delete(0, END)
        e_disciplina.delete(0, END)
        e_curso.delete(0, END)
        e_turma.delete(0, END)
        cb_cod.delete(0, END)
        e_data_ocorrencia.delete(0, END)
        e_prof.delete(0, END)

        mostrar_ocorrencia()



#Bloco de interação com "Aluno" (SLOT DE INTERAÇÃO COM USUÁRIO)

    l_aluno = Label(frame_detalhes, text="Aluno:", height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
    l_aluno.place(x=4, y=10)
    e_aluno = Entry(frame_detalhes, width=35, justify='left', relief='solid')
    e_aluno.place(x=7, y=35)

#Disciplina da ocorrencia (SLOT DE INTERAÇÃO COM USUÁRIO)

    l_disciplina = Label(frame_detalhes, text="Disciplina da ocorrência:", height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
    l_disciplina.place(x=4, y=70)
    e_disciplina = Entry(frame_detalhes, width=20, justify='left', relief='solid')
    e_disciplina.place(x=7, y=95)

#campo pro CURSO da ocorrencia (SLOT DE INTERAÇÃO COM USUÁRIO)

    l_curso = Label(frame_detalhes, text="Curso:", height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
    l_curso.place(x=230, y=10)
    e_curso = Entry(frame_detalhes, width=20, justify='left', relief='solid')
    e_curso.place(x=230, y=35)


#campo pra TURMA da ocorrencia (SLOT DE INTERAÇÃO COM USUÁRIO)

    l_turma = Label(frame_detalhes, text="Turma:", height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
    l_turma.place(x=230, y=70)
    e_turma = Entry(frame_detalhes, width=10, justify='left', relief='solid')
    e_turma.place(x=230, y=95)

#campo pra CODIGO DA OCORRÊNCIA da ocorrencia
#Criação de uma combo box para o codigo da ocorrencia (SLOT DE INTERAÇÃO COM USUÁRIO)
    cb_cod = Label(frame_detalhes, text="Código da ocorrência:", height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
    cb_cod.place(x=230, y=120)
    cb_cod = ttk.Combobox(frame_detalhes, width=7, font=('Ivy 10 '))
    cb_cod ['values'] = ('01', '02', '03', '04', '05', '06', '07')
    cb_cod.place(x=230, y=150)

#campo pra DATA DE NASCIMENTO DA OCORRÊNCIA da ocorrencia (SLOT DE INTERAÇÃO COM USUÁRIO)

    l_data_ocorrencia = Label(frame_detalhes, text="Data da Ocorrência:", height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
    l_data_ocorrencia.place(x=4, y=120)
    e_data_ocorrencia = DateEntry(frame_detalhes, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern= 'dd/mm/yyyy')
    e_data_ocorrencia.place(x=7, y=150)

#campo pro Professor responsavel DA OCORRÊNCIA da  (SLOT DE INTERAÇÃO COM USUÁRIO)

    l_prof = Label(frame_detalhes, text="Professor responsável:", height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
    l_prof.place(x=380, y=10)
    e_prof = Entry(frame_detalhes, width=25, justify='left', relief='solid')
    e_prof.place(x=380, y=35)

#Criando linha separatoria (VISUAL) para a aba "Procurar ocorrência"-------------------------

    l_linha = Label(frame_detalhes, relief= GROOVE, text='h', width=1, height=100, anchor=NW , font="Ivy 1", bg= cor1, fg= cor0)
    l_linha.place(x=610, y=10)

#Criação dp slot para buscar o aluno na tabela_ (SLOT DE INTERAÇÃO COM USUÁRIO) -------------------------------

    l_procurar = Label(frame_detalhes, text= "Procurar ocorrência/Aluno:", height=1, anchor=NW, font="Ivy 10 bold", bg=cor1, fg=cor4)
    l_procurar.place(x=620, y=10)
    e_procurar = Entry(frame_detalhes, width=25, justify='center', relief='solid')
    e_procurar.place(x=620, y=35)
    
#Botao "procurar" da aba busca por aluno
    botao_procurar = Button(frame_detalhes, command=procurar_Aluno, anchor=CENTER, text='Procurar'.upper(), width=10, overrelief=RIDGE, font='Ivy 7', bg=cor1, fg=cor0)
    botao_procurar.place(x=620, y=55)

#Botão "salvar" do frame detalhes
    botao_carregar = Button(frame_detalhes, command=nova_ocorrencia, anchor=CENTER, text='Salvar'.upper(), width=10, overrelief=RIDGE, font='Ivy 7', bg=cor8, fg=cor0)
    botao_carregar.place(x=380, y=170)

#Botao "deletar" do frame detalhes
    botao_deletar = Button(frame_detalhes, command=deletar_ocorrencia, anchor=CENTER, text='Deletar'.upper(), width=10, overrelief=RIDGE, font='Ivy 7', bg=cor6, fg=cor1)
    botao_deletar.place(x=450, y=170)

#Botão "atualizar" do frame detalhes
    botao_atualizar = Button(frame_detalhes, command=confirmar_alteracao, anchor=CENTER, text='Atualizar'.upper(), width=10, overrelief=RIDGE, font='Ivy 7', bg=cor3, fg=cor1)
    botao_atualizar.place(x=520, y=170)


#Criação da tabela com os dados DENTRO DO FRAME TABELA --------------------------------------
    def mostrar_ocorrencia():
        for widget in frame_tabela.winfo_children(): widget.destroy()
        lista = ver_alunos()
        df_list = ver_alunos()

      

        app_tabelaOco = Label(frame_tabela, text="Tabela de Ocorrências", height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
        app_tabelaOco.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

#Exibindo os codigos das ocorrências 
#Mensagens visuais para que o usuario saiba qual o codigo de cada ocorrencia (Canto inferior direito)
                  
        l_cod1 = Label(frame_tabela, text="CÓD 01: Desrespeito ao professor/técnico;", height=10, anchor=NW, font=('Ivy 12 bold'), bg=cor1, fg=cor4)
        l_cod1.place(x=445, y=30)

        l_cod2 = Label(frame_tabela, text="CÓD 02: Baixa produtividade durante a aula;", height=10, anchor=NW, font=('Ivy 12 bold'), bg=cor1, fg=cor4)
        l_cod2.place(x=445, y=60)

        l_cod3 = Label(frame_tabela, text="CÓD 03: Aluno tumultuando a sala;", height=10, anchor=NW, font=('Ivy 12 bold'), bg=cor1, fg=cor4)
        l_cod3.place(x=445, y=90)

        l_cod4 = Label(frame_tabela, text="CÓD 04: Excesso de conversa na aula", height=10, anchor=NW, font=('Ivy 12 bold'), bg=cor1, fg=cor4)
        l_cod4.place(x=445, y=120)

        l_cod1 = Label(frame_tabela, text="CÓD 05: Aluno fora de sala sem autorização", height=10, anchor=NW, font=('Ivy 12 bold'), bg=cor1, fg=cor4)
        l_cod1.place(x=445, y=150)

        l_cod1 = Label(frame_tabela, text="CÓD 06: Uso indevido do celular durante a aula", height=10, anchor=NW, font=('Ivy 12 bold'), bg=cor1, fg=cor4)
        l_cod1.place(x=445, y=180)

        l_cod1 = Label(frame_tabela, text="CÓD 07: OUTRA SITUAÇÃO", height=10, anchor=NW, font=('Ivy 12 bold'), bg=cor1, fg=cor4)
        l_cod1.place(x=445, y=210)

        #criando a treeview com duas scrollbars
        
        list_header = ['ID','Nome','Curso','Turma', 'Código'] 

        df_list = ver_alunos()

        global tree_Aluno

        tree_Aluno = ttk.Treeview(frame_tabela, selectmode="browse",columns=list_header, show="headings")

    #Vertical scrollbar
        vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_Aluno.yview)

    #Horizontal scrollbar
        hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_Aluno.xview)

        tree_Aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_Aluno.grid(column=0, row=1, sticky='nsew')

        vsb.grid(column=2, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela.grid_rowconfigure(0, weight=6)

        hd=["nw","nw","e","e","e"]
        h=[80,950,85,50,90]
        n=0

        for i, col in enumerate (list_header):
            tree_Aluno.heading(col, text=col.title(), anchor=NW)
            tree_Aluno.column(col, width=h[n],anchor=hd[n])

        n+=1

        for item in df_list:
            
            id = item[0]
            nome = item[1]
            curso = item[3]
            turma = item[5]
            codigo = item[4]
            tree_Aluno.insert('', 'end', values=(id, nome, curso, turma, codigo))
        tree_Aluno.bind("<Double-1>", preencher_campos)
    
    mostrar_ocorrencia()


#Função para salvar (Responsavel por criar o arquivo PDF, defininido suas dimensões, fontes e etc)
#É inicializada apartir do momento em que o usuario clica em "Salvar" do frame detalhes
def salvar():
   
    dados = ver_alunos()
    if not dados:
        messagebox.showwarning("Aviso", "Nenhum dado encontrado para salvar.")
        return

    nome_arquivo = f"relatorio_ocorrencias_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.pdf"
    c = canvas.Canvas(nome_arquivo, pagesize=A4)
    largura, altura = A4

    x = 30
    y = altura - 50

    c.setFont("Helvetica-Bold", 14)
    c.drawString(x, y, "Relatório de Ocorrências - IEMA")
    y -= 30

    headers = ["ID", "Nome", "Data", "Curso", "Código", "Turma", "Professor", "Disciplina"]
    col_widths = [30, 100, 60, 80, 50, 50, 100, 100]  # largura em pontos de cada coluna

    c.setFont("Helvetica-Bold", 9)
    for i, header in enumerate(headers):
        c.drawString(x + sum(col_widths[:i]), y, header)
    y -= 15
    c.setFont("Helvetica", 8)

    for aluno in dados:
        if y < 60:  # Quebra de página
            c.showPage()
            y = altura - 50
            c.setFont("Helvetica-Bold", 9)
            for i, header in enumerate(headers):
                c.drawString(x + sum(col_widths[:i]), y, header)
            y -= 15
            c.setFont("Helvetica", 8)

        for i, dado in enumerate(aluno):
            texto = str(dado)
            texto = texto if len(texto) <= 30 else texto[:27] + "..."  # Trunca texto longo
            c.drawString(x + sum(col_widths[:i]), y, texto)
        y -= 12

    c.save()
    messagebox.showinfo("Sucesso", f"Relatório PDF salvo como '{nome_arquivo}'.")

janela.mainloop()
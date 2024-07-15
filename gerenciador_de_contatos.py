from operator import contains
import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / 'contatos.sqlite')
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

# def criar_tabela(conexao, cursor):
#     cursor.execute('CREATE TABLE contatos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), telefone VARCHAR(11))')
#     conexao.commit()
# criar_tabela(conexao, cursor)

def inserir_contato(conexao, cursor, nome, telefone):
    data = (nome, telefone)
    cursor.execute('INSERT INTO contatos (nome, telefone) VALUES (?,?);', (data))
    conexao.commit()

def buscar_contato(conexao, cursor, nome, telefone):
    data = (nome, telefone)
    cursor.execute('SELECT * FROM contatos WHERE nome=? AND telefone=?', (data))
    contatos = cursor.fetchall()
    if contatos:
        for contato in contatos:
            print(f"Nome: {contato['nome']} - Telefone: {contato['telefone']}")
    else:
        print(f"Contato {nome} não encontrado.")
def listar_contatos(conexao, cursor):
    cursor.execute('SELECT * FROM contatos')
    contatos = cursor.fetchall()
    if contatos:
        print("Lista de contatos:")
        for contato in contatos:
            print(f"Nome: {contato['nome']} - Telefone: {contato['telefone']}")
    else:
        print("Lista de contatos vazia.")
def editar_contato(conexao, cursor, nome, novo_telefone):
    data = (novo_telefone, nome)
    try:
        cursor.execute('UPDATE contatos SET telefone=? WHERE nome=?', data)
        conexao.commit() 
    except sqlite3.Error as e:
        print(f"Erro ao editar contato: {e}")
def deletar_contato(conexao, cursor, nome, telefone):
    data = (nome, telefone)
    try:
        cursor.execute('DELETE FROM contatos WHERE nome=? AND telefone=?', data)
        conexao.commit()
    except sqlite3.Error as e:
        print(f"Erro ao deletar contato: {e}")



    

def menu():
    while True:
        print("\n=== Gerenciador de Contatos ===")
        print("1. Adicionar contato")
        print("2. Buscar contato")
        print("3. Listar contatos")
        print("4. Editar contato")
        print("5. Excluir contato")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o número do contato: ")
            inserir_contato(conexao, cursor, nome, telefone)
        elif opcao == "2":
            nome = input("Digite o nome a ser procurado: ")
            telefone = input("Digite o número a ser procurado: ")
            buscar_contato(conexao, cursor, nome, telefone)
        elif opcao == "3":
            listar_contatos(conexao, cursor)
        elif opcao == "4":
            nome = input("Digite o nome do contato a editar: ")
            novo_telefone = input("Digite o novo telefone: ")
            editar_contato(conexao, cursor, nome, novo_telefone)
        elif opcao == "5":
            nome = input("Digite o nome do contato para ser deletar: ")
            telefone = input("Digite o número a ser deletado: ")
            deletar_contato(conexao, cursor, nome, telefone)
        elif opcao == "6":
            break
menu()

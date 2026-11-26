import mysql.connector
import pandas as pandas

# Construir a conexão com o servidor MYSQL
def conectar():
    conexao = mysql.connector.connect(
        host = "localhost", # onde esta o mysql
        user = "desenvolvedor",
        password = "desen123",
        database = "biblioteca_jogos" # o banco que vamos usar
    )
    return conexao 

def cadastrar(titulo, plataforma, genero, status_jogo, nota, preco):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO jogos (titulo, plataforma, genero, status_jogo, nota, preco) VALUES (%s, %s, %s, %s, %s, %s)",
        (titulo, plataforma, genero, status_jogo, nota, preco)
    )
    conexao.commit()
    cursor.close()
    conexao.close()
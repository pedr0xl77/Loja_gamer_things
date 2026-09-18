import mysql.connector 
from mysql.connector import Error

def conectar():
    try:
        # Substitua com os dados do seu banco
        banco = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="12345678",
                    database="db_projeto"
        )
        
        if banco.is_connected():
            return banco

    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

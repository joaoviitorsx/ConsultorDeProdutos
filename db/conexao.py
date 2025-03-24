import mysql.connector
from mysql.connector import Error

#cnpj atacado = 32768826000272
#cnpj jm = 00092104000173

def conectar_com_banco():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="consulta_produtos",
            port=3306
        )
        if conexao.is_connected():
            print('Conectado ao banco de dados')
            return conexao
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
    

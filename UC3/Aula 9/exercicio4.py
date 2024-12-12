import mysql.connector

# Conexão com o banco de dados
cnx = mysql.connector.connect(
    user="python",
    password="aula@123",
    host="exemploaulacaio.mysql.database.azure.com",
    port=3306,
    database="escolasenac",  
)
# Consulta parametrizada

cursor = cnx.cursor()

print("Sistema de cadastro")
cadastro_usuario = input("Digite o seu nome: ")
senha_nova = input("Digite a sua senha: ")
query = "INSERT INTO usuario_secretaria (usuario, senha) VALUES (%s, %s);"
cursor.execute(query, (cadastro_usuario, senha_nova))
cnx.commit()
cursor.close()
cnx.close()
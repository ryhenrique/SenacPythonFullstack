import mysql.connector

# Conexão com o banco de dados

cnx = mysql.connector.connect(
    user="aluno",
    password="aula@123",
    host="aulabackend.mysql.database.azure.com",
    port=3306,
    database="escoladb",  
)

cursor = cnx.cursor()

query = "SELECT nome FROM alunos WHERE data_nascimento > '2005-01-01';"
cursor.execute(query)

for row in cursor.fetchall():
    print(row)

cursor.close()
cnx.close()



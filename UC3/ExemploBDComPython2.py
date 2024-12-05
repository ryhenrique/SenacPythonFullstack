import mysql.connector

# Conexão com o banco de dados
cnx = mysql.connector.connect(
    user="python",
    password="aula@123",
    host="exemploaularyan.mysql.database.azure.com",
    port=3306,
    database="escola",  
    ssl_disabled=True     
)

# Criação do cursor
cursor = cnx.cursor()

# Consulta
query = "SELECT nome, idade FROM aluno;"

cursor.execute(query)

# Processar os resultados
resultados = cursor.fetchall()

# Classificação dos alunos
for nome, idade in resultados:
    if idade < 12:
        print(f"{nome} é uma criança ({idade} anos).")
    elif 12 <= idade < 18:
        print(f"{nome} é um adolescente ({idade} anos).")
    else:
        print(f"{nome} é um adulto ({idade} anos).")

# Fechando o cursor e a conexão
cursor.close()
cnx.close()

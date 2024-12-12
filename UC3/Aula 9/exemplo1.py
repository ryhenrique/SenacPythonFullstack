import mysql.connector

# Conexão com o banco de dados
cnx = mysql.connector.connect(
    user="python",
    password="aula@123",
    host="exemploaulacaio.mysql.database.azure.com",
    port=3306,
    database="escolasenac",  
)

cursor = cnx.cursor()
nome_aluno = input("Digite o nome do aluno que deseja buscar: ")

# Consula parametrizada
query = "SELECT nome, idade, turno FROM aluno WHERE nome = %s;"
cursor.execute(query, (nome_aluno,))

resultados = cursor.fetchall()
if resultados:
    for nome, idade, turno in resultados:
        print(f"Aluno: {nome}, Idade: {idade}, Turno: {turno}")
else:
    print("Nenhum aluno encontrado com esse nome.")

cursor.close()
cnx.close()
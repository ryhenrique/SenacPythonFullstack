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



# Consulta parametrizada


idademenor = int(input("Digite a menor idade:"))
idademaior = int(input("Digite a maior idade:"))
query = "SELECT nome, idturma, idade, alergias FROM aluno WHERE idade between %s and %s and alergias = 'leite' is FALSE;"
cursor.execute(query,(idademenor, idademaior))
resultados = cursor.fetchall()
for nome, idturma,idade, alergias in resultados:
    if idade > idademenor and idade < idademaior:
        print(f"aluno: {nome} e a Turma é: {idturma} e a idade {idade}")


cursor.close()
cnx.close()
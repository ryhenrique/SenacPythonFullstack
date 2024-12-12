#1 - Faça um programa em python que consulte e retorne todos os CPF e endereços dos alunos com base em uma idade digitada pelo usuário.

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
idade = int(input("Digite a idade do aluno que deseja buscar: "))

# Consulta parametrizada
query = "SELECT CPF, endereco FROM aluno WHERE idade = %s;"
cursor.execute(query, (idade,))

resultados = cursor.fetchall()
if resultados:
    for CPF, endereco in resultados:
        print(f"CPF: {CPF} Endereço: {endereco}")
else:
    print("Nenhum aluno encontrado com essa idade!")

cursor.close()
cnx.close()
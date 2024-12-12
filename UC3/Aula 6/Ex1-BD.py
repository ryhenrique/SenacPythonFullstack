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
query = ("SELECT nome, endereco FROM aluno;")
cursor.execute(query)

# Processar os resultados
resultados = cursor.fetchall()

query2 = ("SELECT nome, idade, tipo_sanguineo from aluno;")
cursor.execute(query2)
resultados2 = cursor.fetchall()

query3 = ("SELECT nome, sexo, naturalidade from aluno")
cursor.execute(query3)
resultados3 = cursor.fetchall()

query4 = ("SELECT nome, sexo, naturalidade from aluno")
cursor.execute(query4)
resultados4 = cursor.fetchall()

#EX2 - Tipo Sanguíneo da Tabela Aluno

for nome, endereco in resultados:
    print(f" O nome do aluno é: {nome}\nO endereço do aluno é: {endereco}")

for nome, idade, tipo_sanguineo in resultados2:
    if(tipo_sanguineo in ["B+", "B-", "O-", "O+"]):
        print(f"Possível doador: {nome} {idade}")

#EX3 - Homens Cariocas e Mulheres Paulistas da Tabela Aluno
for nome, sexo, naturalidade in resultados3:
    if sexo in "M" and naturalidade in "Rio de Janeiro":
        print(f"O nome de todos alunos homens e cariocas é: {nome} e {naturalidade}")
    if sexo in "F" and naturalidade in "São Paulo":
        print(f"O nome das mulheres é {nome} e cidade: {naturalidade}")

#EX4 - Retornar CPF dos Estudantes que tem os 2 responsáveis Cadastros no BD
        
    for nome, cpf_responsavel1, cpf_responsavel2 in resultados4:
        if cpf_responsavel1 and cpf_responsavel2:
            print(f"{nome} tem dois responsáveis cadastrados no cpf")

# Fechando o cursor e a conexão
cursor.close()
cnx.close()
import mysql.connector
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__, template_folder='templates')

# Indica ao Flask que os arquivos .html estão dentro de "cadastro/templcates"



db_config = {
    'user': 'python',
    'password': 'aula@123',
    'host': 'exemploaulacaio.mysql.database.azure.com',
    'port': 3306,
    'database': 'escolasenac'
}

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')

        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()
        query = "INSERT INTO usuario_secretaria (usuario, senha) VALUES (%s, %s)"
        cursor.execute(query, (usuario, senha))
        cnx.commit()
        cursor.close()
        cnx.close()

        return redirect(url_for('cadastro'))
    else:
        return render_template('cadastro.html')
    
if __name__ == '__main__':
    app.run(debug=True)
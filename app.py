# Arquivo principal da aplicação Flask


# Importa a classe Flask do pacote Flask
from flask import Flask, render_template

# Importa os pacotes internos
import database as db

# Cria a instância 
#__name__ diz ao Flask onde está a raiz do projeto
app = Flask (__name__)

# Chave secreta - usada para proteger sessões 
# e formulários CSRF
app.config['SECRET_KEY'] = 'trocar_senha'
db.criar_tabela()

# Rota Principal 
# http://localhost:5000 , retorna Olá
@app.route ('/')
def index():
    alunos = db.listar_alunos() 
    total = db.contar_alunos()
    media = db.media_turma()                                                                                                                                                                                                
    return render_template('index.html', alunos=alunos, total=total, media=media)

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    return render_template('cadastrar.html')
# Debug 
if __name__ == '__main__':  
    app.run(debug=True)
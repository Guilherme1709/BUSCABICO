from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = (__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgres:gui13almeida@localhost/usuario'

db=SQLAlchemy(app)

class Cadastro(db.Model):
    __tablename__='usuario'
    email=db.Column(db.String(40), primary_key=True)
    senha=db.Column(db.String(30))
    nome=db.Column(db.String(40))
    cidade=db.Column(db.String(40))

    def __init__(self, senha, nome, cidade, bairro):
        self.senha = senha
        self.nome = nome
        self.cidade = cidade

@app.route('/criar', methods=['GET', 'POST'])
def criar():
    if request.method == 'POST':
        senha=request.form['senha']
        nome=request.form['nome']
        cidade=request.form['cidade']

        usuario = Cadastro(senha, nome, cidade)
        db.session.add(usuario)
        db.session.commit()
    return redirect('/')
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', titulo='Cadastrados')

@app.route('/cadastro')
def registro():
    return render_template('registro.html', titulo='Cadastro')

app.run()

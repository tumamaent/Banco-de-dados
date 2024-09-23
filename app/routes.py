from flask import Flask, Blueprint, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///veiculos.db'
db = SQLAlchemy(app)

bp = Blueprint('main', __name__)

class Veiculo(db.Model):
    __tablename__ = 'veiculos'
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String, nullable=False)
    modelo = db.Column(db.String, nullable=False)
    ano = db.Column(db.Integer, nullable=False)

@app.route('/')
def index():
    veiculos = Veiculo.query.all()
    return render_template('index.html', veiculos=veiculos)

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        ano = request.form['ano']
        # Criar o objeto veiculo antes de adicioná-lo à sessão
        veiculo = Veiculo(marca=marca, modelo=modelo, ano=ano)
        db.session.add(veiculo)
        db.session.commit()
        return redirect(url_for('index'))# Alterado para a função da rota, não o template
    return render_template('formularios.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    veiculo = Veiculo.query.get(id)
    if veiculo is None:
        return "Veículo não encontrado", 404  # Verifica se o veículo existe
    if request.method == 'POST':
        veiculo.marca = request.form['marca']
        veiculo.modelo = request.form['modelo']
        veiculo.ano = request.form['ano']
        db.session.commit()# Salva as alterações no banco de dados
        return redirect(url_for('index'))  
    return render_template('editar.html', veiculo=veiculo)

@app.route('/excluir/<int:id>', methods=['POST'])# Rota para excluir
def excluir(id):
    veiculo = Veiculo.query.get(id)
    if veiculo is None:
        return "Veículo não encontrado", 404 # Verifica se o veículo existe
    db.session.delete(veiculo)# Remove o veículo da sessão
    db.session.commit()# Confirma a exclusão
    return redirect(url_for('index'))# Redireciona para a lista de veículos

if __name__ == '__main__':
    db.create_all()  
    app.run(debug=True)

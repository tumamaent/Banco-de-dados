from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicializa a aplicação Flask
app = Flask(__name__)

# Configurações do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///veiculos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o banco de dados
db = SQLAlchemy(app)

# Importa os modelos
from models import Usuario, Veiculo, Reserva, Manutencao  # Ajuste conforme necessário

# Importa e registra os blueprints
from routes import main  # Ajuste conforme o nome do seu arquivo de rotas
app.register_blueprint(main)

# Cria as tabelas no banco de dados, se não existirem
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicializa o banco de dados
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configurações do aplicativo
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa o banco de dados com o app
    db.init_app(app)

    # Importa os modelos
    from .models import Usuario, Reserva# Ajuste conforme necessário

    # Registra blueprints
    from .routes import main# Ajuste conforme necessário
    app.register_blueprint(main)

    # Cria as tabelas no banco de dados
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_app().run(debug=True)

from app import db, create_app
from app.models import User,Veicles

# Crea la aplicación
app = create_app()

# Crear la base de datos dentro del contexto de la aplicación
with app.app_context():
    db.create_all()
    print("Banco de datos creado perfectamente")
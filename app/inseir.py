from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import db, Usuario, Veiculo, Reserva, Manutencao  # Ajuste conforme a estrutura do seu projeto

# Configurar a conexão com o banco de dados
engine = create_engine('sqlite:///veiculos.db')  # Use o mesmo URI do seu aplicativo
Session = sessionmaker(bind=engine)
session = Session()

def inserir_usuario(nome, email, senha):
    usuario = Usuario(nome=nome, email=email, senha=senha)
    session.add(usuario)
    session.commit()
    print(f"Usuário {nome} adicionado com sucesso!")

def inserir_veiculo(marca, modelo, ano):
    veiculo = Veiculo(marca=marca, modelo=modelo, ano=ano)
    session.add(veiculo)
    session.commit()
    print(f"Veículo {modelo} adicionado com sucesso!")

def inserir_reserva(usuario_id, veiculo_id, data_inicio, data_fim):
    reserva = Reserva(usuario_id=usuario_id, veiculo_id=veiculo_id, data_inicio=data_inicio, data_fim=data_fim)
    session.add(reserva)
    session.commit()
    print(f"Reserva para o veículo ID {veiculo_id} criada com sucesso!")

def inserir_manutencao(veiculo_id, descricao, data):
    manutencao = Manutencao(veiculo_id=veiculo_id, descricao=descricao, data=data)
    session.add(manutencao)
    session.commit()
    print(f"Manutenção para o veículo ID {veiculo_id} registrada com sucesso!")

if __name__ == "__main__":
    # Exemplos de inserção
    inserir_usuario('João Silva', 'joao@example.com', 'senha123')
    inserir_veiculo('Toyota', 'Corolla', 2020)
    inserir_reserva(1, 1, datetime(2024, 9, 20), datetime(2024, 9, 25))  # IDs fictícios
    inserir_manutencao(1, 'Troca de óleo', datetime(2024, 9, 18))

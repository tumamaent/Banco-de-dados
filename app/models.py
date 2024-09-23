from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

db = declarative_base()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)
    reservas = relationship('Reserva', back_populates='usuario')

class Veiculo(db.Model):
    __tablename__ = 'veiculos'
    id = Column(Integer, primary_key=True)
    marca = Column(String, nullable=False)
    modelo = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    manutencoes = relationship('Manutencao', back_populates='veiculo')
    reservas = relationship('Reserva', back_populates='veiculo')

class Reserva(db.Model):
    __tablename__ = 'reservas'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    veiculo_id = Column(Integer, ForeignKey('veiculos.id'), nullable=False)
    data_inicio = Column(DateTime, nullable=False)
    data_fim = Column(DateTime, nullable=False)
    usuario = relationship('Usuario', back_populates='reservas')
    veiculo = relationship('Veiculo', back_populates='reservas')

class Manutencao(db.Model):
    __tablename__ = 'manutencoes'
    id = Column(Integer, primary_key=True)
    veiculo_id = Column(Integer, ForeignKey('veiculos.id'), nullable=False)
    descricao = Column(String, nullable=False)
    data = Column(DateTime, nullable=False)
    veiculo = relationship('Veiculo', back_populates='manutencoes')


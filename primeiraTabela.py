import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()

class Artista(Base):
    __tablename__ = "artista"
    artista_id = Column(Integer, primary_key=True)
    nome = Column(String)

engine = create_engine('sqlite:///artistas.db', echo=True)
Base.metadata.create_all(bind=engine)

Conexao = sessionmaker(bind=engine)
conexao = Conexao()
conexao: sessionmaker

novo_artista = Artista()
novo_artista.artista_id = 1
novo_artista.nome = "Artista 1"
conexao.add(novo_artista)
conexao.commit()
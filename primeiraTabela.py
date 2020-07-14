import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Sequence, Numeric, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
Base = declarative_base()

class Artista(Base):
    __tablename__ = "artista"
    artista_id = Column(Integer,Sequence("artista_id_auto_incremento", start=1), primary_key=True)
    nome = Column(String)
    albuns = relationship('Album')

class Album(Base):
    __tablename__ = "album"
    album_id = Column(Integer, Sequence("album_id_auto_incremento", start=1), primary_key=True) 
    titulo = Column(String)
    preco = Column(Numeric(10,2))
    artista_id = Column(Integer, ForeignKey('artista.artista_id'))
    
    cancoes = relationship('Cancao')

class Cancao(Base):
    __tablename__ = "cancao"
    cancao_id = Column(Integer, Sequence('cancao_id_auto_incremento', start=1), primary_key=True)
    nome = Column('String')
    album_id = Column(Integer, ForeignKey('album.album_id'))
engine = create_engine('sqlite:///artistas.db', echo=True)
Base.metadata.create_all(bind=engine)

Conexao = sessionmaker(bind=engine)
conexao = Conexao()
conexao: sessionmaker

# novo_artista = Artista()
# novo_artista.artista_id = 1
# novo_artista.nome = "Artista 1"
# conexao.add(novo_artista)
# conexao.commit()

# resultado = conexao.query(Artista).all()

# for item in resultado:
#     print(item.artista_id)
#     print(item.nome)

# novo_artista2 = Artista()
# novo_artista2.artista_id = 2
# novo_artista2.nome = "Artista 2"
# conexao.add(novo_artista2)
# conexao.commit()
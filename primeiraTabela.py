import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Artista(Base):
    __tablename__ = "artista"
    artista_id = Column(Integer, primary_key=True)
    nome = Column(String)

engine = create_engine('sqlite:///artistas.db', echo=True)
Base.metadata.create_all(bind=engine)
import subprocess
from getpass import getpass
from typing import List
import os
import json
from sqlalchemy import Column, String, Integer, create_engine, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy.orm import DeclarativeBase
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

database_name = os.getenv('YT_DB_NAME')
db_username = os.getenv('YT_DB_USER')
db_userpassword = os.getenv('YT_DB_PASSWORD')
db_host = os.getenv('YT_DB_HOST')
db_host_port = os.getenv('YT_DB_HOST_PORT')

database_path = "postgresql://{}{}{}@{}:{}/{}".format(
  db_username,
  ':' if len(db_userpassword) else '',
  db_userpassword,
  db_host,
  db_host_port,
  database_name
)

# DDL - data definition language

# Remove user and database
dbname = database_name
username = db_username

firstcmd = f'psql -U {username} postgres -c \'DROP DATABASE "{dbname}";\''

try:
  subprocess.check_callcall(firstcmd, shell=True)
except:
  print('Error droping database, did it already exist?')

passw = db_userpassword

# Create database
create_db = f"CREATE DATABASE \"{dbname}\" OWNER \"{username}\";"
try:
  subprocess.check_call(f'psql -U {username} postgres -c \'{create_db}\'', shell=True)
except:
  print(f'Error creating database {dbname}. Please verify if it already exists and is not locked by another application.')
  exit(1)

engine = create_engine(database_path)

def makeSession():
  Session = sessionmaker(engine)
  return Session()

class Base(DeclarativeBase):
  def insert(self, session, toCommit=False):
    session.add(self)
    if (toCommit):
      session.commit()

  def update(self, session):
    session.commit()

class AssocPalestranteSetor(Base):
  __tablename__ = "palestr_sect_assoc_table"

  palestrante_id: Mapped[int] = mapped_column(ForeignKey("palestrantes.id"),
                                              primary_key=True)
  setor_id: Mapped[int] = mapped_column(ForeignKey("setores.id"),
                                        primary_key=True)

class Setores(Base):
  __tablename__ = "setores"

  def __init__(self, nome):
    self.nome = nome

  id: Mapped[int] = mapped_column(primary_key=True)
  nome: Mapped[str] = mapped_column(String(50))

  def __repr__(self) -> str:
    return f"Setor(id={self.id!r}, name={self.nome!r})"

class Palestrantes(Base):
  __tablename__ = "palestrantes"

  def __init__(self, nome, listSetores: List[Setores], afiliacao, experiencia):
    self.nome = nome
    self.setores = listSetores
    self.afiliacao = afiliacao
    self.experiencia = experiencia

  id: Mapped[int] = mapped_column(primary_key=True)
  nome: Mapped[str] = mapped_column(String(100))
  afiliacao: Mapped[str] = mapped_column(String(100))
  experiencia: Mapped[int]

  setores: Mapped[List["Setores"]] = relationship(
    secondary=AssocPalestranteSetor.__table__,
  )

class CategoriasVideo(Base):
  __tablename__ = "categorias_video"

  def __init__(self, nome):
    self.nome = nome

  id: Mapped[int] = mapped_column(primary_key=True)
  nome: Mapped[str] = mapped_column(String(50))

class AssocVideosPalestrantes(Base):
  __tablename__ = "videos_palestr_assoc_table"

  palestrante_id: Mapped[int] = mapped_column(ForeignKey("palestrantes.id"),
                                              primary_key=True)
  video_id: Mapped[int] = mapped_column(ForeignKey("videos.id"),
                                        primary_key=True)


class Videos(Base):
  __tablename__ = "videos"

  def __init__(self, title, yt_id, categoria, palestrantes):
    self.title = title
    self.yt_id = yt_id
    self.categoria = categoria
    self.palestrantes = palestrantes

  id: Mapped[int] = mapped_column(primary_key=True)
  title: Mapped[str] = mapped_column(String(100))

  # o youtube id é o valor que vem na URL do video após https://www.youtube.com/watch?v=
  yt_id: Mapped[str] = mapped_column(String(11), unique=True)

  categoria_id: Mapped[int] = mapped_column(ForeignKey("categorias_video.id"))
  categoria: Mapped['CategoriasVideo'] = relationship()

  palestrantes: Mapped[List["Palestrantes"]] = relationship(
    secondary=AssocVideosPalestrantes.__table__,
  )

Base.metadata.create_all(engine)

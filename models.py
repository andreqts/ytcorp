import subprocess
from getpass import getpass
from typing import List
import os
import json
from sqlalchemy import Column, String, Integer, create_engine
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
subprocess.call(firstcmd, shell=True)

passw = db_userpassword

# Create database
create_db = f"CREATE DATABASE \"{dbname}\" OWNER \"{username}\";"
subprocess.call(f'psql -U {username} postgres -c \'{create_db}\'', shell=True)

engine = create_engine(database_path, echo=True)

def makeSession():
  Session = sessionmaker(engine)
  return Session()

class Base(DeclarativeBase):
  def insert(self, session, toCommit=False):
    session.add(self, session)
    if (toCommit):
      session.commit()

  def update(self, session):
    session.commit()

with engine.connect() as conn:
  result = conn.execute(text("select 'hello world yt'"))
  print(result.all())

palestr_sect_assoc_table = Table(
    "palestr_sect_assoc_table",
    Base.metadata,
    Column("palestrante_id", ForeignKey("palestrante.id")),
    Column("setor_id", ForeignKey("setor.id")),
)

class Palestrante(Base):
  __tablename__ = "palestrante"

  def __init__(self, nome, listSetores, afiliacao, experiencia):
    self.nome = nome
    self.setores = listSetores
    self.afiliacao = afiliacao
    self.experiencia = experiencia

  id: Mapped[int] = mapped_column(primary_key=True)
  nome: Mapped[str] = mapped_column(String(100))

  setores: Mapped[List['Setor']] = relationship(secondary=palestr_sect_assoc_table)
  afiliacao: Mapped[str] = mapped_column(String(100))
  experiencia: Mapped[int]

class Setor(Base):
  __tablename__ = "setor"

  def __init__(self, nome):
    self.nome = nome

  id: Mapped[int] = mapped_column(primary_key=True)
  nome: Mapped[str] = mapped_column(String(50))

  def __repr__(self) -> str:
    return f"Setor(id={self.id!r}, name={self.nome!r})"

Base.metadata.create_all(engine)

from typing import List
import os
from sqlalchemy import Column, String, Integer, create_engine
import json
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

class Base(DeclarativeBase):
  pass

engine = create_engine(database_path, echo=True)

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

  id: Mapped[int] = mapped_column(primary_key=True)
  nome: Mapped[str] = mapped_column(String(100))

  setor: Mapped[List['Setor']] = relationship(secondary=palestr_sect_assoc_table)
  afiliacao: Mapped[str] = mapped_column(String(100))
  experiencia: Mapped[int]

class Setor(Base):
  __tablename__ = "setor"

  id: Mapped[int] = mapped_column(primary_key=True)
  nome: Mapped[str] = mapped_column(String(50))


# def __repr__(self) -> str:
#   return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

Base.metadata.create_all(engine)

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
# def setup_db(app, database_path=database_path):
#     app.config["SQLALCHEMY_DATABASE_URI"] = database_path
#     app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#     db.app = app
#     db.init_app(app)
#     db.create_all()

# '''
# Question

# '''
# class Question(db.Model):  
#   __tablename__ = 'questions'

#   id = Column(Integer, primary_key=True)
#   question = Column(String)
#   answer = Column(String)
#   category = Column(String)
#   difficulty = Column(Integer)

#   def __init__(self, question, answer, category, difficulty):
#     self.question = question
#     self.answer = answer
#     self.category = category
#     self.difficulty = difficulty

#   def insert(self):
#     db.session.add(self)
#     db.session.commit()

#   def update(self):
#     db.session.commit()

#   def delete(self):
#     db.session.delete(self)
#     db.session.commit()

#   def format(self):
#     return {
#       'id': self.id,
#       'question': self.question,
#       'answer': self.answer,
#       'category': self.category,
#       'difficulty': self.difficulty
#     }

# '''
# Category

# '''
# class Category(db.Model):  
#   __tablename__ = 'categories'

#   id = Column(Integer, primary_key=True)
#   type = Column(String)

#   def __init__(self, type):
#     self.type = type

#   def format(self):
#     return {
#       'id': self.id,
#       'type': self.type
#     }
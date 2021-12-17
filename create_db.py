from sqlalchemy import create_engine
from sqlalchemy.sql.schema import CheckConstraint, ForeignKey
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Date, Boolean


engine = create_engine("postgresql+psycopg2://postgres:1111@localhost/library")
if not database_exists(engine.url):
    create_database(engine.url)


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    location = Column(String)
    sub = Column(Boolean)


class Publisher(Base):
    __tablename__ = 'publs'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    location = Column(String)
    books = relationship('Book')


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    author = Column(String)
    desc = Column(String)
    genre = Column(String)
    publisher = Column(Integer, ForeignKey('publs.id'))
    release_date = Column(Date)
    age_restriction = Column(Integer)


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    text = Column(String)
    grade = Column(Integer, CheckConstraint('grade > 0 AND grade <= 10'))


Base.metadata.create_all(engine)
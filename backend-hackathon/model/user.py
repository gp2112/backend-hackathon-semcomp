from sqlalchemy import Column, String, Integer, DateTime
from model import Base
from datetime import datetime


class User(Base):
    __tablename__ = 'user'
    username = Column(String(10), primary_key=True)
    password = Column(String(64), nullable=False)  # hashedpass
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    localizacao_lat = Column(Integer(), nullable=True)
    localizacao_lon = Column(Integer(), nullable=True)
    created_on = Column(DateTime(), default=datetime.now, nullable=False)

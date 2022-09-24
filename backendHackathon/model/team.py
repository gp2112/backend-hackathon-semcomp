from sqlalchemy import Column, String, Integer
from model import Base


class Team(Base):
    __tablename__ = 'team'
    id = Column(Integer(), primary_key=True)
    name = Column(String(30), index=True)
    uf = Column(String(2))
    logo = Column(String(100), nullable=False)  # url
    sport = Column(String(20), nullable=False)

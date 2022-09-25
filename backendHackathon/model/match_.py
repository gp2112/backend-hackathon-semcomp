from sqlalchemy import Column, Integer, ForeignKey, DateTime
from model import Base


class Match(Base):
    __tablename__ = 'match'
    id = Column(Integer(), primary_key=True)
    team_a = Column(Integer(), index=True)
    team_b = Column(Integer(), ForeignKey('team.id'), index=True)
    starts_on = Column(DateTime(), nullable=False, index=True)


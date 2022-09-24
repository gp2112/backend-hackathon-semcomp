from sqlalchemy import Column, Integer, ForeignKey
from model import Base


class PlaceMatch(Base):
    __tablename__ = 'placematch'
    place = Column(Integer(), ForeignKey('place.id'), primary_key=True),
    matchId = Column(Integer(), ForeignKey('match.id'),
                     primary_key=True, index=True)
    quantTeamA = Column(Integer(), default=0)
    quantTeamB = Column(Integer(), default=0)

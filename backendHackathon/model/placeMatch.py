from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from model import Base


class PlaceMatch(Base):
    __tablename__ = 'placematch'
    lat = Column(ForeignKey('place.lat'), primary_key=True),
    lon = Column(ForeignKey('place.lon'), primary_key=True),
    matchId = Column(ForeignKey('match.id'),
                     primary_key=True, index=True)
    quantTeamA = Column(Integer(), default=0)
    quantTeamB = Column(Integer(), default=0)

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from model import Base
from model.match_ import Match


class Team(Base):
    __tablename__ = 'team'
    id = Column(Integer(), primary_key=True)
    name = Column(String(30), index=True)
    uf = Column(String(2))
    logo = Column(String(100), nullable=False)  # url
    sport = Column(String(20), nullable=False)

    matches = relationship('Match')

    def toDict(self):
        return {
                'id': self.id,
                'name': self.name,
                'uf': self.uf,
                'logo': self.logo,
                'sport': self.sport
            }

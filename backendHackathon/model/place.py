from sqlalchemy import Column, String, Integer, Float,  \
        ForeignKey, DateTime
from model import Base
from datetime import datetime


class Place(Base):
    __tablename__ = 'place'
    lat = Column(Float(), primary_key=True)
    lon = Column(Float(), primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(), nullable=True)
    address = Column(String(100), nullable=False)
    uf = Column(String(2), nullable=False)
    city = Column(String(2), nullable=False)
    created_by = Column(String(10), ForeignKey('user.name'), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_by = Column(String(10), ForeignKey('user.name'), nullable=True)
    updated_on = Column(DateTime(),
                        default=datetime.now, onupdate=datetime.now)

    def toDict(self):
        return {
                'latitude': self.lat,
                'longitude': self.lon,
                'name': self.name,
                'description': self.description,
                'address': self.address,
                'uf': self.uf,
                'city': self.city
            }


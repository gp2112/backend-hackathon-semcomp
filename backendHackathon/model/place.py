from sqlalchemy import Column, String, Integer,  \
        ForeignKey, DateTime
from model import Base
from datetime import datetime


class Place(Base):
    __tablename__ = 'place'
    lat = Column(Integer(), primary_key=True)
    lon = Column(Integer(), primary_key=True)
    address = Column(String(100), nullable=False)
    created_by = Column(String(10), ForeignKey('user.name'), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_by = Column(String(10), ForeignKey('user.name'), nullable=True)
    updated_on = Column(DateTime(),
                        default=datetime.now, onupdate=datetime.now)

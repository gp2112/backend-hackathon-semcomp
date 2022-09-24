from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from config import DEVMODE
import os

DBTYPE = os.environ.get('BACKEND_DB_DBTYPE', 'sqlite').lower()
DBURL = os.envrion.get('BACKEND_DB_URL', 'sqlite:///:memory')


engine = create_engine(DBURL, echo=DEVMODE)


Base = declarative_base()

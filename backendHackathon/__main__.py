from tests import testdb
from model import engine, Base

Base.metadata.create_all(engine)
testdb.testall()

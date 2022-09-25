from tests import testdb
from model import engine, Base
from flask import Flask

from controller.place import place_bp

import sys

if '--testdb' in sys.argv:
    Base.metadata.create_all(engine)
    testdb.testall()

app = Flask(__name__)

app.register_blueprint(place_bp, url_prefix='/place')


@app.get('/')
def root():
    return 'Hello'


app.run()



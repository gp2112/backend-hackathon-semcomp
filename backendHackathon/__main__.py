from tests import testdb
from model import engine, Base
from flask import Flask

from controller.place import place_bp
from controller.placematches import placematch_bp
from controller.team import team_bp

import sys

if '--createdb' in sys.argv:
    Base.metadata.create_all(engine)
    testdb.testall()
    sys.exit(0)

app = Flask(__name__)

app.register_blueprint(place_bp, url_prefix='/place')
app.register_blueprint(placematch_bp, url_prefix='/matches')
app.register_blueprint(team_bp, url_prefix='/team')


@app.get('/')
def root():
    return 'Hello'


app.run()

from tests import testdb
from model import engine, Base
from flask import Flask
import sys

if '--test' in sys.argv:
    Base.metadata.create_all(engine)
    testdb.testall()

app = Flask(__name__)


@app.get('/')
def root():
    return 'Hello'


def main():
    app.run()


if __name__ == '__main__':
    main()

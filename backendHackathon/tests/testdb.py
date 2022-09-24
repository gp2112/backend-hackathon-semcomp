from sqlalchemy.orm import Session
from sqlalchemy import select
from model import engine
from model.team import Team
from model.user import User
from model.place import Place


def testInsertTeam():
    with Session(engine) as session:
        team = Team(
                name='Botafogo',
                uf='RJ',
                logo='urlfogao',
                sport='futebol'
            )
        session.add(team)
        session.commit()


def testInsertUser():
    with Session(engine) as session:
        user = User(
                username='gp2112',
                name='Guilherme',
                password='dmeko3djio3jdie',
                email='me@guip.dev'
            )
        session.add(user)
        session.commit()


def testInsertPlace():
    with Session(engine) as session:
        place = Place(
                lat=7653846,
                lon=9374989,
                address='av. prof. murtinho 999, sao paulo, sp',
                created_by='gp2112'
            )
        session.add(place)
        session.commit()


def testQueryTeam():
    with Session(engine) as session:

        s = select(Team)
        for r in session.scalars(s):
            print(r)


def testQueryUser():
    with Session(engine) as session:

        s = select(User)
        for r in session.scalars(s):
            print(r)


def testQueryPlace():
    with Session(engine) as session:

        s = select(Place)
        for r in session.scalars(s):
            print(r)


def testall():
    testInsertTeam()
    testQueryTeam()

    testInsertUser()
    testQueryUser()

    testInsertPlace()
    testQueryPlace()

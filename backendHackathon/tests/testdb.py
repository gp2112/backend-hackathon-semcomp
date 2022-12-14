from sqlalchemy.orm import Session
from sqlalchemy import select
from model import engine
from model.team import Team
from model.user import User
from model.place import Place
from model.match_ import Match

from services.team import get_team

from datetime import datetime


def testInsertTeam():
    with Session(engine) as session:
        team_a = Team(
                id=1,
                name='Botafogo',
                uf='RJ',
                logo='urlfogao',
                sport='futebol'
            )
        team_b = Team(
                id=2,
                name="Flamengo",
                uf="RJ",
                logo="urlflamengo",
                sport='futebol'
            )
        session.add_all([team_a, team_b])
        session.commit()


def testInsertUser():
    with Session(engine) as session:
        user = User(
                username='gp2112',
                name='Guilherme',
                password='dmeko3djio3jdie',
                email='me@guip.dev',
                localizacao_lat=27364.1,
                localizacao_lon=27384.2,
                uf='RJ',
                city='rio de janeiro'
            )
        session.add(user)
        session.commit()


def testInsertPlace():
    with Session(engine) as session:
        place = Place(
                lat=7653846,
                lon=9374989,
                address='av. prof. murtinho 999, sao paulo, sp',
                created_by='gp2112',
                name='bar do guip',
                city="Rio de Janeiro",
                uf="rj"
            )
        session.add(place)
        session.commit()


def testInsertMatch():
    with Session(engine) as session:
        m = Match(
                team_a=1,
                team_b=2,
                starts_on=datetime.now()
            )
        session.add(m)
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


def testQueryMatch():
    with Session(engine) as session:
        teams = session.query(Team).all()
        print([[(get_team(m.team_a), get_team(m.team_b)) for m in t.matches] for t in teams])


def testall():
    testInsertTeam()
    testQueryTeam()

    testInsertUser()
    testQueryUser()

    testInsertPlace()
    testQueryPlace()

    testInsertMatch()
    testQueryMatch()

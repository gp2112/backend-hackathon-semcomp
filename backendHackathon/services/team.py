from model.team import Team
from model import engine
from sqlalchemy.orm import Session


def get_team(team_id):
    with Session(engine) as session:
        t = session.query(Team).get(team_id)
        return t.toDict()


def get_teams():
    with Session(engine) as session:
        ts = session.query(Team).all()
        return [t.toDict() for t in ts]

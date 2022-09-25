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


def get_team_matches(team_id):
    with Session(engine) as session:
        t = session.query(Team).get(team_id)
        return [(get_team(m.team_a), get_team(m.team_b)) for m in t.matches]

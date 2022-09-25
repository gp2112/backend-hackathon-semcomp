from model.user import User
from model import engine
from sqlalchemy.orm import Session


def get_user(username: str) -> User:
    with Session(engine) as session:
        return session.query(User).get(username)

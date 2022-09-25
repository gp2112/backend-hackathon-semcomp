from model.place import Place
from model.placeMatch import PlaceMatch
from model.match_ import Match
from model import engine
from sqlalchemy.orm import Session


def get_place(lat: float, lon: float) -> dict:
    with Session(engine) as session:
        place = session.query(Place).get((lat, lon))
        return place.toDict()


def insert_place(lat: float, lon: float, name: str,
                 address: str, uf: str, city: str, created_by: str,
                 description: str = None):
    place = Place(
                lat=lat,
                lon=lon,
                name=name,
                address=address,
                description=description,
                created_by=created_by,
                city=city,
                uf=uf
            )
    with Session(engine) as session:
        session.add(place)
        session.commit()


def close_places(user, radius: float, dt: int, team: str):
    places = []
    with Session(engine) as session:
        places = session.query(PlaceMatch).join([PlaceMatch.lat, PlaceMatch.lon] == [Place.lat, Place.lon]).join(Match).filter(
                                                        Place.uf == user.uf and
                                                        Place.city == user.city and
                                                        Match.team_a == team and
                                                        Match.datetime >= dt).all()

    iR = lambda p: (p.lat-user.localizacao_lat)**2 + (p.lon-user.localizacao_lon)**2 <= radius

    places = filter(iR, places)
    return [p.toDict() for p in places]

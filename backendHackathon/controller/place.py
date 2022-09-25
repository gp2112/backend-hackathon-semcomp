from flask import Blueprint, request
from services.place import get_place, insert_place, close_places
from services.user import get_user

place_bp = Blueprint('place', __name__)


@place_bp.get('')
def getone():
    lat = request.args.get('lat', 0)
    lon = request.args.get('lon', 0)
    return get_place(lat, lon)


@place_bp.post('')
def create():
    place = request.get_json()

    insert_place(
                place.get('lat'),
                place.get('lon'),
                place.get('name'),
                place.get('address'),
                place.get('uf'),
                place.get('city'),
                place.get('created_by'),
                place.get('description'),
            )
    return {"code": 200, "message": "success"}




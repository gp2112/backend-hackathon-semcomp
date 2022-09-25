from flask import Blueprint, request
from services.place import get_place, insert_place, close_places
from services.user import get_user

placematch_bp = Blueprint('placematch', __name__)

# @placematch_bp.get()


@placematch_bp.get('/close')
def search():
    username = request.args.get('username')
    radius = float(request.args.get('radius', 0))
    from_dt = int(request.args.get('from', 0))
    team = request.args.get('team')

    user = get_user(username)
    print(user.localizacao_lat, user.localizacao_lon)
    return close_places(user, radius, from_dt, team)

from flask import Blueprint, request
from services.team import get_team

team_bp = Blueprint('team', __name__)


@team_bp.get('')
def geteam():
    team_id = int(request.args.get('id', -1))
    return get_team(team_id)

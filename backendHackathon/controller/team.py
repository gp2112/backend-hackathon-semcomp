from flask import Blueprint, request
from services.team import get_team, get_team_matches

team_bp = Blueprint('team', __name__)


@team_bp.get('/<team_id>')
def geteam(team_id: int):
    return get_team(team_id)


@team_bp.get('/<team_id>/matches')
def getmatches(team_id):
    return get_team_matches(team_id)

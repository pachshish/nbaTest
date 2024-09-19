from flask import Blueprint, requests, jsonify, abort

from services.teamService import create_team as insert_team, put_team, delete_team, geting_team


teams_db = Blueprint('teams', __name__, url_prefix='/teams')


@teams_db.route('/teams', methods=['POST'])
def create_team():
    if not requests.json or 'name' not in requests:
        abort(400, description="bad request")
    result = insert_team(requests)
    if result.get('error'):
        return jsonify(result), 400
    return jsonify(result), 201


@teams_db.route('/teams/int: <team_id>', methods=['PUT'])
def update_team(team_id):
    if not requests.json or 'name' not in requests:
        abort(400, description="bad request")
    result = put_team(requests, team_id)
    if result.get('error'):
        return jsonify(result), 400
    return jsonify(result), 200


@teams_db.route('/teams/int: <team_id>', methods=['DELETE'])
def delete(team_id):
    result = delete_team(team_id)
    return result


@teams_db.route('/teams/int: <team_id>', methods=['GET'])
def get_team(team_id):
    result = geting_team(team_id)
    return result


# @teams_db.route('/teams/int: <team1>/int: <team2>', methods=['GET'])







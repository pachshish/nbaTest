from flask import Flask, Blueprint, request, jsonify
from db import db

from services.playerService import get_players, get_players_from_API, create_player

players_db = Blueprint('players', __name__, url_prefix='/players')



@players_db.route('/players/string:<position>', methods=['GET'])
def get_players_by_position(position):
    pos = position
    result = request.get_json()
    players = get_players(result, pos)
    if players == "error":
        return jsonify(players), 400
    return jsonify(players), 201


@players_db.route('/init', methods=['GET'])
def initialize_players():
    data = get_players_from_API()
    return jsonify(create_player(data))


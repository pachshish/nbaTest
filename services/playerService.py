from flask import Flask, Blueprint, request, jsonify
import json



from models.playerModel import Player
from db import db
import requests


#בדיקה באיזה עונות השחקן שיחק
def check_seasons(a, b, c):
    one = ""
    two = ""
    three = "2024 He didn't play"
    if a is not None:
        one =  "2022"
    if b is not None:
        two = "2023"
    if c is not None:
        three = "2024"
    return f'played in {one}, {two} and {three}'


#חישוב סך הנקודות
def calculate_points(a, b, c):
    one = 0
    two = 0
    three = 0
    if a is not None:
        one = (int(a["twoFg"]) * 2) + (int(a["threeFg"]) * 3)
    if b is not None:
        two = (int(b["twoFg"]) * 2) + (int(b["threeFg"]) * 3)
    if c is not None:
        three = (int(c["twoFg"]) * 2) + (int(c["threeFg"]) * 3)
    return one + two + three


#חישוב סך המשחקים
def calculate_games(a, b, c):
    one = 0
    two = 0
    three = 0
    if a is not None:
        one = a["games"]
    if b is not None:
        two = b["games"]
    if c is not None:
        three = c["games"]
    return one + two + three


#אחוז קליעה ל2
def calculate_success_two(a, b, c):
    one = 0
    two = 0
    three = 0
    if a["twoPercent"] is not None:
        one = int(a["twoPercent"])
    if b["twoPercent"] is not None:
        two = int(b["twoPercent"])
    if c["twoPercent"] is not None:
        three = int(c["twoPercent"])
    return (one + two + three) / 3

#אחוז קליעה ל3
def calculate_success_three(a, b, c):
    one = 0
    two = 0
    three = 0
    if a["threePercent"] is not None:
        one = int(a["threePercent"])
    if b["threePercent"] is not None:
        two = int(b["threePercent"])
    if c["threePercent"] is not None:
        three = int(c["threePercent"])
    return (one + two + three) / 3


#חישוב הATR
def calculate_ATR(a, b, c):
    one = 0
    two = 0
    three = 0
    if a["assists"] != 0 and a["turnovers"] != 0:
        one = int(a["assists"]) / int(a["turnovers"])
    if b["assists"] != 0 and b["turnovers"] != 0:
        two = int(b["assists"]) / int(b["turnovers"])
    if c["assists"] != 0 and c["turnovers"] != 0:
        three = int(c["assists"]) / int(c["turnovers"])
    return (one + two + three) / 3

# def calculate_success_two(a, b, c):
#     one = 0
#     two = 0
#     three = 0
#     if a is not None:
#         one
#     if b is not None:
#         two
#     if c is not None:
#         three
#     return one + two + three

#הבאת כל השחקנים לעונות 2022, 2023, 2024
def get_players_from_API():
    urls = [
        'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season=2022&&pageSize=1000',
        'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season=2023&&pageSize=1000',
        'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season=2024&&pageSize=1000'
    ]

    responses = []
    for url in urls:
        try:
            response = requests.get(url, verify=False)
            response.raise_for_status()
            responses.append(response.json())
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {url}: {e}")
            return []

    response_2022, response_2023, response_2024 = responses
    print(response_2022)
    print(response_2023)
    print(response_2024)
    players = []
    for player in response_2022:
        for i in response_2023:
            if i["playerName"] == player["playerName"]:
                to = i
            else:
                to = None

        for j in response_2024:
            if j["playerName"] == player["playerName"]:
                three = j
            else:
                three = None

        new_player = Player(
            name=player["playerName"],
            position=player["position"],
            season=check_seasons(player, i, j),
            points=calculate_points(player, i, j),
            games=calculate_games(player, i, j),
            twoPercent=calculate_success_two(player, i, j),
            threePercent=calculate_success_three(player, i, j),
            ATR=calculate_ATR(player, i, j),
            PPGRatio= 0
        )
        players.append(new_player)
    return players
    # לבדוק אם הוא שינה עמדה במשך העוות

#עדכון הדאטא בייס בשחקן  חדש
def create_player(players: list) -> dict:
    try:
        for player in players:
            db.session.add(player)
            db.session.commit()
            return players.to_dict()
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

create_player(get_players_from_API())

#הצגת השחקנים שמשחקים בעמדה
def get_players(players, position):
    if players == None or position == None:
        return "error"
    players_in_position = []
    for player in players:
        if player["position"] == position:
            players_in_position.append(player)
    return players_in_position











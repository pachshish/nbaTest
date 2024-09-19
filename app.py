from flask import Flask, Blueprint, request, jsonify
from db import db
from services.playerService import get_players, get_players_from_API, create_player




app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()




def create_player(players: list) -> dict:
    try:
        for player in players:
            db.session.add(player)
        db.session.commit()
        return {"message": "Players added successfully."}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

# Route לדוגמה להוספת שחקנים
@app.route('/init', methods=['GET'])
def initialize_players():
    data = get_players_from_API()  # ודא שאתה מייבא את הפונקציה הזו
    return jsonify(create_player(data))

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
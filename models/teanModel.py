from db import db
from models import playerModel
from playerModel import Player


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    Point_Guard = db.Column(db.Player, nullable=False)
    Shooting_Guard = db.Column(db.Player, nullable=False)
    Small_Forward = db.Column(db.Player, nullable=False)
    Power_Forward = db.Column(db.Player, nullable=False)
    Center = db.Column(db.Player, nullable=False)
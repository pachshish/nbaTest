from db import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    season = db.Column(db.String(50), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    games = db.Column(db.Integer, nullable=False)
    twoPercent = db.Column(db.Integer, nullable=False)
    threePercent = db.Column(db.Integer, nullable=False)
    ATR = db.Column(db.Integer, nullable=False)
    PPGRatio = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'position': self.position,
            'season': self.season,
            'points': self.points,
            'games': self.games,
            'twoPercent': self.twoPercent,
            'threePercent': self.threePercent,
            'ATR': self.ATR,
            'PPGRatio': self.PPGRatio
        }


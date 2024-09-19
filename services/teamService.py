from models.teanModel import Team
from db import db




def create_team(team):
    try:
        new_team = Team(
            name=team["name"],
            Point_Guard=team["Point_Guard"],
            Shooting_Guard=team["Shooting_Guard"],
            Small_Forward=team["Small_Forward"],
            Power_Forward=team["Power_Forward"],
            Center=team["Center"]
        )
        db.session.add(new_team)
        db.session.commit()
        return team.to_dict()
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}


def put_team(apdate, id):
    try:
        existing_team = Team.query.get(id)

        if existing_team is None:
            return {"error": "Team not found"}, 404

        existing_team.name = apdate["name"]
        existing_team.Point_Guard = apdate["Point_Guard"]
        existing_team.Shooting_Guard = apdate["Shooting_Guard"]
        existing_team.Small_Forward = apdate["Small_Forward"]
        existing_team.Power_Forward = apdate["Power_Forward"]
        existing_team.Center = apdate["Center"]

        db.session.commit()
        return apdate
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500


def delete_team(id):
    try:
        team_to_delete = Team.query.get(id)

        if team_to_delete is None:
            return {"error": "Team not found"}, 404

        db.session.delete(team_to_delete)
        db.session.commit()

        return {"message": "Team deleted successfully"}, 200

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500


def geting_team(id):
    team = Team.query.get(id)

    if team is None:
        return {"error": "Team not found"}, 404
    return team


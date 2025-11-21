from flask import Blueprint, render_template, current_app

leaderboard_bp = Blueprint("leaderboard", __name__, template_folder="../templates")

@leaderboard_bp.route("/leaderboard")
def show_leaderboard():
    db = current_app.config['DB']
    top_pokemon = list(db["leaderboard"].find().sort("count", -1).limit(5))
    return render_template(
        "leaderboard.html",
        top=top_pokemon
    )
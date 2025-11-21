from flask import Blueprint, current_app, render_template, request, redirect, url_for, flash
from models.history import HistoryModel
from models.traits import TraitsModel
from models.leaderboard import LeaderboardModel
import requests
from config import POKEAPI_BASE

quiz_bp = Blueprint("quiz", __name__, template_folder="../templates", static_folder="../static")

@quiz_bp.route("/quiz", methods=["GET"])
def quiz_form():
    traits_list = ["brave", "loyal", "funny", "calm", "energetic", "curious", "stubborn", "playful", "smart", "shy"]
    return render_template("quiz.html", traits=traits_list)

@quiz_bp.route("/quiz", methods=["POST"])
def quiz_submit():
    db = current_app.config['DB']
    traits_model = TraitsModel(db)
    leaderboard = LeaderboardModel(db)
    history = HistoryModel(db)

    selected_traits = [
        request.form.get("trait1"),
        request.form.get("trait2"),
        request.form.get("trait3"),
        request.form.get("trait4")
    ]
    selected_traits = [t for t in selected_traits if t]
    if len(selected_traits) != 4:
        flash("Please select 4 traits.", "danger")
        return redirect(url_for("quiz.quiz_form"))

    companion = traits_model.get_pokemon_for_traits(selected_traits)
    if not companion:
        flash("No companion found for those traits. Try other traits.", "warning")
        return redirect(url_for("quiz.quiz_form"))

    poke_api_url = f"{POKEAPI_BASE}/{companion.lower()}"
    resp = requests.get(poke_api_url, timeout=10)
    if resp.status_code != 200:
        pokemon_data = {"name": companion, "image": None, "types": [], "abilities": []}
    else:
        data = resp.json()
        image = data.get("sprites", {}).get("other", {}).get("official-artwork", {}).get("front_default") \
                or data.get("sprites", {}).get("front_default")
        types = [t["type"]["name"] for t in data.get("types", [])]
        abilities = [a["ability"]["name"] for a in data.get("abilities", [])]
        pokemon_data = {
            "name": data.get("name", companion),
            "image": image,
            "types": types,
            "abilities": abilities
        }

    leaderboard.increment(pokemon_data["name"])

    history.add_history(selected_traits, pokemon_data["name"])

    return render_template("result.html", pokemon=pokemon_data, traits=selected_traits)

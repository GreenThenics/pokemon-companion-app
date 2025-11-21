from flask import Blueprint, redirect, render_template, request, current_app, url_for, flash
from models.history import HistoryModel

history_bp = Blueprint("history", __name__, template_folder="../templates")


@history_bp.route("/")
def history_dashboard():
    db = current_app.config["DB"]
    history_model = HistoryModel(db)

    recent = history_model.get_recent()
    best_by_trait = history_model.get_best_by_trait()
    combos = history_model.get_top_combos()

    return render_template(
        "history.html",
        recent=recent,
        best_by_trait=best_by_trait,
        combos=combos
    )

@history_bp.route("/search", methods=["GET"])
def search_history():
    db = current_app.config["DB"]
    history_model = HistoryModel(db)

    name = request.args.get("pokemon", "").lower()
    if not name:
        flash("Please enter a Pokémon name.", "warning")
        return redirect(url_for("history.history_dashboard"))

    records = history_model.search_by_pokemon(name)

    # fetch other data so the page stays complete
    recent = history_model.get_recent()
    best_by_trait = history_model.get_best_by_trait()
    combos = history_model.get_top_combos()

    return render_template(
        "history.html",
        recent=recent,
        best_by_trait=best_by_trait,
        combos=combos,
        search_results=records,
        search_query=name
    )


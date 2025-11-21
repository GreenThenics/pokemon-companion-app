from flask import Flask, render_template
from config import MONGO_URI, DB_NAME
from pymongo import MongoClient
from routes.quiz_routes import quiz_bp
from routes.leaderboard_routes import leaderboard_bp
from routes.history_routes import history_bp
import os

app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = os.getenv("SECRET_KEY", "dev-secret-key")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

app.config['DB'] = db

app.register_blueprint(quiz_bp)
app.register_blueprint(leaderboard_bp, url_prefix="/leaderboard")
app.register_blueprint(history_bp, url_prefix="/history")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("start.html")

@views.route('/options')
def options():
    return render_template("options.html")

@views.route('/player-selection')
def playerSelection():
    return render_template("player-selection.html")

@views.route('/scoreboard')
def score():
    return render_template("scoreboard.html")
